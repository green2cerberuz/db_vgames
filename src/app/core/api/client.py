import graphene

# from app.graph.console.schema import ConsoleQuery, ConsoleMutation
from app.graph.console.schema import ConsoleQuery


class Query(ConsoleQuery, graphene.ObjectType):
    """All projects queries will be mapped here."""

    pass


# class Mutation(ConsoleMutation, graphene.ObjectType):
#     pass


# client_schema = graphene.Schema(query=Query, mutation=Mutation)
client_schema = graphene.Schema(query=Query)
