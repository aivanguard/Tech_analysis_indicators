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


def trend_data(ETF,num_periods,period,td):
  df_ts = td.time_series(
    symbol=ETF,
    outputsize=num_periods,
    interval=period,)
  ts_trend = df_ts.with_rsi().with_macd().with_ema().with_stoch().as_pandas()
  ts_trend.to_csv('ts_momentum.csv')



#Define the visualization of trends to plot
  st.title("Plotting price trends w/ tech indicators")
  df = pd.read_csv("ts_momentum.csv")
  #df['datetime'] = df.index
  st.write(df.head(20))

  fig1 = px.line(df,x='datetime',y=['ema','close'] , title='Price Trends Over Time')
  st.plotly_chart(fig1)

  fig2 = px.line(df,x='datetime',y=['rsi','slow_k','slow_d'] , title='RSI & Stochastic  Over Time')
  st.plotly_chart(fig2)

  fig3 = px.bar(df,x='datetime',y=['macd_hist'] , title='MACD Over Time')
  st.plotly_chart(fig3)

  fig4 = px.bar(df,x='datetime',y=['volume'] , title='Volume Trend Over Time')
  st.plotly_chart(fig4)

viz_ETF = 'ARM'
num_periods = 100
period = '1h'

if __name__ == '__main__':
  trend_data(viz_ETF,num_periods,period,td)