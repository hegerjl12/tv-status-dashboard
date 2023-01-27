import streamlit as st
from deta import Deta

deta = Deta('b0hip04s_DyG5HST9fRrAtbUr425Q9bDNLSaLScv5')

spy1m_db = deta.Base('SPY1m')
spy3m_db = deta.Base('SPY3m')
spy5m_db = deta.Base('SPY5m')
spy15m_db = deta.Base('SPY15m')
spy30m_db = deta.Base('SPY30m')
spy1h_db = deta.Base('SPY1h')

spy1m_data = spy1m_db.get('current')
if spy1m_data['signal'] == 'sell':
  sp1m_price = "-" + spy1m_data['price']
  
spy3m_data = spy3m_db.get('current')
spy5m_data = spy5m_db.get('current')
spy15m_data = spy15m_db.get('current')
spy30m_data = spy30m_db.get('current')
spy1h_data = spy1h_db.get('current')

                         
col1, col2, col3, col4, col5, col6 = st.columns(6)
                          
col1.metric(label='SPY 1m', value=spy1m_data['signal'], delta=spy1m_price)
col2.metric(label='SPY 3m', value=spy3m_data['signal'], delta=spy3m_data['price'])
col3.metric(label='SPY 5m', value=spy5m_data['signal'], delta=spy5m_data['price'])                          
col4.metric(label='SPY 15m', value=spy15m_data['signal'], delta=spy15m_data['price'])                          
col5.metric(label='SPY 30m', value=spy30m_data['signal'], delta=spy30m_data['price'])                          
col6.metric(label='SPY 1h', value=spy1h_data['signal'], delta=spy1h_data['price'])                          
