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
"""Exports a Cloud Deploy custom target type resource."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import textwrap

from apitools.base.py import exceptions as apitools_exceptions
from googlecloudsdk.api_lib.clouddeploy import custom_target_type
from googlecloudsdk.calliope import base
from googlecloudsdk.calliope import exceptions
from googlecloudsdk.command_lib.deploy import export_util
from googlecloudsdk.command_lib.deploy import manifest_util
from googlecloudsdk.command_lib.deploy import resource_args
from googlecloudsdk.command_lib.export import util as core_export_util

_DETAILED_HELP = {
    'DESCRIPTION': '{description}',
    'EXAMPLES': textwrap.dedent("""\

      To return the .yaml definition of the custom target type `test-custom-target-type`, in region `us-central1`, run:

        $ {command} test-custom-target-type --region=us-central1

      """),
}


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Export(base.ExportCommand):
  """Returns the .yaml definition of the specified custom target type.

  The exported yaml definition can be applied by `deploy apply` command.
  """

  detailed_help = _DETAILED_HELP

  @staticmethod
  def Args(parser):
    resource_args.AddCustomTargetTypeResourceArg(parser, positional=True)
    core_export_util.AddExportFlags(parser)

  def Run(self, args):
    """Entry point of the export command.

    Args:
      args: argparser.Namespace, an object that contains the values for the
        arguments specified in the .Args() method.
    """
    custom_target_type_ref = args.CONCEPTS.custom_target_type.Parse()
    try:
      resource = custom_target_type.CustomTargetTypesClient().Get(
          custom_target_type_ref.RelativeName()
      )
    except apitools_exceptions.HttpError as error:
      raise exceptions.HttpException(error)

    manifest = manifest_util.ProtoToManifest(
        resource, custom_target_type_ref, manifest_util.CUSTOM_TARGET_TYPE_KIND
    )

    export_util.Export(manifest, args)
