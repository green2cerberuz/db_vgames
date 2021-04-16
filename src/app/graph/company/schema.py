import graphene

from app.schemas.company import CompanyOutput

from .mutations import CreateCompany
from .resolvers import resolve_company


class CompanyQuery(graphene.ObjectType):
    """Queries to get all console information."""

    # consoles = graphene.List(graphene.relay.Node.Field(ConsoleNode))
    # consoles = SQLAlchemyConnectionField(ConsoleNode.connection)
    companies = graphene.List(CompanyOutput)

    async def resolve_companies(parent, info, **kwargs):
        """Wrap resolver function."""
        return await resolve_company(parent, info, **kwargs)


class CompanyMutation(graphene.ObjectType):
    """Mutations related to object model."""

    create_company = CreateCompany.Field()
