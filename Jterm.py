import yfinance as yf
import streamlit as st
from datetime import date
import pandas as pd
import json
import matplotlib

PYPL = pd.read_csv('PYPL.csv')
NVDA = pd.read_csv('NVDA.csv')
UNH = pd.read_csv('UNH.csv')
TSLA = pd.read_csv('TSLA.csv')
BAC = pd.read_csv('BAC.csv')


def load_data():
   tickerData = yf.Ticker(str(tickerSymbol))
   tickerDf = tickerData.history(period='1d', start='2010-1-11', end=today)
def load_twitter_data():
   pass

tickerSymbol = 'NVDA'

today = date.today()



mode_selectbox = st.selectbox(
    'select mode',
    ('Twitter data','Stocks')
)
if mode_selectbox == 'Twitter data':
   add_selectbox = st.sidebar.selectbox(
    'Choose which stock you want twitter data for',
    ('PYPL','NVDA','UNH','TSLA','BAC')
    )


   if add_selectbox == 'PYPL':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = PYPL.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         PYPL.plot.scatter(x = side_select,y = 'High')
   elif add_selectbox == 'NVDA':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = NVDA.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         NVDA.plot.scatter(x = side_select,y = 'High')
   elif add_selectbox == 'UNH':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = UNH.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         UNH.plot.scatter(x = side_select,y = 'High')
   elif add_selectbox == 'TSLA':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = TSLA.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         TSLA.plot.scatter(x = side_select,y = 'High')
   elif add_selectbox == 'TSLA':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = TSLA.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         TSLA.plot.scatter(x = side_select,y = 'High')
   elif add_selectbox == 'BAC':
      select_status = st.sidebar.radio("Tweet Volume as X?", ('No','Yes'))
      if select_status == 'No':
         side_select = st.sidebar.selectbox(
         'Data Points',
         ('Open','Close','High','Low','Volume'))
      elif select_status == 'Yes':
         side_select = st.sidebar.selectbox(
         'Predictors',
         ('Sentiment','Tweet Vol'))

      if select_status == 'No':
         plot = BAC.plot(x = 'Date', y = side_select)
            #plt.figure()
      if select_status == 'Yes':
         BAC.plot.scatter(x = side_select,y = 'High')



if mode_selectbox == 'Stocks':
   slider = st.sidebar.slider('choose year for data',2010, 2021,2010)

   slider2 = st.sidebar.slider('choose month for data',1, 12,1)

   slider3 = st.sidebar.slider('choose day for data',1, 30,1)

   ticker_input = st.sidebar.text_input('Chose your stocks Ticker:')

   if ticker_input:
       tickerSymbol = ticker_input
       load_twitter_data()
       load_data()
   slider_minval = str(slider)[0:4]+'-'+str(slider2)+'-'+str(slider3)
   #slider_maxval = str(slider)[7:11]+str(today)[4:]
   tickerData = yf.Ticker(str(tickerSymbol))
   tickerDf = tickerData.history(period='1m', start=slider_minval, end=today)




if mode_selectbox == 'Stocks':



   st.write("""
   # J Term Project
   Shown are the stock closing price and volume of your stock
   """)

   stock = st.write(tickerSymbol)

   st.line_chart(tickerDf.Close)
   st.line_chart(tickerDf.Volume)
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()
