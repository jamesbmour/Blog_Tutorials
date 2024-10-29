###############################################################################
# SECTION 12: Cache
# app.py
###############################################################################
import streamlit as st
import time
import pandas as pd
import numpy as np

st.title("Streamlit Caching and State Tutorial")

###############################################################################
# SECTION 1: CACHING DATA WITH ST.CACHE_DATA
###############################################################################
st.header("1. st.cache_data")
st.write("st.cache_data is used for caching functions that return data.")

###############################################################################
# SECTION 2: RESOURCE CACHING WITH ST.CACHE_RESOURCE
###############################################################################
st.header("2. st.cache_resource")
st.write(
    "st.cache_resource is used for caching global resources like ML models or database connections."
)


###############################################################################
# SECTION 3: CACHE MANAGEMENT
###############################################################################
st.header("3. Clearing Cache")


###############################################################################
# SECTION 4: INTRODUCTION TO SESSION STATE
###############################################################################
st.header("4. Session State")
st.write("Session State allows you to store and persist state for each user session.")

###############################################################################
# SECTION 5: ADVANCED SESSION STATE WITH CALLBACKS
###############################################################################
st.header("5. Callbacks with Session State")


###############################################################################
# SECTION 6: FORMS AND SESSION STATE INTEGRATION
###############################################################################
st.header("6. Forms and Session State")
