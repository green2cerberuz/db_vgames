from datetime import datetime

import graphene
from graphene.types.generic import GenericScalar

from app.db.async_db import database
from app.models import console
from app.schemas.console import ConsoleInput, ConsoleOutput, ConsoleUpdateInput


class CreateConsole(graphene.Mutation):
    """Create a console record."""

    # Investigate more about it.
    Output = ConsoleOutput

    class Arguments:
        console_details = ConsoleInput()

    async def mutate(parent, info, console_details):
        """Create a console object based on input fields."""
        console_details["release_year"] = datetime.strptime(
            console_details["release_year"], "%Y-%m-%d %H:%M:%S"
        )

        async with database.transaction():
            query = console.insert().values(**console_details)
            new_console_id = await database.execute(query)
            console_query = console.select().where(console.c.id == new_console_id)
            # Console is a row object that can be accessed by keys
            new_console = await database.fetch_one(console_query)
            return ConsoleOutput(**new_console)


class UpdateConsole(graphene.Mutation):
    """Update console record."""

    Output = ConsoleOutput

    class Arguments:
        console_details = ConsoleUpdateInput()

    async def mutate(parent, info, console_details):
        """Create a console object based on input fields."""
        if console_details.get("release_year", False):
            console_details["release_year"] = datetime.strptime(
                console_details["release_year"], "%Y-%m-%d %H:%M:%S"
            )

        async with database.transaction():
            console_id = console_details.pop("id")
            query = (
                console.update()
                .values(console_details)
                .where(console.c.id == console_id)
            )

            # Set new values to console
            await database.execute(query)
            updated_query = console.select().where(console.c.id == console_id)
            updated_console = await database.fetch_one(updated_query)
            return ConsoleOutput(**updated_console)


class DeleteConsole(graphene.Mutation):
    """Delete a console."""

    response = GenericScalar()

    class Arguments:
        console_id = graphene.Int()

    async def mutate(parent, info, console_id):
        """Delete a console record with provided ID."""
        # Excute deletion query
        async with database.transaction():
            query = (
                console.delete()
                .where(console.c.id == console_id)
                .returning(console.c.id)
            )
            try:
                record_deleted = await database.execute(query)
            except Exception as e:
                result = {"ok": False, "error": e}
            else:
                if not record_deleted:
                    result = {
                        "ok": False,
                        "error": "Problems deleting a console record",
                    }
                else:
                    result = {"ok": True}
            return DeleteConsole(response=result)
