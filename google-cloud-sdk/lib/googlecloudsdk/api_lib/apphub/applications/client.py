# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Apphub Applications API."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager
from googlecloudsdk.api_lib.apphub import consts as api_lib_consts
from googlecloudsdk.api_lib.apphub import utils as api_lib_utils
from googlecloudsdk.api_lib.util import waiter


class ApplicationsClient(object):
  """Client for Applications in apphub API."""

  def __init__(self, client=None, messages=None):
    self.client = client or api_lib_utils.GetClientInstance()
    self.messages = messages or api_lib_utils.GetMessagesModule()
    self._app_client = self.client.projects_locations_applications
    self._lookup_client = self.client.projects_locations
    self._poller = waiter.CloudOperationPoller(
        self._app_client,
        self.client.projects_locations_operations,
    )
    self._delete_poller = waiter.CloudOperationPollerNoResources(
        self.client.projects_locations_operations,
    )
    self._lookup_poller = waiter.CloudOperationPoller(
        self._lookup_client,
        self.client.projects_locations_operations,
    )

  def Describe(self, app_id):
    """Describe an application in the Project/location.

    Args:
      app_id: str, the application id.

    Returns:
      Described service project Resource.
    """
    describe_req = self.messages.ApphubProjectsLocationsApplicationsGetRequest(
        name=app_id
    )
    return self._app_client.Get(describe_req)

  def List(
      self,
      parent,
      limit=None,
      page_size=100,
  ):
    """List applications in the Projects/Location.

    Args:
      parent: str, projects/{projectId}/locations/{location}
      limit: int or None, the total number of results to return. Default value
        is None
      page_size: int, the number of entries in each batch (affects requests
        made, but not the yielded results). Default value is 100.

    Returns:
      Generator of matching service projects.
    """
    list_req = self.messages.ApphubProjectsLocationsApplicationsListRequest(
        parent=parent
    )
    return list_pager.YieldFromList(
        self._app_client,
        list_req,
        field='applications',
        batch_size=page_size,
        limit=limit,
        batch_size_attribute='pageSize',
    )

  def Create(
      self,
      app_id,
      scope_type,
      display_name,
      description,
      attributes,
      async_flag,
      parent,
  ):
    """Creates an application in the Project/location.

    Args:
      app_id: str, Application ID
      scope_type: str, Scope of the Application
      display_name: str, Human-friendly display name
      description: str, Description of the Application
      attributes: Attributes, Attributes of the Application
      async_flag: Boolean value for async operation. If true the operation will
        be async
      parent: parent for project resource

    Returns:
      Application or Operation based on async flag value.
    """
    application = self.messages.Application(
        description=description,
        displayName=display_name,
        scope=self.messages.Scope(
            type=self.messages.Scope.TypeValueValuesEnum(scope_type)
        ),
        attributes=attributes,
    )

    create_req = self.messages.ApphubProjectsLocationsApplicationsCreateRequest(
        application=application, applicationId=app_id, parent=parent
    )
    operation = self._app_client.Create(create_req)

    if async_flag:
      return operation

    create_response = api_lib_utils.WaitForOperation(
        self._poller,
        operation,
        api_lib_consts.CreateApplication.WAIT_FOR_ADD_MESSAGE,
        api_lib_consts.CreateApplication.ADD_TIMELIMIT_SEC,
    )

    return create_response

  def Update(self, args):
    """Updates an Apphub application.

    Args:
      args: args, Arguments provided by the client

    Returns:
      Application or Operation based on async flag value.
    """

    update_mask = ''
    app_ref = args.CONCEPTS.application.Parse()

    attributes = api_lib_utils.GetMessagesModule().Attributes()
    application = self.messages.Application(attributes=attributes)

    if args.environment:
      attributes.environment = api_lib_utils.GetMessagesModule().Environment(
          environment=args.environment
      )
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_ENVIRONMENT_FIELD_NAME,
      )

    if args.criticality:
      criticality = api_lib_utils.GetMessagesModule().Criticality()
      criticality.level = args.criticality.get('level')
      criticality.missionCritical = args.criticality.get('mission-critical')
      attributes.criticality = criticality
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_CRITICALITY_FIELD_NAME,
      )

    for b_owner in args.business_owners or []:
      business_owner = api_lib_utils.GetMessagesModule().ContactInfo()
      business_owner.email = b_owner.get('email', None)
      if b_owner.get('display-name', None):
        business_owner.displayName = b_owner.get('display-name', None)
      if b_owner.get('channel-uri', None):
        business_owner.channel = api_lib_utils.GetMessagesModule().Channel(
            uri=b_owner.get('channel-uri')
        )
      attributes.businessOwners.append(business_owner)
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_BUSINESS_OWNERS_FIELD_NAME,
      )

    for d_owner in args.developer_owners or []:
      developer_owner = api_lib_utils.GetMessagesModule().ContactInfo()
      developer_owner.email = d_owner.get('email', None)
      if d_owner.get('display-name', None):
        developer_owner.displayName = d_owner.get('display-name', None)
      if d_owner.get('channel-uri', None):
        developer_owner.channel = api_lib_utils.GetMessagesModule().Channel(
            uri=d_owner.get('channel-uri')
        )
      attributes.developerOwners.append(developer_owner)
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_DEVELOPER_OWNERS_FIELD_NAME,
      )

    for o_owner in args.operator_owners or []:
      operator_owner = api_lib_utils.GetMessagesModule().ContactInfo()
      operator_owner.email = o_owner.get('email', None)
      if o_owner.get('display-name'):
        operator_owner.displayName = o_owner.get('display-name')
      if o_owner.get('channel-uri'):
        operator_owner.channel = api_lib_utils.GetMessagesModule().Channel(
            uri=o_owner.get('channel-uri')
        )
      attributes.operatorOwners.append(operator_owner)
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_OPERATOR_OWNERS_FIELD_NAME,
      )

    if args.display_name:
      application.displayName = args.display_name
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_DISPLAY_NAME_FIELD_NAME,
      )

    if args.description:
      application.description = args.description
      update_mask = api_lib_utils.AddToUpdateMask(
          update_mask,
          api_lib_consts.UpdateApplication.UPDATE_MASK_DESCRIPTION_FIELD_NAME,
      )

    patch_req = self.messages.ApphubProjectsLocationsApplicationsPatchRequest(
        application=application,
        name=app_ref.RelativeName(),
        updateMask=update_mask,
    )

    operation = self._app_client.Patch(patch_req)

    if args.async_:
      return operation

    patch_response = api_lib_utils.WaitForOperation(
        self._poller,
        operation,
        api_lib_consts.UpdateApplication.WAIT_FOR_UPDATE_MESSAGE,
        api_lib_consts.UpdateApplication.ADD_TIMELIMIT_SEC,
    )

    return patch_response

  def Delete(self, app_id, async_flag):
    """Delete an application in the Project/location.

    Args:
      app_id: str, The name for the application being deleted
      async_flag: Boolean value for async operation. If true the operation will
        be async

    Returns:
      Empty Response Message or Operation based on async flag value.
    """
    remove_req = self.messages.ApphubProjectsLocationsApplicationsDeleteRequest(
        name=app_id
    )
    operation = self._app_client.Delete(remove_req)

    if async_flag:
      return operation

    delete_response = api_lib_utils.WaitForOperation(
        self._delete_poller,
        operation,
        api_lib_consts.DeleteApplication.WAIT_FOR_DELETE_MESSAGE,
        api_lib_consts.DeleteApplication.REMOVE_TIMELIMIT_SEC,
    )

    return delete_response
