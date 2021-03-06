# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import pecan
from pecan import rest
import six
import wsme
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan

from solum.api.controllers import common_types
from solum.api.controllers.v1 import types as api_types


class Extension(api_types.Base):
    """The Extension resource represents changes that the Provider has added
    onto a Platform in addition to the ones supplied by Solum by default.
    This may include additional protocol semantics, resource types,
    application lifecycle states, resource attributes, etc. Anything may be
    added, as long as it does not contradict the base functionality offered
    by Solum.
    """

    version = wtypes.text
    "Version of the extension."

    documentation = common_types.Uri
    "Documentation URI to the extension."

    @classmethod
    def sample(cls):
        return cls(uri='http://example.com/v1/extensions/mysql',
                   name='mysql',
                   type='extension',
                   tags=['large'],
                   description='A mysql extension',
                   version='2.13',
                   documentation='http://example.com/docs/ext/mysql')


class ExtensionController(rest.RestController):
    """Manages operations on a single extension."""

    def __init__(self, extension_id):
        pecan.request.context['extension_id'] = extension_id
        self._id = extension_id

    @wsme_pecan.wsexpose(Extension, wtypes.text)
    def get(self):
        """Return this extension."""
        error = _("Not implemented")
        pecan.response.translatable_error = error
        raise wsme.exc.ClientSideError(six.text_type(error))


class ExtensionsController(rest.RestController):
    """Manages operations on the extensions collection."""

    @pecan.expose()
    def _lookup(self, extension_id, *remainder):
        if remainder and not remainder[-1]:
            remainder = remainder[:-1]
        return ExtensionController(extension_id), remainder

    @wsme_pecan.wsexpose([Extension])
    def get_all(self):
        """Return all extensions, based on the query provided."""
        return []
