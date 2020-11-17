import graphene


class ConsoleQuery(graphene.ObjectType):
    """Queries to get all console information."""

    say_hello = graphene.String(name=graphene.String(default_value="Test Driven"))

    @staticmethod
    async def resolve_say_hello(parent, info, name):
        """Test resolver function."""
        return f"Hello {name}"


# class ConsoleMutation(graphene.ObjectType):
#     """Mutation related to object model."""

#     pass
