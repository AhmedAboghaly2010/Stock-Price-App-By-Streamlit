import streamlit as st
import yfinance as yf 
import pandas as pd

st.write(""" 
# Simple Stock Price App

shown are the stock **closing price** and ***volume*** of google! """)

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)  
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2023-5-31')

st.write(
    """ ## Closing Price"""
)
st.line_chart(tickerDf.Close)
st.write(
    """ ## Volume Price"""
)
st.line_chart(tickerDf.Volume)