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
"""Command to list unregistered workloads in the Project/Location."""
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.apphub import discovered_workloads as apis
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.apphub import flags


_DETAILED_HELP = {
    'DESCRIPTION': '{description}',
    'EXAMPLES': """ \
        To list all unregistered workloads, run:

          $ {command}
        """,
}

_FORMAT = """
  table(
    name.scope("discoveredWorkloads"):label=NAME,
    name.scope("projects").segment(1):label=PROJECT,
    name.scope("locations").segment(0):label=LOCATION,
    workloadReference,
    workloadProperties
  )
"""


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class FindUnregistered(base.ListCommand):
  """List Unregistered Discovered Workloads."""

  detailed_help = _DETAILED_HELP

  @staticmethod
  def Args(parser):
    flags.AddFindUnregisteredWorkloadFlags(parser)
    parser.display_info.AddFormat(_FORMAT)

  def Run(self, args):
    """Run the find unregistered workload command."""
    client = apis.DiscoveredWorkloadsClient()
    location_ref = args.CONCEPTS.location.Parse()
    return client.FindUnregistered(
        limit=args.limit,
        page_size=args.page_size,
        parent=location_ref.RelativeName(),
    )
