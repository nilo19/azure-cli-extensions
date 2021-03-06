# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource import ProxyResource


class ServerCommunicationLink(ProxyResource):
    """Server communication link.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar state: The state.
    :vartype state: str
    :param partner_server: Required. The name of the partner server.
    :type partner_server: str
    :ivar location: Communication link location.
    :vartype location: str
    :ivar kind: Communication link kind.  This property is used for Azure
     Portal metadata.
    :vartype kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'state': {'readonly': True},
        'partner_server': {'required': True},
        'location': {'readonly': True},
        'kind': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'state': {'key': 'properties.state', 'type': 'str'},
        'partner_server': {'key': 'properties.partnerServer', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ServerCommunicationLink, self).__init__(**kwargs)
        self.state = None
        self.partner_server = kwargs.get('partner_server', None)
        self.location = None
        self.kind = None
