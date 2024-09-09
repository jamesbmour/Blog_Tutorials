import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["col1", "col2", "col3"]
)

st.area_chart(
    chart_data,
    x="col1",
    y=["col2", "col3"],
    color=["#FF0000", "#0000FF"],  # Optional
)