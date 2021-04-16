from datetime import datetime

import graphene

from app.db.async_db import database
from app.models import company
from app.schemas.company import CompanyInput, CompanyOutput


class CreateCompany(graphene.Mutation):
    """Create a console record."""

    # Investigate more about it.
    Output = CompanyOutput

    class Arguments:
        company_details = CompanyInput()

    async def mutate(parent, info, company_details):
        """Create a console object based on input fields."""
        company_details["creation_year"] = datetime.strptime(
            company_details["creation_year"], "%Y-%m-%d %H:%M:%S"
        )

        async with database.transaction():
            query = company.insert().values(**company_details).return_defaults()
            new_company = await database.execute(query)

            company_query = company.select().where(company.c.id == new_company)
            # Company is a row object that can be accessed by keys
            new_company = await database.fetch_one(company_query)
            return CompanyOutput(**new_company)
