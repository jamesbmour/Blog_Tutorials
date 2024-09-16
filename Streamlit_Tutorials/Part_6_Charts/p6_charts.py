import numpy as np
import pandas as pd
import streamlit as st

# Optional: Uncomment these lines if you want the app to auto-refresh
# from streamlit_autorefresh import st_autorefresh
# count = st_autorefresh(interval=4000, limit=200, key="refresh_counter")

# Title of the Streamlit app
st.write("## Streamlit Part 6: Charts")

# --- Section 1: Area Chart ---
st.write("### 1. Area Chart")
# Generate random data for the area chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20 rows of random numbers with 3 columns
    columns=["col1", "col2", "col3"],  # Name the columns
)

# Create an area chart using the random data
st.area_chart(
    chart_data,
    x="col1",  # Set 'col1' as the x-axis
    y=["col2", "col3"],  # Plot 'col2' and 'col3' as the y-axis
    color=["#FF0000", "#0000FF"],  # Optional: Set custom colors for the areas
)

# --- Section 2: Bar Chart ---
st.write("### 2. Bar Chart")
# Display a bar chart using the same data
st.bar_chart(chart_data)

# --- Section 3: Line Chart ---
st.write("### 3. Line Chart")
# Create a line chart with the random data
st.line_chart(
    chart_data,
    x="col1",  # Set 'col1' as the x-axis
    y="col2",  # Plot 'col2' as the y-axis
    color="col3",  # Optional: Color lines based on 'col3'
)

st.write("#### 3.1 Basic Line Chart")
# Note: The subheader is added but no additional code is provided

# --- Section 4: Map ---
st.write("### 4. Map")
# Create a DataFrame with random latitude and longitude data
df = pd.DataFrame(
    {
        "col1": np.random.randn(1000) / 50 + 37.76,  # Latitude values around 37.76
        "col2": np.random.randn(1000) / 50 + -122.4,  # Longitude values around -122.4
        "col3": np.random.randn(1000) * 100,  # Random size values
        "col4": np.random.rand(1000, 4).tolist(),  # Random color values
    }
)

# Display the data on a map
st.map(
    df,
    latitude="col1",
    longitude="col2",
    size="col3",  # Optional: Set the size of the markers
    color="col4",  # Optional: Set the color of the markers
)

# --- Section 5: Scatter Chart ---
st.write("### 5. Scatter Chat")
# Generate random data for the scatter chart
scatter_data = pd.DataFrame(
    np.random.randn(20, 3),  # 20 rows, 3 columns
    columns=["a", "b", "c"],  # Name the columns
)

# Create a scatter chart with the random data
st.scatter_chart(scatter_data)

# --- Advanced Charts Section ---
st.write("## Advanced Charts")

# --- Section 6: Altair Chart ---
st.write("### 6. Altair Chart")
import altair as alt  # Import Altair for advanced charting

# Generate random data for the Altair chart
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# Create an Altair chart with interactive tooltips
c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a",  # X-axis data
        y="b",  # Y-axis data
        size="c",  # Size of the markers
        color="c",  # Color of the markers
        tooltip=["a", "b", "c"],  # Display data values on hover
    )
)

# Display the Altair chart in the Streamlit app
st.altair_chart(c, use_container_width=True)

# --- Section 8: Graphviz Chart ---
st.write("### 8. Graphviz Chart")
import graphviz  # Import Graphviz for creating graph diagrams

# Create a Graphviz directed graph
graph = graphviz.Digraph()

graph.edge("Planning", "Development")
graph.edge("Development", "Testing")
graph.edge("Testing", "Deployment")
graph.edge("Requirements Gathering", "Planning")
graph.edge("Design", "Planning")
graph.edge("Coding", "Development")
graph.edge("Code Review", "Development")
graph.edge("Unit Testing", "Testing")
graph.edge("Integration Testing", "Testing")
graph.edge("Staging", "Deployment")
graph.edge("Production", "Deployment")

# Display the graph in the Streamlit app
st.graphviz_chart(graph)

# --- Section 9: Plotly Chart ---
st.write("### 9. Plotly Chart")
import plotly.figure_factory as ff  # Import Plotly's figure factory
import plotly.express as px  # Import Plotly Express for easy plotting

# Generate random data for histograms
x1 = np.random.randn(200) - 2  # Dataset 1
x2 = np.random.randn(200)  # Dataset 2
x3 = np.random.randn(200) + 2  # Dataset 3

# Group the data together
hist_data = [x1, x2, x3]
group_labels = ["Group 1", "Group 2", "Group 3"]  # Labels for each dataset

# Create a distribution plot with custom bin sizes
fig = ff.create_distplot(
    hist_data,
    group_labels,
    bin_size=[0.1, 0.25, 0.5],  # Custom bin sizes for each dataset
)

# Display the distribution plot in the Streamlit app
st.plotly_chart(fig, use_container_width=True)

# Load the Gapminder dataset
df = px.data.gapminder()

# Create a scatter plot for the year 2007
fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",  # GDP per capita on the x-axis
    y="lifeExp",  # Life expectancy on the y-axis
    size="pop",  # Size of markers based on population
    color="continent",  # Color markers by continent
    hover_name="country",  # Show country name when hovering
    log_x=True,  # Use a logarithmic scale for the x-axis
    size_max=60,  # Maximum size of markers
)

# Create tabs to compare different themes
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Display the chart using the Streamlit theme
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Display the chart using Plotly's native theme
    st.plotly_chart(fig, theme=None, use_container_width=True)

# --- Additional Plotly Chart with Custom Colorscale ---
import plotly.express as px  # Already imported, but included for clarity

st.subheader("Define a custom colorscale")
# Load the Iris dataset
df = px.data.iris()

# Create a scatter plot with a custom colorscale
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",  # Use the 'reds' colorscale
)

# Create tabs to compare different themes
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    st.plotly_chart(fig, theme=None, use_container_width=True)

# --- Section 10: pydeck Chart ---
st.write("### 10. pydeck Chart")
import pydeck as pdk  # Import pydeck for advanced mapping

# Generate random latitude and longitude data around a central point
chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"],
)

# Define the initial view state and layers for the map
st.pydeck_chart(
    pdk.Deck(
        map_style=None,  # Use default map style
        initial_view_state=pdk.ViewState(
            latitude=37.76,  # Initial latitude
            longitude=-122.4,  # Initial longitude
            zoom=11,  # Initial zoom level
            pitch=50,  # Tilt angle
        ),
        layers=[
            # Add a hexagon layer to visualize density
            pdk.Layer(
                "HexagonLayer",
                data=chart_data,
                get_position="[lon, lat]",
                radius=200,  # Radius of each hexagon bin
                elevation_scale=4,  # Elevation scale factor
                elevation_range=[0, 1000],  # Elevation range
                pickable=True,
                extruded=True,  # Display as 3D
            ),
            # Add a scatterplot layer on top
            pdk.Layer(
                "ScatterplotLayer",
                data=chart_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",  # Color of the points
                get_radius=200,  # Radius of the points
            ),
        ],
    )
)

# --- Section 11: pyplot Chart ---
st.write("### 11. pyplot Chart")
import matplotlib.pyplot as plt  # Import matplotlib for plotting

# Generate random data from a normal distribution
arr = np.random.normal(1, 1, size=100)

# Create a histogram of the data
fig, ax = plt.subplots()
ax.hist(arr, bins=20)  # 20 bins in the histogram

# Display the histogram in the Streamlit app
st.pyplot(fig)

# --- Section 12: Vega Chart ---
st.write("### 12. Vega Chart")
from vega_datasets import data  # Import sample datasets for Vega

# Load the cars dataset
source = data.cars()

# Define the Vega-Lite chart specification
chart = {
    "mark": "point",  # Use point marks
    "encoding": {
        "x": {
            "field": "Horsepower",
            "type": "quantitative",  # Numeric data
        },
        "y": {
            "field": "Miles_per_Gallon",
            "type": "quantitative",
        },
        "color": {"field": "Origin", "type": "nominal"},  # Color by origin
        "shape": {"field": "Origin", "type": "nominal"},  # Shape by origin
    },
}

# Create tabs to compare different themes
tab1, tab2 = st.tabs(["Streamlit theme (default)", "Vega-Lite native theme"])

with tab1:
    # Display the chart using the Streamlit theme
    st.vega_lite_chart(source, chart, theme="streamlit", use_container_width=True)
with tab2:
    # Display the chart using Vega-Lite's native theme
    st.vega_lite_chart(source, chart, theme=None, use_container_width=True)
