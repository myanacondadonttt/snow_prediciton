"""Generated message classes for artifactregistry version v1alpha1.

Store and manage build artifacts in a scalable and integrated service built on
Google infrastructure.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'artifactregistry'


class ArtifactregistryProjectsLocationsGetRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsGetRequest object.

  Fields:
    name: Resource name for the location.
  """

  name = _messages.StringField(1, required=True)


class ArtifactregistryProjectsLocationsListRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsListRequest object.

  Fields:
    filter: A filter to narrow down results to a preferred subset. The
      filtering language accepts strings like `"displayName=tokyo"`, and is
      documented in more detail in [AIP-160](https://google.aip.dev/160).
    name: The resource that owns the locations collection, if applicable.
    pageSize: The maximum number of results to return. If not set, the service
      selects a default.
    pageToken: A page token received from the `next_page_token` field in the
      response. Send that page token to receive the subsequent page.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class ArtifactregistryProjectsLocationsOperationsGetRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class ArtifactregistryProjectsLocationsRepositoriesAptArtifactsImportRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesAptArtifactsImportRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest resource
      to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      imported.
  """

  googleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest', 1)
  parent = _messages.StringField(2, required=True)


class ArtifactregistryProjectsLocationsRepositoriesAptArtifactsUploadRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesAptArtifactsUploadRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest resource
      to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      uploaded.
  """

  googleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest', 1)
  parent = _messages.StringField(2, required=True)


class ArtifactregistryProjectsLocationsRepositoriesCreateRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesCreateRequest object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1Repository: A
      GoogleDevtoolsArtifactregistryV1alpha1Repository resource to be passed
      as the request body.
    parent: Required. The name of the parent resource where the repository
      will be created.
    repositoryId: Required. The repository id to use for this repository.
  """

  googleDevtoolsArtifactregistryV1alpha1Repository = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1Repository', 1)
  parent = _messages.StringField(2, required=True)
  repositoryId = _messages.StringField(3)


class ArtifactregistryProjectsLocationsRepositoriesDeleteRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesDeleteRequest object.

  Fields:
    name: Required. The name of the repository to delete.
  """

  name = _messages.StringField(1, required=True)


class ArtifactregistryProjectsLocationsRepositoriesGetRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesGetRequest object.

  Fields:
    name: Required. The name of the repository to retrieve.
  """

  name = _messages.StringField(1, required=True)


class ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsImportRequest(_messages.Message):
  r"""A
  ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsImportRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsRequest
      resource to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      imported.
  """

  googleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsRequest', 1)
  parent = _messages.StringField(2, required=True)


class ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsUploadRequest(_messages.Message):
  r"""A
  ArtifactregistryProjectsLocationsRepositoriesGoogetArtifactsUploadRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactRequest
      resource to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      uploaded.
  """

  googleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactRequest', 1)
  parent = _messages.StringField(2, required=True)


class ArtifactregistryProjectsLocationsRepositoriesListRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesListRequest object.

  Fields:
    pageSize: The maximum number of repositories to return. Maximum page size
      is 1,000.
    pageToken: The next_page_token value returned from a previous list
      request, if any.
    parent: Required. The name of the parent resource whose repositories will
      be listed.
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  parent = _messages.StringField(3, required=True)


class ArtifactregistryProjectsLocationsRepositoriesPatchRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesPatchRequest object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1Repository: A
      GoogleDevtoolsArtifactregistryV1alpha1Repository resource to be passed
      as the request body.
    name: The name of the repository, for example: "projects/p1/locations/us-
      central1/repositories/repo1".
    updateMask: The update mask applies to the resource. For the `FieldMask`
      definition, see https://developers.google.com/protocol-
      buffers/docs/reference/google.protobuf#fieldmask
  """

  googleDevtoolsArtifactregistryV1alpha1Repository = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1Repository', 1)
  name = _messages.StringField(2, required=True)
  updateMask = _messages.StringField(3)


class ArtifactregistryProjectsLocationsRepositoriesYumArtifactsImportRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesYumArtifactsImportRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest resource
      to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      imported.
  """

  googleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest', 1)
  parent = _messages.StringField(2, required=True)


class ArtifactregistryProjectsLocationsRepositoriesYumArtifactsUploadRequest(_messages.Message):
  r"""A ArtifactregistryProjectsLocationsRepositoriesYumArtifactsUploadRequest
  object.

  Fields:
    googleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest: A
      GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest resource
      to be passed as the request body.
    parent: The name of the parent resource where the artifacts will be
      uploaded.
  """

  googleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest', 1)
  parent = _messages.StringField(2, required=True)


class GoogleDevtoolsArtifactregistryV1alpha1AptArtifact(_messages.Message):
  r"""A detailed representation of an Apt artifact. Information in the record
  is derived from the archive's control file. See
  https://www.debian.org/doc/debian-policy/ch-controlfields.html

  Enums:
    PackageTypeValueValuesEnum: Output only. An artifact is a binary or source
      package.

  Fields:
    architecture: Output only. Operating system architecture of the artifact.
    component: Output only. Repository component of the artifact.
    controlFile: Output only. Contents of the artifact's control metadata
      file.
    name: Output only. The Artifact Registry resource name of the artifact.
    packageName: Output only. The Apt package name of the artifact.
    packageType: Output only. An artifact is a binary or source package.
  """

  class PackageTypeValueValuesEnum(_messages.Enum):
    r"""Output only. An artifact is a binary or source package.

    Values:
      PACKAGE_TYPE_UNSPECIFIED: Package type is not specified.
      BINARY: Binary package.
      SOURCE: Source package.
    """
    PACKAGE_TYPE_UNSPECIFIED = 0
    BINARY = 1
    SOURCE = 2

  architecture = _messages.StringField(1)
  component = _messages.StringField(2)
  controlFile = _messages.BytesField(3)
  name = _messages.StringField(4)
  packageName = _messages.StringField(5)
  packageType = _messages.EnumField('PackageTypeValueValuesEnum', 6)


class GoogleDevtoolsArtifactregistryV1alpha1GoogetArtifact(_messages.Message):
  r"""A detailed representation of a GooGet artifact.

  Fields:
    architecture: Output only. Operating system architecture of the artifact.
    name: Output only. The Artifact Registry resource name of the artifact.
    packageName: Output only. The GooGet package name of the artifact.
  """

  architecture = _messages.StringField(1)
  name = _messages.StringField(2)
  packageName = _messages.StringField(3)


class GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsErrorInfo(_messages.Message):
  r"""Error information explaining why a package was not imported.

  Fields:
    error: The detailed error status.
    gcsSource: Google Cloud Storage location requested.
  """

  error = _messages.MessageField('Status', 1)
  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsGcsSource', 2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsGcsSource(_messages.Message):
  r"""Google Cloud Storage location where the artifacts currently reside.

  Fields:
    uris: Cloud Storage paths URI (e.g., gs://my_bucket//my_object).
    useWildcards: Supports URI wildcards for matching multiple objects from a
      single URI.
  """

  uris = _messages.StringField(1, repeated=True)
  useWildcards = _messages.BooleanField(2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsRequest(_messages.Message):
  r"""The request to import new apt artifacts.

  Fields:
    gcsSource: Google Cloud Storage location where input content is located.
  """

  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsGcsSource', 1)


class GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsResponse(_messages.Message):
  r"""The response message from importing APT artifacts.

  Fields:
    aptArtifacts: The Apt artifacts imported.
    errors: Detailed error info for packages that were not imported.
  """

  aptArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1AptArtifact', 1, repeated=True)
  errors = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportAptArtifactsErrorInfo', 2, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsErrorInfo(_messages.Message):
  r"""Error information explaining why a package was not imported.

  Fields:
    error: The detailed error status.
    gcsSource: Google Cloud Storage location requested.
  """

  error = _messages.MessageField('Status', 1)
  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsGcsSource', 2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsGcsSource(_messages.Message):
  r"""Google Cloud Storage location where the artifacts currently reside.

  Fields:
    uris: Cloud Storage paths URI (e.g., `gs://my_bucket/my_object`).
    useWildcards: Supports URI wildcards for matching multiple objects from a
      single URI.
  """

  uris = _messages.StringField(1, repeated=True)
  useWildcards = _messages.BooleanField(2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsRequest(_messages.Message):
  r"""The request to import new googet artifacts.

  Fields:
    gcsSource: Google Cloud Storage location where input content is located.
  """

  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsGcsSource', 1)


class GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsResponse(_messages.Message):
  r"""The response message from importing artifacts.

  Fields:
    errors: Detailed error info for packages that were not imported.
    googetArtifacts: The GooGet artifacts updated.
  """

  errors = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportGoogetArtifactsErrorInfo', 1, repeated=True)
  googetArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1GoogetArtifact', 2, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsErrorInfo(_messages.Message):
  r"""Error information explaining why a package was not imported.

  Fields:
    error: The detailed error status.
    gcsSource: Google Cloud Storage location requested.
  """

  error = _messages.MessageField('Status', 1)
  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsGcsSource', 2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsGcsSource(_messages.Message):
  r"""Google Cloud Storage location where the artifacts currently reside.

  Fields:
    uris: Cloud Storage paths URI (e.g., gs://my_bucket//my_object).
    useWildcards: Supports URI wildcards for matching multiple objects from a
      single URI.
  """

  uris = _messages.StringField(1, repeated=True)
  useWildcards = _messages.BooleanField(2)


class GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsRequest(_messages.Message):
  r"""The request to import new yum artifacts.

  Fields:
    gcsSource: Google Cloud Storage location where input content is located.
  """

  gcsSource = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsGcsSource', 1)


class GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsResponse(_messages.Message):
  r"""The response message from importing YUM artifacts.

  Fields:
    errors: Detailed error info for packages that were not imported.
    yumArtifacts: The yum artifacts imported.
  """

  errors = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1ImportYumArtifactsErrorInfo', 1, repeated=True)
  yumArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1YumArtifact', 2, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1ListRepositoriesResponse(_messages.Message):
  r"""The response from listing repositories.

  Fields:
    nextPageToken: The token to retrieve the next page of repositories, or
      empty if there are no more repositories to return.
    repositories: The repositories returned.
  """

  nextPageToken = _messages.StringField(1)
  repositories = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1Repository', 2, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1Repository(_messages.Message):
  r"""A Repository for storing artifacts with a specific format.

  Enums:
    FormatValueValuesEnum: Optional. The format of packages that are stored in
      the repository.
    ModeValueValuesEnum: Optional. The mode of the repository.

  Messages:
    LabelsValue: Labels with user-defined metadata. This field may contain up
      to 64 entries. Label keys and values may be no longer than 63
      characters. Label keys must begin with a lowercase letter and may only
      contain lowercase letters, numeric characters, underscores, and dashes.

  Fields:
    createTime: Output only. The time when the repository was created.
    description: The user-provided description of the repository.
    format: Optional. The format of packages that are stored in the
      repository.
    kmsKeyName: The Cloud KMS resource name of the customer managed encryption
      key that's used to encrypt the contents of the Repository. Has the form:
      `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-
      key`. This value may not be changed after the Repository has been
      created.
    labels: Labels with user-defined metadata. This field may contain up to 64
      entries. Label keys and values may be no longer than 63 characters.
      Label keys must begin with a lowercase letter and may only contain
      lowercase letters, numeric characters, underscores, and dashes.
    mode: Optional. The mode of the repository.
    name: The name of the repository, for example: "projects/p1/locations/us-
      central1/repositories/repo1".
    satisfiesPzs: Output only. If set, the repository satisfies physical zone
      separation.
    sizeBytes: Output only. The size, in bytes, of all artifact storage in
      this repository. Repositories that are generally available or in public
      preview use this to calculate storage costs.
    updateTime: Output only. The time when the repository was last updated.
  """

  class FormatValueValuesEnum(_messages.Enum):
    r"""Optional. The format of packages that are stored in the repository.

    Values:
      FORMAT_UNSPECIFIED: Unspecified package format.
      DOCKER: Docker package format.
      MAVEN: Maven package format.
      NPM: NPM package format.
      APT: APT package format.
      YUM: YUM package format.
      GOOGET: GooGet package format.
      PYTHON: Python package format.
    """
    FORMAT_UNSPECIFIED = 0
    DOCKER = 1
    MAVEN = 2
    NPM = 3
    APT = 4
    YUM = 5
    GOOGET = 6
    PYTHON = 7

  class ModeValueValuesEnum(_messages.Enum):
    r"""Optional. The mode of the repository.

    Values:
      MODE_UNSPECIFIED: Unspecified mode.
      STANDARD_REPOSITORY: A standard repository storing artifacts.
      VIRTUAL_REPOSITORY: A virtual repository to serve artifacts from one or
        more sources.
    """
    MODE_UNSPECIFIED = 0
    STANDARD_REPOSITORY = 1
    VIRTUAL_REPOSITORY = 2

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels with user-defined metadata. This field may contain up to 64
    entries. Label keys and values may be no longer than 63 characters. Label
    keys must begin with a lowercase letter and may only contain lowercase
    letters, numeric characters, underscores, and dashes.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = _messages.StringField(1)
  description = _messages.StringField(2)
  format = _messages.EnumField('FormatValueValuesEnum', 3)
  kmsKeyName = _messages.StringField(4)
  labels = _messages.MessageField('LabelsValue', 5)
  mode = _messages.EnumField('ModeValueValuesEnum', 6)
  name = _messages.StringField(7)
  satisfiesPzs = _messages.BooleanField(8)
  sizeBytes = _messages.IntegerField(9)
  updateTime = _messages.StringField(10)


class GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactMediaResponse(_messages.Message):
  r"""The response to upload an artifact.

  Fields:
    operation: Operation to be returned to the user.
  """

  operation = _messages.MessageField('Operation', 1)


class GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactMetadata(_messages.Message):
  r"""The operation metadata for uploading artifacts."""


class GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactRequest(_messages.Message):
  r"""The request to upload an artifact."""


class GoogleDevtoolsArtifactregistryV1alpha1UploadAptArtifactResponse(_messages.Message):
  r"""The response of the completed artifact upload operation. This response
  is contained in the Operation and available to users.

  Fields:
    aptArtifacts: The Apt artifacts updated.
  """

  aptArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1AptArtifact', 1, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactMediaResponse(_messages.Message):
  r"""The response to upload an artifact.

  Fields:
    operation: Operation to be returned to the user.
  """

  operation = _messages.MessageField('Operation', 1)


class GoogleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactRequest(_messages.Message):
  r"""The request to upload an artifact."""


class GoogleDevtoolsArtifactregistryV1alpha1UploadGoogetArtifactResponse(_messages.Message):
  r"""The response of the completed artifact upload operation. This response
  is contained in the Operation and available to users.

  Fields:
    googetArtifacts: The GooGet artifacts updated.
  """

  googetArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1GoogetArtifact', 1, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactMediaResponse(_messages.Message):
  r"""The response to upload an artifact.

  Fields:
    operation: Operation to be returned to the user.
  """

  operation = _messages.MessageField('Operation', 1)


class GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactMetadata(_messages.Message):
  r"""The operation metadata for uploading artifacts."""


class GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactRequest(_messages.Message):
  r"""The request to upload an artifact."""


class GoogleDevtoolsArtifactregistryV1alpha1UploadYumArtifactResponse(_messages.Message):
  r"""The response of the completed artifact upload operation. This response
  is contained in the Operation and available to users.

  Fields:
    yumArtifacts: The Yum artifacts updated.
  """

  yumArtifacts = _messages.MessageField('GoogleDevtoolsArtifactregistryV1alpha1YumArtifact', 1, repeated=True)


class GoogleDevtoolsArtifactregistryV1alpha1YumArtifact(_messages.Message):
  r"""A detailed representation of a Yum artifact.

  Enums:
    PackageTypeValueValuesEnum: Output only. An artifact is a binary or source
      package.

  Fields:
    architecture: Output only. Operating system architecture of the artifact.
    name: Output only. The Artifact Registry resource name of the artifact.
    packageName: Output only. The yum package name of the artifact.
    packageType: Output only. An artifact is a binary or source package.
  """

  class PackageTypeValueValuesEnum(_messages.Enum):
    r"""Output only. An artifact is a binary or source package.

    Values:
      PACKAGE_TYPE_UNSPECIFIED: Package type is not specified.
      BINARY: Binary package (.rpm).
      SOURCE: Source package (.srpm).
    """
    PACKAGE_TYPE_UNSPECIFIED = 0
    BINARY = 1
    SOURCE = 2

  architecture = _messages.StringField(1)
  name = _messages.StringField(2)
  packageName = _messages.StringField(3)
  packageType = _messages.EnumField('PackageTypeValueValuesEnum', 4)


class ListLocationsResponse(_messages.Message):
  r"""The response message for Locations.ListLocations.

  Fields:
    locations: A list of locations that matches the specified filter in the
      request.
    nextPageToken: The standard List next-page token.
  """

  locations = _messages.MessageField('Location', 1, repeated=True)
  nextPageToken = _messages.StringField(2)


class Location(_messages.Message):
  r"""A resource that represents a Google Cloud location.

  Messages:
    LabelsValue: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    MetadataValue: Service-specific metadata. For example the available
      capacity at the given location.

  Fields:
    displayName: The friendly name for this location, typically a nearby city
      name. For example, "Tokyo".
    labels: Cross-service attributes for the location. For example
      {"cloud.googleapis.com/region": "us-east1"}
    locationId: The canonical id for this location. For example: `"us-east1"`.
    metadata: Service-specific metadata. For example the available capacity at
      the given location.
    name: Resource name for the location, which may vary between
      implementations. For example: `"projects/example-project/locations/us-
      east1"`
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Cross-service attributes for the location. For example
    {"cloud.googleapis.com/region": "us-east1"}

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata. For example the available capacity at the
    given location.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  displayName = _messages.StringField(1)
  labels = _messages.MessageField('LabelsValue', 2)
  locationId = _messages.StringField(3)
  metadata = _messages.MessageField('MetadataValue', 4)
  name = _messages.StringField(5)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    ResponseValue: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: Service-specific metadata associated with the operation. It
      typically contains progress information and common metadata such as
      create time. Some services might not provide such metadata. Any method
      that returns a long-running operation should document the metadata type,
      if any.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. If you use the default HTTP mapping,
      the `name` should be a resource name ending with
      `operations/{unique_id}`.
    response: The normal, successful response of the operation. If the
      original method returns no data on success, such as `Delete`, the
      response is `google.protobuf.Empty`. If the original method is standard
      `Get`/`Create`/`Update`, the response should be the resource. For other
      methods, the response should have the type `XxxResponse`, where `Xxx` is
      the original method name. For example, if the original method name is
      `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""Service-specific metadata associated with the operation. It typically
    contains progress information and common metadata such as create time.
    Some services might not provide such metadata. Any method that returns a
    long-running operation should document the metadata type, if any.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""The normal, successful response of the operation. If the original
    method returns no data on success, such as `Delete`, the response is
    `google.protobuf.Empty`. If the original method is standard
    `Get`/`Create`/`Update`, the response should be the resource. For other
    methods, the response should have the type `XxxResponse`, where `Xxx` is
    the original method name. For example, if the original method name is
    `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details. You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details. There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
