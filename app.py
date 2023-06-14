import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Kullanıcıdan hisse senedi sembolünü alın
symbol = st.sidebar.text_input('Hisse Senedi Sembolü', value='ASELS')

# Streamlit uygulama başlığı
st.title( symbol + ' Hisse Senedi Grafiği')


# Kullanıcıdan veri aralığını alın
start_date = st.sidebar.date_input('Başlangıç Tarihi', value=datetime(2020, 1, 1))
end_date = st.sidebar.date_input('Bitiş Tarihi', value=datetime.now())

# Hisse senedi verilerini Yandex Finans API'si üzerinden alın
df = yf.download(symbol + '.IS', start=start_date, end=end_date)

# Verileri grafikleştirin
st.subheader('Hisse Senedi Fiyatları')
st.line_chart(df['Close'])

# Verilerin tablosunu gösterin
st.subheader('Hisse Senedi Verileri')
st.write(df)
