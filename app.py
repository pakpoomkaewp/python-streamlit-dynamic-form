import streamlit as st
import pandas as pd
import numpy as np

st.title('My First Streamlit App')

df = pd.DataFrame({
    'col1': [1, 2, 3],
    'col2': [10, 20, 30],
})

st.dataframe(df)

st.subheader('Line Chart Example')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

st.subheader('Interactive Slider')
x = st.slider('Select a value', min_value=0, max_value=100)
st.write(f'You selected: {x}')
