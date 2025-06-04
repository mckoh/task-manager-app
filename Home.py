import streamlit as st

# Initialisierung der Session State Liste
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []

st.title("Willkommen zur Aufgabenverwaltung!")
st.write("Navigiere über die Sidebar zu den anderen Screens.")