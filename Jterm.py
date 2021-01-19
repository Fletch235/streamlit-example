import yfinance as yf
import streamlit as st
from datetime import date
import pandas as pd
import json

def load_data():
   tickerData = yf.Ticker(str(tickerSymbol))
   tickerDf = tickerData.history(period='1d', start='2010-1-11', end=today)
def load_twitter_data():
   pass

today = date.today()
print("Today's date:", today)


slider = st.sidebar.slider('choose year for data',2010, 2021,2010)

slider2 = st.sidebar.slider('choose month for data',1, 12,1)

slider3 = st.sidebar.slider('choose day for data',1, 30,1)
#st.slider("Number of turns in spiral", 1, 100, 9)

add_selectbox = st.sidebar.selectbox(
    'Choose which stock you want twitter data for',
    ('','NVDA','')
)

# Add a slider to the sidebar:
ticker_input = st.sidebar.text_input('Chose your stocks Ticker:')


st.write("""
# J Term Project
Shown are the stock closing price and volume of your stock
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'NVDA'


if add_selectbox:
    ticker_input = ''
    tickerSymbol = add_selectbox
    load_data()
if ticker_input:
    add_selectbox = ''
    tickerSymbol = ticker_input
    load_twitter_data()
    load_data()


slider_minval = str(slider)[0:4]+'-'+str(slider2)+'-'+str(slider3)
#slider_maxval = str(slider)[7:11]+str(today)[4:]
tickerData = yf.Ticker(str(tickerSymbol))
tickerDf = tickerData.history(period='1m', start=slider_minval, end=today)


# Open	High	Low	Close	Volume	Dividends	Stock Splits


stock = st.write(tickerSymbol)

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
