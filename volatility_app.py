# Install the Core Pkgs
import streamlit as st

# Load EDA libraries
import pandas as pd
import numpy as np

# Install Data Viz Pkg
import plotly.express as px

# Load Financial Data & Visualization Pkgs
from twelvedata import TDClient
#Get 12Data API
with open('api_key.txt', 'r') as file:
  api_key = file.read().strip()

# Access the environment variable for the key
# Load Financial Data & Visualization Pkgs
from twelvedata import TDClient
td = TDClient(apikey=api_key)


def volatility_data(ETF,num_periods,period,td):
  df_ts = td.time_series(
    symbol=ETF,
    outputsize=num_periods,
    interval=period,)
  ts_volatile = df_ts.with_bbands().with_atr().with_keltner().as_pandas()
  ts_volatile.to_csv('ts_volatile.csv')



#Define the visualization to plot
  st.title("Plotting price trends w/ tech indicators")
  df = pd.read_csv("ts_volatile.csv")
  #df['datetime'] = df.index
  st.write(df.head(20))

  fig1 = px.line(df,x='datetime',y=['lower_band','close','upper_band'] , title='Bollinger Bands Over Time')
  st.plotly_chart(fig1)

  fig2 = px.line(df,x='datetime',y=['lower_line','close','upper_line'] , title='Keltner Bands Over Time')
  st.plotly_chart(fig2)

  fig3 = px.bar(df,x='datetime',y=['atr'] , title='Avg True Range Over Time')
  st.plotly_chart(fig3)

viz_ETF = 'ARM'
num_periods = 100
period = '1h'

if __name__ == '__main__':
  volatility_data(viz_ETF,num_periods,period,td)