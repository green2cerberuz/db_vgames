from .association import FranchiseAssociation
from .company import Company
from .console import Console
from .franchise import Franchise
from .game import Game
from .tag import Tag

# table mappers imports
company = Company.__table__
console = Console.__table__
game = Game.__table__
franchise = Franchise.__table__
tag = Tag.__table__
franchise_association = FranchiseAssociation.__table__
