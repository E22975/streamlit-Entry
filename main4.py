import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('Streamlit 超入門')

st.write('Interactive Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button :
    right_column.write('ここは右カラム')
     
  
expandar1 = st.expander('問い合わせ1')
expandar1.write('問い合わせ1の回答')
expandar2 = st.expander('問い合わせ2')
expandar2.write('問い合わせ2の回答')
expandar3 = st.expander('問い合わせ3')
expandar3.write('問い合わせ3の回答')



# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0 ,100, 50)

# st.sidebar.write('Interactive Widgets')
# text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
# condition = st.sidebar.slider('あなたの今の調子は？', 0 ,100, 50)


# 'あなたの趣味 :' , text
# 'コンデション :' , condition

# st.write('Display Image')

# option = st.selectbox(
#       'あなたが好きな数字を教えて下さい。',
#       list(range(1,11))
#   )

# 'あなたの好きな数字は、', option, 'です。'


# if st.checkbox('Show Image'):
#     img = Image.open('mokomini.JPG')
#     st.image(img, caption='Mini Moko', use_column_width=True)
    