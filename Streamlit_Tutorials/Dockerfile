import streamlit as st
import pandas as pd

st.title("Streamlit Connections and Secrets Tutorial")

st.header("1. st.connection (formerly st.experimental_connection)")

st.markdown("""
As of Streamlit 1.28.0, `st.experimental_connection` has been deprecated in favor of `st.connection`. 
Let's see how to use the new `st.connection` API:
""")

# Example of st.connection
st.code("""
import streamlit as st

# Create a connection to a SQL database
conn = st.connection("mydb", type="sql")

# Query the database
df = conn.query("SELECT * FROM users LIMIT 5")
st.dataframe(df)
""", language="python")

st.header("2. st.connections.SnowflakeConnection (formerly SnowparkConnection)")

st.markdown("""
The `SnowparkConnection` has been deprecated in favor of `SnowflakeConnection`. 
Here's how you can use the new `SnowflakeConnection`:
""")

st.code("""
import streamlit as st

# Create a connection to Snowflake
conn = st.connection("snowflake")

# Query Snowflake
df = conn.query("SELECT * FROM my_table LIMIT 5")
st.dataframe(df)
""", language="python")

st.header("3. st.connections.SQLConnection")

st.markdown("""
The `SQLConnection` class provides a convenient way to connect to various SQL databases. 
Let's look at an example:
""")

st.code("""
import streamlit as st

# Create a connection to a SQL database
conn = st.connection("sql", type="sql")

# Query the database
df = conn.query("SELECT * FROM products ORDER BY price DESC LIMIT 5")
st.dataframe(df)

# You can also use parameters in your queries
user_id = st.number_input("Enter user ID", min_value=1)
user_orders = conn.query("SELECT * FROM orders WHERE user_id = :user_id", params={"user_id": user_id})
st.dataframe(user_orders)
""", language="python")

st.header("4. st.secrets")

st.markdown("""
`st.secrets` provides a secure way to access sensitive information in your Streamlit app. 
Here's how you can use it:
""")

st.code("""
import streamlit as st

# Access a secret
api_key = st.secrets["API_KEY"]

# Access nested secrets
db_username = st.secrets["database"]["username"]
db_password = st.secrets["database"]["password"]

# Use secrets in your app
st.write(f"Connected to the database as {db_username}")
""", language="python")

st.header("5. secrets.toml")

st.markdown("""
The `secrets.toml` file is where you store your secrets locally. It should be placed in the `.streamlit` folder 
in your project directory. Here's an example of what it might look like:
""")

st.code("""
# .streamlit/secrets.toml

API_KEY = "your-api-key-here"

[database]
username = "db-user"
password = "db-password"

[snowflake]
account = "your-account"
username = "sf-user"
password = "sf-password"
warehouse = "compute_wh"
database = "my_db"
schema = "public"
""", language="toml")

st.markdown("""
Remember, never commit your `secrets.toml` file to version control. Add it to your `.gitignore` file to keep your secrets safe.
""")

st.header("Conclusion")

st.markdown("""
That's it for our tutorial on Streamlit Connections and Secrets! Here's a quick recap:

1. Use `st.connection` to create database connections.
2. `SnowflakeConnection` replaces the deprecated `SnowparkConnection`.
3. `SQLConnection` provides a flexible way to work with SQL databases.
4. Use `st.secrets` to securely access sensitive information in your app.
5. Store your secrets in the `secrets.toml` file in the `.streamlit` folder.

Remember to always keep your secrets secure and never expose them in your code or version control.
Happy Streamlit coding!
""")