import numpy as np
import pandas as pd
import streamlit as st
import altair as alt
import graphviz
import plotly.figure_factory as ff
import plotly.express as px
import pydeck as pdk
import matplotlib.pyplot as plt
from vega_datasets import data  # Import sample datasets for Vega

# Optional: Uncomment these lines if you want the app to auto-refresh
# from streamlit_autorefresh import st_autorefresh
# count = st_autorefresh(interval=4000, limit=200, key="refresh_counter")

st.set_page_config(page_title="Streamlit Charts Tutorial", layout="wide")
st.title("## Streamlit Part 6: Charts")

# Create tabs for Basic and Advanced Charts
basic_tab, advanced_tab = st.tabs(["Basic Charts", "Advanced Charts"])

with basic_tab:
    st.header("### Basic Charts")

    # --- Section 1: Area Chart ---
    st.subheader("1. Area Chart")
    # Generate random data for the area chart
    area_chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["col1", "col2", "col3"],
    )

    # Create an area chart using the random data
    st.area_chart(
        area_chart_data,
        x="col1",
        y=["col2", "col3"],
        color=["#FF0000", "#0000FF"],
    )

    # --- Section 2: Bar Chart ---
    st.subheader("2. Bar Chart")
    # Display a bar chart using the same data
    st.bar_chart(area_chart_data)

    # --- Section 3: Line Chart ---
    st.subheader("3. Line Chart")
    # Create a line chart with the random data

    st.line_chart(
        area_chart_data,
        x="col1",
        y="col2",
        color="col3",
    )

    st.markdown("#### 3.1 Basic Line Chart")
    # Note: You can add additional customization or explanations here if needed

    # --- Section 4: Map ---
    st.subheader("4. Map")
    # Create a DataFrame with random latitude and longitude data
    map_data = pd.DataFrame(
        {
            "latitude": np.random.randn(1000) / 50
            + 37.76,  # Latitude values around 37.76
            "longitude": np.random.randn(1000) / 50
            - 122.4,  # Longitude values around -122.4
            "size": np.random.randn(1000) * 100,  # Random size values
            "color": np.random.rand(1000, 4).tolist(),  # Random color values
        }
    )

    # Display the data on a map
    st.map(
        map_data,
        latitude="latitude",
        longitude="longitude",
    )

    # --- Section 5: Scatter Chart ---
    st.subheader("5. Scatter Chart")
    scatter_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"],
    )

    # Create a scatter chart with the random data
    st.scatter_chart(scatter_data)

with advanced_tab:
    st.header("Advanced Charts")

    # --- Section 6: Altair Chart ---
    st.subheader("6. Altair Chart")
    import altair as alt

    altair_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    # Create an Altair chart with interactive tooltips
    altair_chart = (
        alt.Chart(altair_data)
        .mark_circle()
        .encode(
            x="a",
            y="b",
            size="c",
            color="c",
            tooltip=["a", "b", "c"],
        )
    )

    # Display the Altair chart in the Streamlit app
    st.altair_chart(altair_chart, use_container_width=True)

    # --- Section 8: Graphviz Chart ---
    st.subheader("8. Graphviz Chart")
    import graphviz

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
    st.subheader("9. Plotly Chart")
    import plotly.figure_factory as ff
    import plotly.express as px

    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group the data together
    hist_data = [x1, x2, x3]
    group_labels = ["Group 1", "Group 2", "Group 3"]  # Labels for each dataset

    # Create a distribution plot with custom bin sizes
    dist_fig = ff.create_distplot(
        hist_data,
        group_labels,
        bin_size=[0.1, 0.25, 0.5],  # Custom bin sizes for each dataset
    )

    # Display the distribution plot in the Streamlit app
    st.plotly_chart(dist_fig, use_container_width=True)

    gapminder_df = px.data.gapminder()

    # Create a scatter plot for the year 2007
    scatter_fig = px.scatter(
        gapminder_df.query("year == 2007"),
        x="gdpPercap",  # GDP per capita on the x-axis
        y="lifeExp",  # Life expectancy on the y-axis
        size="pop",  # Size of markers based on population
        color="continent",  # Color markers by continent
        hover_name="country",  # Show country name when hovering
        log_x=True,  # Use a logarithmic scale for the x-axis
        size_max=60,  # Maximum size of markers
    )

    st.plotly_chart(scatter_fig, theme=None, use_container_width=True)

    # --- Section 10: pydeck Chart ---
    st.subheader("10. pydeck Chart")
    import pydeck as pdk

    # Generate random latitude and longitude data around a central point
    pydeck_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [39.7392, -104.9903],
        columns=["lat", "lon"],
    )

    # Define the initial view state and layers for the map
    pydeck_chart = pdk.Deck(
        map_style=None,  # Use default map style
        initial_view_state=pdk.ViewState(
            latitude=39.7392,  # Initial latitude
            longitude=-104.9903,  # Initial longitude
            zoom=11,  # Initial zoom level
            pitch=50,  # Tilt angle
        ),
        layers=[
            # Add a hexagon layer to visualize density
            pdk.Layer(
                "HexagonLayer",
                data=pydeck_data,
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
                data=pydeck_data,
                get_position="[lon, lat]",
                get_color="[200, 30, 0, 160]",  # Color of the points
                get_radius=200,  # Radius of the points
            ),
        ],
    )

    # Display the pydeck chart in the Streamlit app
    st.pydeck_chart(pydeck_chart)

    # --- Section 11: pyplot Chart ---
    st.subheader("11. pyplot Chart")
    import matplotlib as plt

    pyplot_data = np.random.normal(1, 1, size=100)

    # Create a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(pyplot_data, bins=20)  # 20 bins in the histogram

    # Display the histogram in the Streamlit app
    st.pyplot(fig)

    # --- Section 12: Vega Chart ---
    st.subheader("12. Vega Chart")

    from vega_datasets import data  # Import sample datasets for Vega

    cars_source = data.cars()

    # Define the Vega-Lite chart specification
    vega_chart_spec = {
        "mark": "point",
        "encoding": {
            "x": {
                "field": "Horsepower",
                "type": "quantitative",
            },
            "y": {
                "field": "Miles_per_Gallon",
                "type": "quantitative",
            },
            "color": {"field": "Origin", "type": "nominal"},  # Color by origin
            "shape": {"field": "Origin", "type": "nominal"},  # Shape by origin
        },
    }

    st.vega_lite_chart(
        cars_source, vega_chart_spec, theme=None, use_container_width=True
    )
