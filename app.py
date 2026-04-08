
import streamlit as st
import pandas as pd
from inference import run_suite
import io
from contextlib import redirect_stdout

st.set_page_config(page_title='OpenEnv CRM Cleaner', page_icon='🧹')

st.title('🧹 OpenEnv CRM Cleaner Dashboard')
st.markdown('### Real-time Environment Visualization')

col1, col2, col3 = st.columns(3)
with col1:
    st.metric('Tasks', '3')
with col2:
    st.metric('Status', 'Active')
with col3:
    st.metric('SDK', 'Docker')

st.sidebar.header('Configuration')
task_selection = st.sidebar.selectbox('Select Task', ['clean_001 (Easy)', 'clean_002 (Medium)', 'clean_003 (Hard)'])

if st.button('Run Baseline Evaluation'):
    st.info('Running inference.py suite...')
    f = io.StringIO()
    with redirect_stdout(f):
        run_suite()
    out = f.getvalue()
    st.code(out, language='text')

st.markdown('---')
st.subheader('Environment State Preview')
data = {
    'ID': [1, 2, 3],
    'Name': ['john doe', 'Alice', 'CyberDyne'],
    'Status': ['Messy', 'Duplicate', 'Unknown Industry'],
    'Difficulty': ['Easy', 'Medium', 'Hard']
}
st.table(pd.DataFrame(data))
