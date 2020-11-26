from datetime import datetime

import graphene

from app.db.async_db import database
from app.models import console
from app.schemas.console import ConsoleInput, ConsoleOutput


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

        query = console.insert().values(**console_details)
        new_console_id = await database.execute(query)
        console_query = console.select().where(console.c.id == new_console_id)

        # Console is a row object that can be accessed by keys
        new_console = await database.fetch_one(console_query)
        return ConsoleOutput(**new_console)
