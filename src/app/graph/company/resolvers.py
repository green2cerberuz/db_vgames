from app.db.async_db import database
from app.models.company import Company
from app.schemas.company import CompanyOutput


async def resolve_company(self, info, **kwargs):
    """Get all companies inside database."""
    company = Company.__table__
    query = company.select()
    companies = await database.fetch_all(query)
    return [CompanyOutput(**company) for company in companies]
