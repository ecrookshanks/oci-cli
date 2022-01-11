# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import print_function
import click
import oci  # noqa: F401
import six  # noqa: F401
import sys  # noqa: F401
from oci_cli.cli_root import cli
from oci_cli import cli_constants  # noqa: F401
from oci_cli import cli_util
from oci_cli import json_skeleton_utils
from oci_cli import custom_types  # noqa: F401
from oci_cli.aliasing import CommandGroupWithAlias


@cli.command(cli_util.override('usage.usage_root_group.command_name', 'usage'), cls=CommandGroupWithAlias, help=cli_util.override('usage.usage_root_group.help', """A description of the UsageApi API."""), short_help=cli_util.override('usage.usage_root_group.short_help', """UsageApi API"""))
@cli_util.help_option_group
def usage_root_group():
    pass


@click.command(cli_util.override('usage.redeemable_user_group.command_name', 'redeemable-user'), cls=CommandGroupWithAlias, help="""The Email object for redeemable user.""")
@cli_util.help_option_group
def redeemable_user_group():
    pass


@click.command(cli_util.override('usage.redeemable_user_summary_group.command_name', 'redeemable-user-summary'), cls=CommandGroupWithAlias, help="""It provides email Id information.""")
@cli_util.help_option_group
def redeemable_user_summary_group():
    pass


@click.command(cli_util.override('usage.monthly_reward_summary_group.command_name', 'monthly-reward-summary'), cls=CommandGroupWithAlias, help="""Object describing the rewards summary for a month for the requested subscriptionId.""")
@cli_util.help_option_group
def monthly_reward_summary_group():
    pass


@click.command(cli_util.override('usage.product_summary_group.command_name', 'product-summary'), cls=CommandGroupWithAlias, help="""It provides details about a product rewards and usage amount.""")
@cli_util.help_option_group
def product_summary_group():
    pass


usage_root_group.add_command(redeemable_user_group)
usage_root_group.add_command(redeemable_user_summary_group)
usage_root_group.add_command(monthly_reward_summary_group)
usage_root_group.add_command(product_summary_group)


@redeemable_user_group.command(name=cli_util.override('usage.create_redeemable_user.command_name', 'create'), help=u"""Add list of redeemable user email ids for a subscription Id \n[Command Reference](createRedeemableUser)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscriptionId for which rewards information is requested for.""")
@cli_util.option('--items', type=custom_types.CLI_COMPLEX_TYPE, help=u"""The list of email ids to be added to the redeemable users list.

This option is a JSON list with items of type RedeemableUser.  For documentation on RedeemableUser please see our API reference: https://docs.cloud.oracle.com/api/#/en/rewards/20190111/datatypes/RedeemableUser.""" + custom_types.cli_complex_type.COMPLEX_TYPE_HELP)
@cli_util.option('--user-id', help=u"""The user Id of the person whose email we cc""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@json_skeleton_utils.get_cli_json_input_option({'items': {'module': 'usage', 'class': 'list[RedeemableUser]'}})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={'items': {'module': 'usage', 'class': 'list[RedeemableUser]'}}, output_type={'module': 'usage', 'class': 'RedeemableUserCollection'})
@cli_util.wrap_exceptions
def create_redeemable_user(ctx, from_json, tenancy_id, subscription_id, items, user_id, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if user_id is not None:
        kwargs['user_id'] = user_id
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])

    _details = {}

    if items is not None:
        _details['items'] = cli_util.parse_json_parameter("items", items)

    client = cli_util.build_client('usage', 'rewards', ctx)
    result = client.create_redeemable_user(
        tenancy_id=tenancy_id,
        subscription_id=subscription_id,
        create_redeemable_user_details=_details,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@redeemable_user_group.command(name=cli_util.override('usage.delete_redeemable_user.command_name', 'delete'), help=u"""Delete list of redeemable user email ids for a subscription Id \n[Command Reference](deleteRedeemableUser)""")
@cli_util.option('--email-id', required=True, help=u"""The EmailId that needs to be deleted""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscriptionId for which rewards information is requested for.""")
@cli_util.option('--if-match', help=u"""For optimistic concurrency control. In the PUT or DELETE call for a resource, set the `if-match` parameter to the value of the etag from a previous GET or POST response for that resource. The resource will be updated or deleted, only if the etag you provide matches the resource's current etag value.""")
@cli_util.confirm_delete_option
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={})
@cli_util.wrap_exceptions
def delete_redeemable_user(ctx, from_json, email_id, tenancy_id, subscription_id, if_match):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if if_match is not None:
        kwargs['if_match'] = if_match
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage', 'rewards', ctx)
    result = client.delete_redeemable_user(
        email_id=email_id,
        tenancy_id=tenancy_id,
        subscription_id=subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)


@product_summary_group.command(name=cli_util.override('usage.list_products.command_name', 'list-products'), help=u"""This API provides usage period specific product and its usage details. \n[Command Reference](listProducts)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscriptionId for which rewards information is requested for.""")
@cli_util.option('--usage-period-key', required=True, help=u"""The SPM Identifier for the usage period.""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in the paginated response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, can be ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "TIMESTART"]), help=u"""The field to sort by, supports one sort Order.""")
@cli_util.option('--producttype', type=custom_types.CliCaseInsensitiveChoice(["ALL", "ELIGIBLE", "INELIGIBLE"]), help=u"""The field to specify the type of product.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage', 'class': 'ProductCollection'})
@cli_util.wrap_exceptions
def list_products(ctx, from_json, all_pages, page_size, tenancy_id, subscription_id, usage_period_key, page, limit, sort_order, sort_by, producttype):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    if producttype is not None:
        kwargs['producttype'] = producttype
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage', 'rewards', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_products,
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            usage_period_key=usage_period_key,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_products,
            limit,
            page_size,
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            usage_period_key=usage_period_key,
            **kwargs
        )
    else:
        result = client.list_products(
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            usage_period_key=usage_period_key,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@redeemable_user_summary_group.command(name=cli_util.override('usage.list_redeemable_users.command_name', 'list-redeemable-users'), help=u"""Provides emailids of redeemable users for the given subscriptionId \n[Command Reference](listRedeemableUsers)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscriptionId for which rewards information is requested for.""")
@cli_util.option('--page', help=u"""The value of the 'opc-next-page' response header from the previous call.""")
@cli_util.option('--limit', type=click.INT, help=u"""The maximum number of items to return in the paginated response.""")
@cli_util.option('--sort-order', type=custom_types.CliCaseInsensitiveChoice(["ASC", "DESC"]), help=u"""The sort order to use, can be ascending (ASC) or descending (DESC).""")
@cli_util.option('--sort-by', type=custom_types.CliCaseInsensitiveChoice(["TIMECREATED", "TIMESTART"]), help=u"""The field to sort by, supports one sort Order.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results. If you provide this option, then you cannot provide the --limit option.""")
@cli_util.option('--page-size', type=click.INT, help="""When fetching results, the number of results to fetch per call. Only valid when used with --all or --limit, and ignored otherwise.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage', 'class': 'RedeemableUserCollection'})
@cli_util.wrap_exceptions
def list_redeemable_users(ctx, from_json, all_pages, page_size, tenancy_id, subscription_id, page, limit, sort_order, sort_by):

    if all_pages and limit:
        raise click.UsageError('If you provide the --all option you cannot provide the --limit option')

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    if page is not None:
        kwargs['page'] = page
    if limit is not None:
        kwargs['limit'] = limit
    if sort_order is not None:
        kwargs['sort_order'] = sort_order
    if sort_by is not None:
        kwargs['sort_by'] = sort_by
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage', 'rewards', ctx)
    if all_pages:
        if page_size:
            kwargs['limit'] = page_size

        result = cli_util.list_call_get_all_results(
            client.list_redeemable_users,
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            **kwargs
        )
    elif limit is not None:
        result = cli_util.list_call_get_up_to_limit(
            client.list_redeemable_users,
            limit,
            page_size,
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            **kwargs
        )
    else:
        result = client.list_redeemable_users(
            tenancy_id=tenancy_id,
            subscription_id=subscription_id,
            **kwargs
        )
    cli_util.render_response(result, ctx)


@monthly_reward_summary_group.command(name=cli_util.override('usage.list_rewards.command_name', 'list-rewards'), help=u"""This API returns list of rewards for a subscription Id \n[Command Reference](listRewards)""")
@cli_util.option('--tenancy-id', required=True, help=u"""The OCID of the tenancy.""")
@cli_util.option('--subscription-id', required=True, help=u"""The subscriptionId for which rewards information is requested for.""")
@cli_util.option('--all', 'all_pages', is_flag=True, help="""Fetches all pages of results.""")
@json_skeleton_utils.get_cli_json_input_option({})
@cli_util.help_option
@click.pass_context
@json_skeleton_utils.json_skeleton_generation_handler(input_params_to_complex_types={}, output_type={'module': 'usage', 'class': 'RewardCollection'})
@cli_util.wrap_exceptions
def list_rewards(ctx, from_json, all_pages, tenancy_id, subscription_id):

    if isinstance(subscription_id, six.string_types) and len(subscription_id.strip()) == 0:
        raise click.UsageError('Parameter --subscription-id cannot be whitespace or empty string')

    kwargs = {}
    kwargs['opc_request_id'] = cli_util.use_or_generate_request_id(ctx.obj['request_id'])
    client = cli_util.build_client('usage', 'rewards', ctx)
    result = client.list_rewards(
        tenancy_id=tenancy_id,
        subscription_id=subscription_id,
        **kwargs
    )
    cli_util.render_response(result, ctx)