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
"""Apphub Command Lib Flags."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope.concepts import concepts
from googlecloudsdk.calliope.concepts import deps
from googlecloudsdk.command_lib.apphub import utils as apphub_utils
from googlecloudsdk.command_lib.util.concepts import concept_parsers
from googlecloudsdk.command_lib.util.concepts import presentation_specs


def AddTopologyUpdateFlags(parser):
  """Adds flags to topology update command.

  Flags include:
    --enable
    --disable

  Args:
    parser: The argparser.
  """

  state_group = parser.add_group(mutex=True, help='Manage topology state.')
  state_group.add_argument(
      '--enable',
      action='store_const',
      const=True,
      help='Enable topology.',
  )
  state_group.add_argument(
      '--disable',
      action='store_const',
      const=True,
      help='Disable topology.',
  )


def AddTelemetryUpdateFlags(parser):
  """Adds flags to telemetry update command.

  Flags include:
    --enable-monitoring
    --disable-monitoring

  Args:
    parser: The argparser.
  """

  state_group = parser.add_group(
      mutex=True, help='Manage telemetry monitoring state.'
  )
  state_group.add_argument(
      '--enable-monitoring',
      action='store_const',
      const=True,
      help='Enable telemetry monitoring.',
  )
  state_group.add_argument(
      '--disable-monitoring',
      action='store_const',
      const=True,
      help='Disable telemetry monitoring.',
  )


def GetGlobalLocationResourceSpec():
  return concepts.ResourceSpec(
      'apphub.projects.locations',
      resource_name='location',
      locationsId=_DefaultToGlobalLocationAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
  )


def _DefaultToGlobalLocationAttributeConfig(help_text=None):
  """Create basic attributes that fallthrough location to global in resource argument.

  Args:
    help_text: If set, overrides default help text

  Returns:
    Resource argument parameter config
  """
  return concepts.ResourceParameterAttributeConfig(
      name='location',
      fallthroughs=[
          deps.Fallthrough(
              function=apphub_utils.DefaultToGlobal,
              hint='Service project attachments only support global location',
          )
      ],
      help_text=help_text if help_text else ('Location of the {resource}.'),
  )


def GetGlobalLocationResourceArg(
    arg_name='location',
    help_text=None,
    positional=False,
    required=False,
):
  """Constructs and returns the Location Resource Argument."""

  help_text = help_text or 'Location'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetGlobalLocationResourceSpec(),
      help_text,
      required=required,
  )


def LocationAttributeConfig():
  return concepts.ResourceParameterAttributeConfig(
      name='location',
      help_text='The Cloud location for the {resource}.',
  )


def GetLocationResourceSpec():
  return concepts.ResourceSpec(
      'apphub.projects.locations',
      resource_name='location',
      locationsId=LocationAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
  )


def GetLocationResourceArg(
    arg_name='location',
    help_text=None,
    positional=False,
    required=True,
):
  """Constructs and returns the Location Resource Argument."""

  help_text = help_text or 'Location'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetLocationResourceSpec(),
      help_text,
      required=required,
  )


def GetServiceProjectResourceSpec(arg_name='service_project', help_text=None):
  """Constructs and returns the Resource specification for Service project."""

  def ServiceProjectAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.serviceProjectAttachments',
      resource_name='ServiceProjectAttachment',
      serviceProjectAttachmentsId=ServiceProjectAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=_DefaultToGlobalLocationAttributeConfig(),
  )


def GetServiceProjectResourceArg(
    arg_name='service_project', help_text=None, positional=True, required=True
):
  """Constructs and returns the Service Project Resource Argument."""

  help_text = help_text or 'Name for the Service Project'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetServiceProjectResourceSpec(),
      help_text,
      required=required,
  )


def ApplicationResourceAttributeConfig(arg_name, help_text):
  """Helper function for constructing ResourceAttributeConfig."""

  return concepts.ResourceParameterAttributeConfig(
      name=arg_name,
      help_text=help_text,
  )


def GetApplicationResourceSpec(arg_name='application', help_text=None):
  """Constructs and returns the Resource specification for Application."""

  return concepts.ResourceSpec(
      'apphub.projects.locations.applications',
      resource_name='application',
      applicationsId=ApplicationResourceAttributeConfig(arg_name, help_text),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
  )


def GetApplicationResourceArg(
    arg_name='application', help_text=None, positional=True, required=True
):
  """Constructs and returns the Application ID Resource Argument."""

  help_text = help_text or 'Id of the Application'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetApplicationResourceSpec(),
      help_text,
      required=required,
  )


def AddDescribeServiceProjectFlags(parser):
  GetServiceProjectResourceArg().AddToParser(parser)


def AddDescribeApplicationFlags(parser):
  GetApplicationResourceArg().AddToParser(parser)


def AddListServiceProjectFlags(parser):
  GetGlobalLocationResourceArg().AddToParser(parser)


def AddListApplicationFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddServiceProjectFlags(parser):
  GetServiceProjectResourceArg().AddToParser(parser)
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def CreateApplicationFlags(parser):
  """Adds flags required to create an application."""

  GetApplicationResourceArg().AddToParser(parser)
  AddAttributesFlags(parser)
  parser.add_argument(
      '--scope-type',
      choices={'REGIONAL': 'Represents a regional application'},
      help='Scope of the Application',
      required=True,
  )
  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the Application')
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def UpdateApplicationFlags(parser):
  """Adds flags required to create an application."""

  GetApplicationResourceArg().AddToParser(parser)
  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the Application')
  parser.add_argument(
      '--criticality',
      type=arg_parsers.ArgDict(
          spec={
              'level': str,
              'mission-critical': bool,
          },
          required_keys=['level', 'mission-critical'],
      ),
      help='Criticality of the Application',
  )
  parser.add_argument('--environment', help='Environment of the Application')
  parser.add_argument(
      '--business-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Business owners of the Application',
  )
  parser.add_argument(
      '--developer-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Developer owners of the Application',
  )
  parser.add_argument(
      '--operator-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Operator owners of the Application',
  )
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddRemoveServiceProjectFlags(parser):
  GetServiceProjectResourceArg().AddToParser(parser)
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def GetDiscoveredServiceResourceSpec(
    arg_name='discovered_service',
    help_text=None
):
  """Constructs and returns the Resource specification for Discovered Service."""

  def DiscoveredServiceAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.discoveredServices',
      resource_name='discoveredService',
      discoveredServicesId=DiscoveredServiceAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
  )


def GetDiscoveredServiceResourceArg(
    arg_name='discovered_service',
    help_text=None,
    positional=True,
    required=True
):
  """Constructs and returns the Discovered Service Resource Argument."""

  help_text = help_text or 'Name for the Discovered Service'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetDiscoveredServiceResourceSpec(),
      help_text,
      required=required,
  )


def GetDiscoveredWorkloadResourceSpec(
    arg_name='discovered_workload', help_text=None
):
  """Constructs and returns the Resource specification for Discovered Workload."""

  def DiscoveredWorkloadAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.discoveredWorkloads',
      resource_name='discoveredWorkload',
      discoveredWorkloadsId=DiscoveredWorkloadAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
  )


def GetDiscoveredWorkloadResourceArg(
    arg_name='discovered_workload',
    help_text=None,
    positional=True,
    required=True,
):
  """Constructs and returns the Discovered Workload Resource Argument."""

  help_text = help_text or 'Name for the Discovered Workload'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetDiscoveredWorkloadResourceSpec(),
      help_text,
      required=required,
  )


def GetApplicationWorkloadResourceSpec(
    arg_name='workload', help_text='Name for the workload'
):
  """Constructs and returns the Resource specification for Application Workload."""

  def ApplicationWorkloadAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.applications.workloads',
      resource_name='workload',
      workloadsId=ApplicationWorkloadAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
      applicationsId=ApplicationResourceAttributeConfig(
          arg_name='application',
          help_text='Name for the application',
      ),
  )


def GetApplicationWorkloadResourceArg(
    arg_name='workload',
    help_text=None,
    positional=True,
    required=True,
):
  """Constructs and returns the application workload Resource Argument."""

  help_text = help_text or 'Name for the workload'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetApplicationWorkloadResourceSpec(),
      help_text,
      required=required,
  )


def GetApplicationServiceResourceSpec(
    arg_name='service', help_text='Name for the service'
):
  """Constructs and returns the Resource specification for Application Service."""

  def ApplicationServiceAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.applications.services',
      resource_name='service',
      servicesId=ApplicationServiceAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
      applicationsId=ApplicationResourceAttributeConfig(
          arg_name='application',
          help_text='Name for the application',
      ),
  )


def GetApplicationServiceResourceArg(
    arg_name='service',
    help_text=None,
    positional=True,
    required=True,
):
  """Constructs and returns the application service Resource Argument."""

  help_text = help_text or 'Name for the service'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetApplicationServiceResourceSpec(),
      help_text,
      required=required,
  )


def AddDescribeDiscoveredServiceFlags(parser):
  GetDiscoveredServiceResourceArg().AddToParser(parser)


def AddListDiscoveredServiceFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddFindUnregisteredServiceFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddDescribeDiscoveredWorkloadFlags(parser):
  GetDiscoveredWorkloadResourceArg().AddToParser(parser)


def AddListDiscoveredWorkloadFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddFindUnregisteredWorkloadFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddDeleteApplicationFlags(parser):
  GetApplicationResourceArg().AddToParser(parser)
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def GetOperationResourceSpec(
    arg_name='operation',
    help_text=None
):
  """Constructs and returns the Resource specification for Operation."""

  def OperationAttributeConfig():
    return concepts.ResourceParameterAttributeConfig(
        name=arg_name,
        help_text=help_text,
    )

  return concepts.ResourceSpec(
      'apphub.projects.locations.operations',
      resource_name='operation',
      operationsId=OperationAttributeConfig(),
      projectsId=concepts.DEFAULT_PROJECT_ATTRIBUTE_CONFIG,
      locationsId=LocationAttributeConfig(),
  )


def GetOperationResourceArg(
    arg_name='operation',
    help_text=None,
    positional=True,
    required=True
):
  """Constructs and returns the Operation Resource Argument."""

  help_text = help_text or 'Name for the Operation'

  return concept_parsers.ConceptParser.ForResource(
      '{}{}'.format('' if positional else '--', arg_name),
      GetOperationResourceSpec(),
      help_text,
      required=required,
  )


def AddDescribeOperationFlags(parser):
  GetOperationResourceArg().AddToParser(parser)


def AddListOperationsFlags(parser):
  GetLocationResourceArg().AddToParser(parser)


def AddListApplicationWorkloadFlags(parser):
  GetApplicationResourceArg(positional=False).AddToParser(parser)


def AddDescribeApplicationWorkloadFlags(parser):
  GetApplicationWorkloadResourceArg().AddToParser(parser)


def AddDeleteApplicationWorkloadFlags(parser):
  GetApplicationWorkloadResourceArg().AddToParser(parser)
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddCreateApplicationWorkloadFlags(parser):
  """Adds flags required to create an application workload."""
  concept_parsers.ConceptParser(
      [
          presentation_specs.ResourcePresentationSpec(
              'WORKLOAD',
              GetApplicationWorkloadResourceSpec(),
              'The Workload resource.',
              flag_name_overrides={
                  'location': '--location',
                  'application': '--application',
              },
              prefixes=True,
              required=True,
          ),
          presentation_specs.ResourcePresentationSpec(
              '--discovered-workload',
              GetDiscoveredWorkloadResourceSpec(),
              'The discovered workload resource.',
              # This hides the location flag for discovered resource.
              flag_name_overrides={
                  'location': '',
                  'project': '',
              },
              prefixes=True,
              required=True,
          ),
      ],
      # This configures the fallthrough from the
      # discovered workload's location to
      # the primary flag for the WORKLOAD's location.
      command_level_fallthroughs={
          '--discovered-workload.location': ['WORKLOAD.location'],
      },
  ).AddToParser(parser)
  AddAttributesFlags(parser, resource_name='workload')

  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the Workload')

  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddUpdateApplicationWorkloadFlags(parser):
  """Adds flags required to update an application workload."""

  GetApplicationWorkloadResourceArg().AddToParser(parser)
  AddAttributesFlags(parser, resource_name='workload')

  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the Workload')

  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddAttributesFlags(parser, resource_name='application'):
  """Adds flags required for attributes fields."""
  parser.add_argument(
      '--criticality',
      type=arg_parsers.ArgDict(
          spec={
              'level': str,
              'mission-critical': bool,
          },
          required_keys=['level', 'mission-critical'],
      ),
      help='Criticality of the {}'.format(resource_name),
  )
  parser.add_argument(
      '--environment', help='Environment of the {}'.format(resource_name)
  )
  parser.add_argument(
      '--business-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Business owners of the {}'.format(resource_name),
  )
  parser.add_argument(
      '--developer-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Developer owners of the {}'.format(resource_name),
  )
  parser.add_argument(
      '--operator-owners',
      type=arg_parsers.ArgDict(
          spec={
              'display-name': str,
              'email': str,
              'channel-uri': str,
          },
          required_keys=['email'],
      ),
      action='append',
      help='Operator owners of the {}'.format(resource_name),
  )


def AddListApplicationServiceFlags(parser):
  GetApplicationResourceArg(positional=False).AddToParser(parser)


def AddDescribeApplicationServiceFlags(parser):
  GetApplicationServiceResourceArg().AddToParser(parser)


def AddDeleteApplicationServiceFlags(parser):
  GetApplicationServiceResourceArg().AddToParser(parser)
  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddCreateApplicationServiceFlags(parser):
  """Adds flags required to create an application service."""
  concept_parsers.ConceptParser(
      [
          presentation_specs.ResourcePresentationSpec(
              'SERVICE',
              GetApplicationServiceResourceSpec(),
              'The Service resource.',
              flag_name_overrides={
                  'location': '--location',
                  'application': '--application',
              },
              prefixes=True,
              required=True,
          ),
          presentation_specs.ResourcePresentationSpec(
              '--discovered-service',
              GetDiscoveredServiceResourceSpec(),
              'The discovered service resource.',
              # This hides the location flag for discovered resource.
              flag_name_overrides={
                  'location': '',
                  'project': '',
              },
              prefixes=True,
              required=True,
          ),
      ],
      # This configures the fallthrough from the
      # discovered service's location to
      # the primary flag for the SERVICE's location.
      command_level_fallthroughs={
          '--discovered-service.location': ['SERVICE.location'],
      },
  ).AddToParser(parser)
  AddAttributesFlags(parser, resource_name='service')

  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the service')

  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )


def AddUpdateApplicationServiceFlags(parser):
  """Adds flags required to update an application service."""

  GetApplicationServiceResourceArg().AddToParser(parser)
  AddAttributesFlags(parser, resource_name='service')

  parser.add_argument('--display-name', help='Human-friendly display name')
  parser.add_argument('--description', help='Description of the service')

  parser.add_argument(
      '--async',
      dest='async_',
      action='store_true',
      default=False,
      help='async operation.',
  )

