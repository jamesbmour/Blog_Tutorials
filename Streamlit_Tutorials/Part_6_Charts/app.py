import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Streamlit Part 6: Charts", page_icon="random")

st.write("## Streamlit Part 6: Charts")
# Create tabs for Basic and Advanced Charts
basic_tab, advanced_tab = st.tabs(["Basic Charts", "Advanced Charts"])

################## Basic Charts ##################
with basic_tab:
    st.write("## Basic Charts")
    st.write("### 1. Area Chart")
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

    st.write("### 2. Bar Chart")
    st.bar_chart(area_chart_data)

    st.write("### 3. Line Chart")
    # Create a line chart with the random data
    chart_data = pd.DataFrame(
        {
            "col1": np.random.randn(20),
            "col2": np.random.randn(20),
            "col3": np.random.choice(["A", "B", "C"], 20),
        }
    )

    st.line_chart(chart_data, x="col1", y="col2", color="col3")

    st.write("### 4. Map")
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
    st.write("### 5. Scatter Plot")
    scatter_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=["a", "b", "c"],
    )

    # Create a scatter chart with the random data
    st.scatter_chart(scatter_data)
################## Advanced Charts ##################
with advanced_tab:
    st.write("## Advanced Charts")
    st.write("### 6. Altair Chart")
    import altair as alt

    altair_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    # Create an Altair chart with interactive tooltips
    altair_chart = (
        alt.Chart(altair_data)
        .mark_circle()
        .encode(
            x="a",
            y="b",
            size="a",
            color="c",
            tooltip=["a", "b", "c"],
        )
    )

    # Display the Altair chart in the Streamlit app
    st.altair_chart(altair_chart, use_container_width=True)
    st.write("### 8. Graphviz Chart")
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

    st.write("### 9. Plotly Chart")
    import plotly.figure_factory as ff

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
    st.write("### 10. pydeck Chart")
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
        ],
    )

    # Display the pydeck chart in the Streamlit app
    st.pydeck_chart(pydeck_chart)
    st.write("### 11. pyplot Chart")
    import matplotlib.pyplot as plt

    pyplot_data = np.random.normal(1, 1, size=100)

    # Create a histogram of the data
    fig, ax = plt.subplots()
    ax.hist(pyplot_data, bins=20)  # 20 bins in the histogram

    # Display the histogram in the Streamlit app
    st.pyplot(fig)

    st.write("### 12. Vega Chart")

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
