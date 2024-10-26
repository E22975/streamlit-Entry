import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image


st.title('Streamlit 超入門')

st.write('Interactive Widgets')

text = st.text_input('あなたの趣味を教えて下さい。')

'あなたの趣味 :' , text

condition = st.slider('あなたの今の調子は？', 0 ,100, 50)

'コンデション :' , condition

# st.write('Display Image')

# option = st.selectbox(
#       'あなたが好きな数字を教えて下さい。',
#       list(range(1,11))
#   )

# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('mokomini.JPG')
#     st.image(img, caption='Mini Moko', use_column_width=True)
    