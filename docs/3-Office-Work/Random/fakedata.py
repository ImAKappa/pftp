"""fakedata

This module generates fake business data and exports to an Excel file
"""
import pandas as pd
from faker import Faker
from pathlib import Path

def fake_businesses(fake: Faker, sample_size: int) -> pd.DataFrame:
    """Generates fake business data"""
    fields = {
        "Business Name": fake.company,
        "Purpose": fake.bs,
        "CEO": fake.name,
        "Tagline": fake.catch_phrase,
        "Address": fake.address,
        "Email": fake.ascii_company_email,
        "Website": fake.domain_name,
        # Add more generators here!
    }
    data = {
        field:[generator() for _ in range(sample_size)]
        for field, generator in fields.items()
    }
    return pd.DataFrame(data)

def main():
    fake = Faker()
    df = fake_businesses(fake, 200)
    print(df)
    file = Path("./business.xlsx")
    df.to_excel(file, index=False, sheet_name="Fake Businesses")
    print()
    print(f"Created '{file.absolute()}'")

if __name__ == "__main__":
    program_name = "Fake Data Generator"
    print(f"{program_name}\n{'-'*len(program_name)}")
    main()
