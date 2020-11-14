# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.association import FranchiseAssociation  # noqa
from app.models.company import Company  # noqa
from app.models.console import Console  # noqa
from app.models.franchise import Franchise  # noqa
from app.models.game import Game  # noqa
