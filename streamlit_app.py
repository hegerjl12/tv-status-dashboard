import streamlit as st
from deta import Deta
from streamlit_autorefresh import st_autorefresh
from datetime import datetime

deta = Deta('b0hip04s_DyG5HST9fRrAtbUr425Q9bDNLSaLScv5')

spy1m_db = deta.Base('SPY1m')
spy3m_db = deta.Base('SPY3m')
spy5m_db = deta.Base('SPY5m')
spy15m_db = deta.Base('SPY15m')
spy30m_db = deta.Base('SPY30m')
spy1h_db = deta.Base('SPY1h')

spy1m_data = spy1m_db.get('current')
spy1m_price = float(spy1m_data['price'])
if spy1m_data['signal'] == 'sell':
  spy1m_price = spy1m_price - 2*spy1m_price
  
spy3m_data = spy3m_db.get('current')
spy3m_price = float(spy3m_data['price'])
if spy3m_data['signal'] == 'sell':
  spy3m_price = spy3m_price - 2*spy3m_price
  
spy5m_data = spy5m_db.get('current')
spy5m_price = float(spy5m_data['price'])
if spy5m_data['signal'] == 'sell':
  spy5m_price = spy5m_price - 2*spy5m_price
  
spy15m_data = spy15m_db.get('current')
spy15m_price = float(spy15m_data['price'])
if spy15m_data['signal'] == 'sell':
  spy15m_price = spy15m_price - 2*spy15m_price
  
spy30m_data = spy30m_db.get('current')
spy30m_price = float(spy30m_data['price'])
if spy30m_data['signal'] == 'sell':
  spy30m_price = spy30m_price - 2*spy30m_price
  
spy1h_data = spy1h_db.get('current')
spy1h_price = float(spy1h_data['price'])
if spy1h_data['signal'] == 'sell':
  spy1h_price = spy1h_price - 2*spy1h_price
  

now = datetime.now()
diff = datetime.timedelta(days=0, hours=-8)
dt_string = now.strftime("%d %b %Y - %H:%M")
combined = dt_string + diff
st.subheader(combined)
                         
                         
col1, col2, col3, col4, col5, col6 = st.columns(6)
                          
col1.metric(label='SPY 1m', value=spy1m_data['signal'], delta=spy1m_price)
col2.metric(label='SPY 3m', value=spy3m_data['signal'], delta=spy3m_price)
col3.metric(label='SPY 5m', value=spy5m_data['signal'], delta=spy5m_price)                          
col4.metric(label='SPY 15m', value=spy15m_data['signal'], delta=spy15m_price)                          
col5.metric(label='SPY 30m', value=spy30m_data['signal'], delta=spy30m_price)                          
col6.metric(label='SPY 1h', value=spy1h_data['signal'], delta=spy1h_price)

count = st_autorefresh(interval=60000, limit=1000, key="fizzbuzzcounter")
