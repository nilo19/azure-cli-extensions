# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional

from azure.core import AsyncPipelineClient
from msrest import Deserializer, Serializer

from ._configuration_async import DataShareManagementClientConfiguration
from .operations_async import AccountOperations
from .operations_async import ConsumerInvitationOperations
from .operations_async import DataSetOperations
from .operations_async import DataSetMappingOperations
from .operations_async import InvitationOperations
from .operations_async import OperationOperations
from .operations_async import ShareOperations
from .operations_async import ProviderShareSubscriptionOperations
from .operations_async import ShareSubscriptionOperations
from .operations_async import ConsumerSourceDataSetOperations
from .operations_async import SynchronizationSettingOperations
from .operations_async import TriggerOperations
from .. import models


class DataShareManagementClient(object):
    """Creates a Microsoft.DataShare management client.

    :ivar account: AccountOperations operations
    :vartype account: data_share_management_client.aio.operations_async.AccountOperations
    :ivar consumer_invitation: ConsumerInvitationOperations operations
    :vartype consumer_invitation: data_share_management_client.aio.operations_async.ConsumerInvitationOperations
    :ivar data_set: DataSetOperations operations
    :vartype data_set: data_share_management_client.aio.operations_async.DataSetOperations
    :ivar data_set_mapping: DataSetMappingOperations operations
    :vartype data_set_mapping: data_share_management_client.aio.operations_async.DataSetMappingOperations
    :ivar invitation: InvitationOperations operations
    :vartype invitation: data_share_management_client.aio.operations_async.InvitationOperations
    :ivar operation: OperationOperations operations
    :vartype operation: data_share_management_client.aio.operations_async.OperationOperations
    :ivar share: ShareOperations operations
    :vartype share: data_share_management_client.aio.operations_async.ShareOperations
    :ivar provider_share_subscription: ProviderShareSubscriptionOperations operations
    :vartype provider_share_subscription: data_share_management_client.aio.operations_async.ProviderShareSubscriptionOperations
    :ivar share_subscription: ShareSubscriptionOperations operations
    :vartype share_subscription: data_share_management_client.aio.operations_async.ShareSubscriptionOperations
    :ivar consumer_source_data_set: ConsumerSourceDataSetOperations operations
    :vartype consumer_source_data_set: data_share_management_client.aio.operations_async.ConsumerSourceDataSetOperations
    :ivar synchronization_setting: SynchronizationSettingOperations operations
    :vartype synchronization_setting: data_share_management_client.aio.operations_async.SynchronizationSettingOperations
    :ivar trigger: TriggerOperations operations
    :vartype trigger: data_share_management_client.aio.operations_async.TriggerOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: azure.core.credentials.TokenCredential
    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential: "TokenCredential",
        subscription_id: str,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = DataShareManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = AsyncPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.account = AccountOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_invitation = ConsumerInvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_set = DataSetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.data_set_mapping = DataSetMappingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitation = InvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share = ShareOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.provider_share_subscription = ProviderShareSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.share_subscription = ShareSubscriptionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.consumer_source_data_set = ConsumerSourceDataSetOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.synchronization_setting = SynchronizationSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.trigger = TriggerOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "DataShareManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
