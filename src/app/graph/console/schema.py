import graphene

from app.schemas.console import ConsoleOutput

from .mutations import CreateConsole, DeleteConsole, UpdateConsole
from .resolvers import resolve_console


class ConsoleQuery(graphene.ObjectType):
    """Queries to get all console information."""

    # consoles = graphene.List(graphene.relay.Node.Field(ConsoleNode))
    # consoles = SQLAlchemyConnectionField(ConsoleNode.connection)
    consoles = graphene.List(ConsoleOutput)

    async def resolve_consoles(parent, info, **kwargs):
        """Wrap resolver function."""
        return await resolve_console(parent, info, **kwargs)


class ConsoleMutation(graphene.ObjectType):
    """Mutations related to object model."""

    create_console = CreateConsole.Field()
    update_console = UpdateConsole.Field()
    delete_console = DeleteConsole.Field()
