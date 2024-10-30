# app.py

import streamlit as st
import pandas as pd
import os


# Initialize the connection
@st.cache_resource
def get_connection():
    return st.connection("pet_db", type="sql")


conn = get_connection()


# Function to set up the database
def setup_database(connection):
    with connection.session as session:
        session.execute(
            """
          CREATE TABLE IF NOT EXISTS pet_owners (
              person TEXT,
              pet TEXT
          );
      """
        )
        session.execute("DELETE FROM ")  # Clear existing data
        pet_owners = {"Jerry": "Fish", "Barbara": "Cat", "Alex": "Dog"}
        for owner, pet in pet_owners.items():
            session.execute(
                "INSERT INTO ",
                params={"owner": owner, "pet": pet},
            )
        session.commit()


# Setup the database
setup_database(conn)


# Query the data
@st.cache_data(ttl=600)  # Cache for 10 minutes
def fetch_pet_owners(connection):
    return connection.query("SELECT * FROM ")


pet_owners_df = fetch_pet_owners(conn)

# Display the data
st.title("Pet Owners Database")
st.dataframe(pet_owners_df)

# Display secrets (for demonstration purposes only; remove in production)
st.subheader("Accessing Secrets")
st.write("DB Username:", st.secrets.get("db_username", "Not Set"))
