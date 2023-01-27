import streamlit as st
from deta import Deta

deta = Deta('b0hip04s_DyG5HST9fRrAtbUr425Q9bDNLSaLScv5')

spy1m_db = deta.Base('SPY1m')
spy3m_db = deta.Base('SPY3m')
spy5m_db = deta.Base('SPY5m')
spy15m_db = deta.Base('SPY15m')
spy30m_db = deta.Base('SPY30m')
spy1h_db = deta.Base('SPY1h')

st.metric(label='SPY 1m', value=spy1m_db.get('current'))
