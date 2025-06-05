import streamlit as st
import pandas as pd

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

st.title("Alle Aufgaben")
df = pd.DataFrame(st.session_state['tasks'].values())
st.dataframe(df)