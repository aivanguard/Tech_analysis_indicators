import streamlit as st
import sys

st.write("Financial indicator information")

if len(sys.argv) > 1:
    etf_name = sys.argv[1]
    num_periods = sys.argv[2]
    period = sys.argv[3]
    st.write(f"Hello, {etf_name}!")
else:
    st.write("Not enough ticker info was  provided.")