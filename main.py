import streamlit as st
import pandas as pd
from os import path

st.set_page_config(layout='wide')

data_dir = path.join(path.curdir, 'data')

df = pd.read_csv(path.join(data_dir,'data.csv'), sep=',')

st.title('The Best Company')
content = """
This is a mock-up company page. All names and images were delivered by [udemy course](https://www.udemy.com/course/the-python-mega-course/).
"""
st.write(content)
st.header('Our team:')

col1, empty_col1, col2, empty_col2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

for start_point, col in enumerate([col1, col2, col3]):
    with col:
        for index, row in df[start_point::3].iterrows():
            st.header(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
            st.write(row['role'])
            st.image(path.join(data_dir, row['image']))