import streamlit as st
import sqlite3
import os
from faker import Faker

# Everything is accessible via the st.secrets dict:
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)

# 1. Connections
st.header("1. Connections")

# Connect to the SQLite database
# conn = sqlite3.connect("pets_db.sqlite")
# conn = sqlite3.connect("pets_db.sqlite")
conn = st.connection("pets_db", type='sql')

with conn.session as s:
    s.execute("DROP TABLE IF EXISTS pets")

c = conn.cursor()
# drop table if exists
c.execute("DROP TABLE IF EXISTS pets")
c.execute("DROP TABLE IF EXISTS pets")
# Create table
c.execute(
    """
    CREATE TABLE IF NOT EXISTS pets
    (name TEXT, age INTEGER)
    """
)

# Initialize Faker
fake = Faker()

# Generate and insert random data
for _ in range(7):
    # Generate random pet name (using first_name as pet name)
    pet_name = fake.first_name()
    # Generate random age between 1 and 15
    pet_age = fake.random_int(min=1, max=15)

    # Insert data
    c.execute("INSERT INTO pets (name, age) VALUES (?, ?)", (pet_name, pet_age))

# Commit changes
conn.commit()

# Query data
c.execute("SELECT * FROM pets")
data = c.fetchall()

# Display data
st.write("Data in SQLite database:")
st.write("Table: pets")
st.table(data)

st.write("json data:")
st.write(data)

# Close connection
conn.close()

# Created/Modified files during execution:
print("pets_db.sqlite")
