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
"""The main command group for Backup and DR."""
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.GA, base.ReleaseTrack.BETA)
class Backupdr(base.Group):
  """Backup and DR command group."""

  # See third_party/py/googlecloudsdk/calliope/base.py for a list of categories.
  category = base.STORAGE_CATEGORY

  def Filter(self, context, args):
    # restricts users to pass in project id only, need to check whether
    # its okay to pass in project number
    base.RequireProjectID(args)
    del context, args


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class BackupdrAlpha(base.Group):
  """Backup and DR command group."""

  # See third_party/py/googlecloudsdk/calliope/base.py for a list of categories.
  category = base.STORAGE_CATEGORY

  def Filter(self, context, args):
    # restricts users to pass in project id only, need to check whether
    # its okay to pass in project number
    base.RequireProjectID(args)
    del context, args
