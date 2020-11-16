import databases

from app.core.config import settings

database = databases.Database(settings.DATABASE_URI)
