# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_healthcareapis.generated._client_factory import cf_service
    healthcareapis_service = CliCommandType(
        operations_tmpl='azext_healthcareapis.vendored_sdks.healthcareapis.operations._service_operations#ServiceOperat'
        'ions.{}',
        client_factory=cf_service)
    with self.command_group('healthcareapis service', healthcareapis_service, client_factory=cf_service,
                            is_experimental=True) as g:
        g.custom_command('list', 'healthcareapis_service_list')
        g.custom_show_command('show', 'healthcareapis_service_show')
        g.custom_command('create', 'healthcareapis_service_create', supports_no_wait=True)
        g.custom_command('update', 'healthcareapis_service_update', supports_no_wait=True)
        g.custom_command('delete', 'healthcareapis_service_delete', supports_no_wait=True, confirmation=True)
        g.custom_wait_command('wait', 'healthcareapis_service_show')

    from azext_healthcareapis.generated._client_factory import cf_operation_result
    healthcareapis_operation_result = CliCommandType(
        operations_tmpl='azext_healthcareapis.vendored_sdks.healthcareapis.operations._operation_result_operations#Oper'
        'ationResultOperations.{}',
        client_factory=cf_operation_result)
    with self.command_group('healthcareapis operation-result', healthcareapis_operation_result,
                            client_factory=cf_operation_result, is_experimental=True) as g:
        g.custom_show_command('show', 'healthcareapis_operation_result_show')

    from azext_healthcareapis.generated._client_factory import cf_private_endpoint_connection
    healthcareapis_private_endpoint_connection = CliCommandType(
        operations_tmpl='azext_healthcareapis.vendored_sdks.healthcareapis.operations._private_endpoint_connection_oper'
        'ations#PrivateEndpointConnectionOperations.{}',
        client_factory=cf_private_endpoint_connection)
    with self.command_group('healthcareapis private-endpoint-connection', healthcareapis_private_endpoint_connection,
                            client_factory=cf_private_endpoint_connection, is_experimental=True) as g:
        g.custom_command('list', 'healthcareapis_private_endpoint_connection_list')
        g.custom_show_command('show', 'healthcareapis_private_endpoint_connection_show')
        g.custom_command('create', 'healthcareapis_private_endpoint_connection_create', supports_no_wait=True)
        g.custom_command('update', 'healthcareapis_private_endpoint_connection_update', supports_no_wait=True)
        g.custom_command('delete', 'healthcareapis_private_endpoint_connection_delete', supports_no_wait=True,
                         confirmation=True)
        g.custom_wait_command('wait', 'healthcareapis_private_endpoint_connection_show')

    from azext_healthcareapis.generated._client_factory import cf_private_link_resource
    healthcareapis_private_link_resource = CliCommandType(
        operations_tmpl='azext_healthcareapis.vendored_sdks.healthcareapis.operations._private_link_resource_operations'
        '#PrivateLinkResourceOperations.{}',
        client_factory=cf_private_link_resource)
    with self.command_group('healthcareapis private-link-resource', healthcareapis_private_link_resource,
                            client_factory=cf_private_link_resource, is_experimental=True) as g:
        g.custom_command('list', 'healthcareapis_private_link_resource_list')
        g.custom_show_command('show', 'healthcareapis_private_link_resource_show')
