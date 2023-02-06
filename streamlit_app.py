import streamlit as st
from deta import Deta
from streamlit_autorefresh import st_autorefresh
from datetime import datetime, timedelta

if "spy1m_signal" not in st.session_state:
  st.session_state.spy1m_signal = ''
if "spy1m_count" not in st.session_state:
  st.session_state.spy1m_count = 0

deta = Deta('b0hip04s_DyG5HST9fRrAtbUr425Q9bDNLSaLScv5')

spy1m_db = deta.Base('SPY1m')
spy1m_delta = deta.Base('SPY1m_delta')
spy3m_db = deta.Base('SPY3m')
spy5m_db = deta.Base('SPY5m')
spy15m_db = deta.Base('SPY15m')
spy30m_db = deta.Base('SPY30m')
spy1h_db = deta.Base('SPY1h')
spy_current_price_db = deta.Base('SPY_PRICE')

market_price_data = spy_current_price_db.get('current')
market_price = float(market_price_data['price'])

timestamp = datetime.now()

spy1m_data = spy1m_db.get('current')
spy1m_price = float(spy1m_data['price'])
spy1m_delta_price = round(float(market_price)-spy1m_price,2)

if spy1m_data['signal'] != st.session_state.spy1m_signal:
  st.session_state.spy1m_count = 1
spy1m_delta.put({'key':st.session_state.spy1m_count, 'timestamp':str(timestamp), 'delta':spy1m_delta_price})
st.session_state.spy1m_count += 1

if spy1m_data['signal'] == 'buy':
  st.session_state.spy1m_signal = '🟢'
if spy1m_data['signal'] == 'sell':
  st.session_state.spy1m_signal = '🔴'

  
spy3m_data = spy3m_db.get('current')
spy3m_price = float(spy3m_data['price'])
if spy3m_data['signal'] == 'buy':
  spy3m_signal = '🟢'
if spy3m_data['signal'] == 'sell':
  spy3m_signal = '🔴'
spy3m_delta_price = float(market_price)-spy3m_price
  
spy5m_data = spy5m_db.get('current')
spy5m_price = float(spy5m_data['price'])
if spy5m_data['signal'] == 'buy':
  spy5m_signal = '🟢'
if spy5m_data['signal'] == 'sell':
  spy5m_signal = '🔴'
spy5m_delta_price = float(market_price)-spy5m_price
  
spy15m_data = spy15m_db.get('current')
spy15m_price = float(spy15m_data['price'])
if spy15m_data['signal'] == 'buy':
  spy15m_signal = '🟢'
if spy15m_data['signal'] == 'sell':
  spy15m_signal = '🔴'
spy15m_delta_price = float(market_price)-spy15m_price
  
spy30m_data = spy30m_db.get('current')
spy30m_price = float(spy30m_data['price'])
if spy30m_data['signal'] == 'buy':
  spy30m_signal = '🟢'
if spy30m_data['signal'] == 'sell':
  spy30m_signal = '🔴'
spy30m_delta_price = float(market_price)-spy30m_price
  
spy1h_data = spy1h_db.get('current')
spy1h_price = float(spy1h_data['price'])
if spy1h_data['signal'] == 'buy':
  spy1h_signal = '🟢'
if spy1h_data['signal'] == 'sell':
  spy1h_signal = '🔴'
spy1h_delta_price = float(market_price)-spy1h_price
  

now = datetime.now()
diff = timedelta(days=0, hours=-8)
combined = now + diff
dt_string = combined.strftime("%d %b %Y - %H:%M")
st.subheader(dt_string)
                         
                         
col1, col2, col3, col4, col5, col6 = st.columns(6)



col1.metric(label='SPY 1m', value=st.session_state.spy1m_signal, delta=spy1m_delta_price)
col2.metric(label='SPY 3m', value=spy3m_signal, delta=round(spy3m_delta_price,2))
col3.metric(label='SPY 5m', value=spy5m_signal, delta=round(spy5m_delta_price,2))                          
col4.metric(label='SPY 15m', value=spy15m_signal, delta=round(spy15m_delta_price,2))                          
col5.metric(label='SPY 30m', value=spy30m_signal, delta=round(spy30m_delta_price,2))                          
col6.metric(label='SPY 1h', value=spy1h_signal, delta=round(spy1h_delta_price,2))

st.write(spy1m_delta.fetch())

count = st_autorefresh(interval=60000, limit=1000, key="fizzbuzzcounter")
