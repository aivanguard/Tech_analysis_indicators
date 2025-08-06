# Load Financial Data & Visualization Pkgs
from twelvedata import TDClient
#Get 12Data API
with open('api_key.txt', 'r') as file:
  api_key = file.read().strip()

# Access the environment variable for the key
# Load Financial Data & Visualization Pkgs
from twelvedata import TDClient
td = TDClient(apikey=api_key)

import streamlit as st
import pandas as pd
import plotly.express as px
import mplfinance as mpf



def get_price_trend(ETF,num_periods,period,td):
  df_ts = td.time_series(
    symbol=ETF,
    outputsize=num_periods,
    interval=period,)

  st.write(df_ts.with_bbands().with_atr().with_keltner().as_pandas().head(20))

  st.title("Plotting price trends w/ tech indicators")
  df = df_ts
  df['datetime'] = df.index


  fig1 = px.line(df,x='datetime',y=['lower_band','close','upper_band'] , title='Bollinger Bands Over Time')
  st.plotly_chart(fig1)

  fig2 = px.line(df,x='datetime',y=['lower_line','close','upper_line'] , title='Keltner Bands Over Time')
  st.plotly_chart(fig2)

  fig3 = px.bar(df,x='datetime',y=['atr'] , title='Avg True Range Over Time')
  st.plotly_chart(fig3)





if __name__ == '__main__':
  viz_ETF = 'ARM'
  num_periods = 100
  period = '1h'
  get_price_trend(viz_ETF,num_periods,period,td)