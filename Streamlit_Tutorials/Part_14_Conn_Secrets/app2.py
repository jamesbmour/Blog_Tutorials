import streamlit as st
import pandas as pd

# import snowflake.connector
from sqlalchemy import text

# Set page title
st.set_page_config(page_title="Streamlit Connections and Secrets Tutorial")

st.title("Streamlit Connections and Secrets Tutorial")

# 1. st.connection (formerly st.experimental_connection)
st.header("1. st.connection")

st.markdown(
    """
`st.connection` is used to create database connections. Let's create a connection to a SQL database:
"""
)

# Example of st.connection with SQLite
if st.button("Connect to SQLite and Run Query"):
    conn = st.connection("sqlite", type="sql", url="sqlite:///example.db")
    df = conn.query("SELECT * FROM users LIMIT 5")
    st.dataframe(df)

# 2. st.connections.SnowflakeConnection (formerly SnowparkConnection)
st.header("2. st.connections.SnowflakeConnection")

st.markdown(
    """
`SnowflakeConnection` is used to connect to Snowflake. Here's how you can use it:
"""
)

if st.button("Connect to Snowflake and Run Query"):
    try:
        # Assuming you have set up your Snowflake credentials in secrets.toml
        conn = st.connection("snowflake")
        df = conn.query("SELECT * FROM my_table LIMIT 5")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error connecting to Snowflake: {str(e)}")

# 3. st.connections.SQLConnection
st.header("3. st.connections.SQLConnection")

st.markdown(
    """
`SQLConnection` provides a way to connect to various SQL databases. Let's use it with SQLite:
"""
)

if st.button("Use SQLConnection"):
    conn = st.connection("sqlite", type="sql", url="sqlite:///example.db")

    # Create a table and insert some data
    conn.session.execute(
        text(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)"
        )
    )
    conn.session.execute(
        text(
            "INSERT INTO products (name, price) VALUES ('Apple', 0.5), ('Banana', 0.3), ('Orange', 0.4)"
        )
    )
    conn.session.commit()

    # Query the database
    df = conn.query("SELECT * FROM products ORDER BY price DESC")
    st.dataframe(df)

    # Use parameters in queries
    price_limit = st.number_input(
        "Enter maximum price", min_value=0.0, value=0.5, step=0.1
    )
    filtered_products = conn.query(
        "SELECT * FROM products WHERE price <= :price", params={"price": price_limit}
    )
    st.dataframe(filtered_products)

# 4. st.secrets
st.header("4. st.secrets")

st.markdown(
    """
`st.secrets` provides a secure way to access sensitive information in your Streamlit app.
Make sure you have set up your secrets in the `.streamlit/secrets.toml` file.
"""
)

if st.button("Access Secrets"):
    try:
        api_key = st.secrets["API_KEY"]
        st.success(f"Successfully accessed API_KEY: {api_key[:5]}...")

        db_username = st.secrets["database"]["username"]
        db_password = st.secrets["database"]["password"]
        st.success(f"Database credentials accessed. Username: {db_username}")
    except KeyError as e:
        st.error(
            f"Error accessing secret: {str(e)}. Make sure it's defined in your secrets.toml file."
        )

# 5. secrets.toml
st.header("5. secrets.toml")

st.markdown(
    """
The `secrets.toml` file is where you store your secrets locally. It should be placed in the `.streamlit` folder 
in your project directory. Here's an example of what it might look like:
"""
)

st.code(
    """
# .streamlit/secrets.toml

API_KEY = "your-api-key-here"

[database]
username = "db-user"
password = "db-password"

[connections.snowflake]
account = "your-account"
user = "sf-user"
password = "sf-password"
warehouse = "compute_wh"
database = "my_db"
schema = "public"
""",
    language="toml",
)

st.markdown(
    """
Remember, never commit your `secrets.toml` file to version control. Add it to your `.gitignore` file to keep your secrets safe.
"""
)

st.header("Conclusion")

st.markdown(
    """
That's it for our tutorial on Streamlit Connections and Secrets! Here's a quick recap:

1. Use `st.connection` to create database connections.
2. `SnowflakeConnection` provides a way to connect to Snowflake databases.
3. `SQLConnection` offers a flexible way to work with various SQL databases.
4. Use `st.secrets` to securely access sensitive information in your app.
5. Store your secrets in the `secrets.toml` file in the `.streamlit` folder.

Remember to always keep your secrets secure and never expose them in your code or version control.
Happy Streamlit coding!
"""
)
