import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("result.db")

# Read CSV file
df = pd.read_csv("students.csv")

# Store data into SQL table
df.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

print("CSV data imported into SQL database successfully!")

conn.close()
