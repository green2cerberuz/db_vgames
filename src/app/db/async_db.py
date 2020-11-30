import os

import databases

from app.core.config import settings

# FIXME: Delete after some tests.
if not os.getenv("TEST"):
    database = databases.Database(settings.DATABASE_URI)
else:
    database = databases.Database(os.getenv("TEST_DATABASE_URI"))
