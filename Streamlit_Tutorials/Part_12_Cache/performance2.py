import streamlit as st
import pandas as pd
import numpy as np
import time
import threading
from transformers import pipeline
import requests

st.title("Streamlit Caching Examples")

# Sidebar for navigation
example = st.selectbox(
    "Select an example to run:",
    [
        "Basic Usage of st.cache_data",
        "Basic Usage of st.cache_resource",
        "Controlling Cache Size and Duration",
        "Customizing the Spinner",
        "Excluding Input Parameters from Hashing",
        "Using hash_funcs for Custom Objects",
        "Avoid Mutating Cached Data",
        "Ensuring Thread Safety with st.cache_resource",
        "Widgets Inside Cached Functions",
        "Dealing with Large Data",
        "Mutation and Concurrency Issues",
        "Migrating from st.cache",
    ],
)

# 1. Basic Usage of st.cache_data
if example == "Basic Usage of st.cache_data":
    st.header("Basic Usage of st.cache_data")

    @st.cache_data
    def load_data(url):
        df = pd.read_csv(url)
        return df

    data_url = (
        "https://raw.githubusercontent.com/plotly/datasets/master/uber-rides-data1.csv"
    )
    df = load_data(data_url)

    st.subheader("Uber Rides Data")
    st.dataframe(df)

    if st.button("Re-run"):
        st.experimental_rerun()

# 2. Basic Usage of st.cache_resource
elif example == "Basic Usage of st.cache_resource":
    st.header("Basic Usage of st.cache_resource")

    @st.cache_resource
    def load_model():
        return pipeline("sentiment-analysis")

    model = load_model()

    st.subheader("Sentiment Analysis App")

    user_input = st.text_input("Enter text for sentiment analysis:")

    if user_input:
        result = model(user_input)[0]
        label = result["label"]
        score = result["score"]
        st.write(f"**Label**: {label}")
        st.write(f"**Score**: {score:.4f}")

# 3. Controlling Cache Size and Duration
elif example == "Controlling Cache Size and Duration":
    st.header("Controlling Cache Size and Duration")

    @st.cache_data(ttl=3600, max_entries=100)
    def fetch_data(api_endpoint):
        response = requests.get(api_endpoint)
        return response.json()

    api_endpoint = "https://jsonplaceholder.typicode.com/posts"
    data = fetch_data(api_endpoint)

    st.subheader("API Data Fetching with Caching")
    st.write(data)

# 4. Customizing the Spinner
elif example == "Customizing the Spinner":
    st.header("Customizing the Spinner")

    spinner_option = st.selectbox(
        "Choose Spinner Option:", ["Disable Spinner", "Custom Spinner Message"]
    )

    if spinner_option == "Disable Spinner":

        @st.cache_data(show_spinner=False)
        def compute_heavy_task():
            time.sleep(5)  # Simulate a heavy computation
            return "Task Completed"

        st.subheader("Spinner Disabled")
        result = compute_heavy_task()
        st.write(result)
    else:

        @st.cache_data(show_spinner="Processing data, please wait...")
        def compute_heavy_task():
            time.sleep(5)  # Simulate a heavy computation
            return "Task Completed"

        st.subheader("Custom Spinner Message")
        result = compute_heavy_task()
        st.write(result)

# 5. Excluding Input Parameters from Hashing
elif example == "Excluding Input Parameters from Hashing":
    st.header("Excluding Input Parameters from Hashing")

    # Mock database connection class
    class DatabaseConnection:
        def execute(self, query):
            return f"Results for query: {query}"

    @st.cache_data
    def query_database(_db_connection, query):
        return _db_connection.execute(query)

    def establish_connection():
        return DatabaseConnection()

    db_connection = establish_connection()
    query = st.text_input("Enter your SQL query:", "SELECT * FROM users")

    st.subheader("Database Query with Caching")
    results = query_database(db_connection, query)
    st.write(results)

# 6. Using hash_funcs for Custom Objects
elif example == "Using hash_funcs for Custom Objects":
    st.header("Using hash_funcs for Custom Objects")

    class CustomObject:
        def __init__(self, data):
            self.data = data

    def custom_object_hasher(obj):
        return hash(obj.data)

    @st.cache_data(hash_funcs={CustomObject: custom_object_hasher})
    def process_custom_object(obj):
        return obj.data * 2

    st.subheader("Custom Object Caching with hash_funcs")

    data_input = st.number_input("Enter a number:", value=10)
    my_obj = CustomObject(data=data_input)
    result = process_custom_object(my_obj)
    st.write(f"The result is: {result}")

# 7. Avoid Mutating Cached Data
elif example == "Avoid Mutating Cached Data":
    st.header("Avoid Mutating Cached Data")

    @st.cache_data
    def create_list():
        return [1, 2, 3]

    my_list = create_list()
    st.write("Initial list:", my_list)

    if st.button("Mutate List"):
        my_list.append(4)
        st.write("Mutated list:", my_list)
    else:
        st.write("List not mutated.")

# 8. Ensuring Thread Safety with st.cache_resource
elif example == "Ensuring Thread Safety with st.cache_resource":
    st.header("Ensuring Thread Safety with st.cache_resource")

    class Counter:
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()

        def increment(self):
            with self.lock:
                self.count += 1
                return self.count

    @st.cache_resource
    def get_counter():
        return Counter()

    counter = get_counter()

    st.subheader("Thread-Safe Counter")

    if st.button("Increment Counter"):
        new_value = counter.increment()
        st.write(f"Counter Value: {new_value}")
    else:
        st.write(f"Counter Value: {counter.count}")

# 9. Widgets Inside Cached Functions
elif example == "Widgets Inside Cached Functions":
    st.header("Widgets Inside Cached Functions")

    @st.cache_data(experimental_allow_widgets=True)
    def cached_function():
        st.write("This is a static element inside a cached function.")
        return "Cached Result"

    st.subheader("Widgets Inside Cached Functions")
    result = cached_function()
    st.write(result)

# 10. Dealing with Large Data
elif example == "Dealing with Large Data":
    st.header("Dealing with Large Data")

    @st.cache_resource
    def generate_large_dataframe(num_rows):
        df = pd.DataFrame(
            {
                "A": np.random.rand(num_rows),
                "B": np.random.rand(num_rows),
                "C": np.random.rand(num_rows),
                "D": np.random.rand(num_rows),
            }
        )
        return df

    st.subheader("Large Data Handling with st.cache_resource")

    num_rows = st.number_input(
        "Number of Rows:", min_value=1_000_000, value=10_000_000, step=1_000_000
    )

    df = generate_large_dataframe(int(num_rows))

    st.write(df)

# 11. Mutation and Concurrency Issues
elif example == "Mutation and Concurrency Issues":
    st.header("Mutation and Concurrency Issues")

    @st.cache_resource
    def create_shared_list():
        return [0]

    shared_list = create_shared_list()

    if st.button("Increment Shared Counter"):
        shared_list[0] += 1

    st.write(f"Shared Counter Value: {shared_list[0]}")

# 12. Migrating from st.cache
elif example == "Migrating from st.cache":
    st.header("Migrating from st.cache")

    st.subheader("Original Code with st.cache")
    st.code(
        """
import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_data():
    return pd.read_csv('data.csv')

data = load_data()
st.write(data)
    """,
        language="python",
    )

    st.subheader("Updated Code with st.cache_data")
    st.code(
        """
import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

data = load_data()
st.write(data)
    """,
        language="python",
    )

    st.write("Since we don't have 'data.csv', we'll use a sample DataFrame.")

    @st.cache_data
    def load_sample_data():
        data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        return data

    data = load_sample_data()
    st.write(data)

else:
    st.write("Please select an example from the sidebar.")
