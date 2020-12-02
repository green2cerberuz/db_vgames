import graphene

from app.graph.company.schema import CompanyMutation, CompanyQuery
from app.graph.console.schema import ConsoleMutation, ConsoleQuery


class Query(ConsoleQuery, CompanyQuery, graphene.ObjectType):
    """All projects queries will be mapped here."""

    pass


class Mutation(ConsoleMutation, CompanyMutation, graphene.ObjectType):
    """All projects mutations will be mapped here."""

    pass


client_schema = graphene.Schema(query=Query, mutation=Mutation)
# client_schema = graphene.Schema(query=Query)
