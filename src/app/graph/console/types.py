from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models.console import Console


class ConsoleNode(SQLAlchemyObjectType):
    """Model node to use with graphql api."""

    class Meta:
        model = Console
        interfaces = (relay.Node,)
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)
