import streamlit as st
import pandas as pd
from os import path

st.set_page_config(layout='wide')

data_dir = path.join(path.curdir, '22_bonus', 'data')

df = pd.read_csv(path.join(data_dir,'data.csv'), sep=',')

st.title('The Best Company')
content = """
It allowance prevailed enjoyment in it. Calling observe for who pressed raising his. 
Can connection instrument astonished unaffected his motionless preference. 
Announcing say boy precaution unaffected difficulty alteration him. 
Above be would at so going heard. Engaged at village at am equally proceed. 
Settle nay length almost ham direct extent. 
Agreement for listening remainder get attention law acuteness day. 
Now whatever surprise resolved elegance indulged own way outlived.
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