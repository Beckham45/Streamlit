import yfinance as yf 
import streamlit as st 
import pandas as pd


st.write(""" 
# *Simple Stock price app*

Shown below are the stock closing price and the volume of ***TESLA***

	""")

#Defining the ticker symbol
tickerSymbol = 'TSLA'

#Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#Get the historical prices for this ticker 
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)