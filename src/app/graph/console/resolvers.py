from app.db.async_db import database
from app.models.console import Console
from app.schemas.console import ConsoleOutput


async def resolve_console(self, info, **kwargs):
    """Get all consoles inside database."""
    console = Console.__table__
    query = console.select()
    consoles = await database.fetch_all(query)
    return [ConsoleOutput(**console) for console in consoles]
