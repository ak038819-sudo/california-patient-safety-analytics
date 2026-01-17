import pandas as pd
import mysql.connector
import numpy as np

CSV_PATH = r"C:\Users\Owner\Downloads\ca-oshpd-adveventhospitalizationspsi-county2005-2015q3.csv"

df = pd.read_csv(CSV_PATH)

# Column and data schema
df.columns = [
    "year",
    "county",
    "psi_code",
    "psi_description",
    "event_count",
    "population",
    "obs_rate"
]

# Strip whitespace and remove commas
df["county"] = df["county"].astype(str).str.strip()
df["psi_code"] = df["psi_code"].astype(str).str.strip()
df["psi_description"] = df["psi_description"].astype(str).str.strip()

for col in ["event_count", "population", "obs_rate", "year"]:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .str.strip()
        .replace({"": np.nan, "NA": np.nan, "N/A": np.nan, "nan": np.nan})
    )

df["year"] = pd.to_numeric(df["year"], errors="coerce").astype("Int64")
df["event_count"] = pd.to_numeric(df["event_count"], errors="coerce").astype("Int64")
df["population"] = pd.to_numeric(df["population"], errors="coerce").astype("Int64")
df["obs_rate"] = pd.to_numeric(df["obs_rate"], errors="coerce")

# conver Pandas to Python
df = df.where(pd.notnull(df), None)

# My SQL translaion layer
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="C@shieP0047",
    database="healthcare_analytics"
)
cursor = conn.cursor()

insert_query = """
INSERT INTO fact_patient_safety
(year, county, psi_code, psi_description, event_count, population, obs_rate)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

cursor.executemany(insert_query, df.values.tolist())
conn.commit()

cursor.close()
conn.close()

print(f"Successfully ingested {len(df)} records.")
