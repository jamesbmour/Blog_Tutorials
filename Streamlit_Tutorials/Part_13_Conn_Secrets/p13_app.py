###############################################################################
# SECTION 13: Connections and Secrets
# app.py
###############################################################################
import streamlit as st
import os
from sqlalchemy import text

st.title("Part 13: Connections and Secrets")

st.header("1. Connection and Secret Management")
# Your secrets code remains the same
st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets.db_password)
st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
conn = st.connection("pets_db", type="sql")  # [connection_name.pet_db] in secrets.toml

st.header("2. Data Generation and Insertion")
# Insert some data with conn.session.
with conn.session as s:
    # Wrap SQL statements with text()
    s.execute(text("CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);"))
    s.execute(text("DELETE FROM pet_owners;"))
    pet_owners = {"jerry": "fish", "barbara": "cat", "alex": "puppy"}
    for k in pet_owners:
        s.execute(
            text("INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);"),
            params=dict(owner=k, pet=pet_owners[k]),
        )
    s.commit()

st.header("3. Data Retrieval and Display")
# Query and display the data you inserted
pet_owners = conn.query("select * from pet_owners", ttl=500)
st.dataframe(pet_owners)
