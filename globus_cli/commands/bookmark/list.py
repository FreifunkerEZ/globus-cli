import click

from globus_cli.parsing import common_options
from globus_cli.safeio import formatted_print

from globus_cli.services.transfer import (
    iterable_response_to_dict, get_client, display_name_or_cname)


@click.command('list', help='List bookmarks for the current user')
@common_options
def bookmark_list():
    """
    Executor for `globus bookmark list`
    """
    client = get_client()

    bookmark_iterator = client.bookmark_list()

    def get_ep_name(item):
        ep_id = item['endpoint_id']
        ep_doc = client.get_endpoint(ep_id)
        return display_name_or_cname(ep_doc)

    formatted_print(
        bookmark_iterator,
        fields=[('Name', 'name'), ('Bookmark ID', 'id'),
                ('Endpoint ID', 'endpoint_id'), ('Endpoint Name', get_ep_name),
                ('Path', 'path')],
        response_key='DATA', json_converter=iterable_response_to_dict)
