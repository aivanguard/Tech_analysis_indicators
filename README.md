# Tech_analysis_indicators
Quick market TA analysis with 12Data APIs and Streamlit

Step 1: Import the necessary libraries

pandas

twelvedata (This is the 12Data Finance API, it will collect the latest stock market prices and serve as the dataset)

datetime (as well as from datetime import date, timedelta)

plotly

streamlit

Step 2: Obtain an API Key to Collect latest data to acquire the Dataset
Store the API Key in a text file

Use this example
with open('api_key.txt', 'r') as file:
  api_key = file.read().strip()

Step 3: Select your ticker, period (e.g. days), lookback interval (e.g. 200 days)
Run it in Streamlit such as with this example

import streamlit as st
import sys

st.write("Financial indicator information")

if len(sys.argv) > 1:
    etf_name = sys.argv[1]
    num_periods = sys.argv[2]
    period = sys.argv[3]

Test it in the terminal with this example for Arm Holdings for an hourly period over 100 hours
streamlit run ta_input.py 'ARM' 100 '1h'

STep 4:
Create the python code for the dashboards and run it as a Streamlit app

Disclaimer:
Figure out your trading strategy with a multitude of indicators (e.g. volatility, volume, etc)

    st.write(f"Hello, {etf_name}!")
else:
    st.write("Not enough ticker info was  provided.")
