import streamlit as st
import pandas as pd
from os import path
from send_email import send_email

st.set_page_config(layout='wide')

data_dir = path.join(path.curdir, '22_bonus', 'data')

df = pd.read_csv(path.join(data_dir,'topics.csv'), sep=',')

st.title('Contact us!')
st.write('Contact form:')

with st.form(key='contact_form'):
    user_mail = st.text_input('Your email adress')
    topic = st.selectbox(label='Topic', options=df)
    raw_message = st.text_area('Your message')

    message = f'Subject: [{topic}] New mail from {user_mail}\n'
    message += raw_message + '\n'
    message += f'From: {user_mail}'

    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        send_email(message)
        st.info('Your email has been sent')
