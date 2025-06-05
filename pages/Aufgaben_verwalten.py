import streamlit as st

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

st.title("Aufgaben verwalten")
if st.session_state['tasks']:
    task_to_remove = st.selectbox("Wähle eine Aufgabe zum Entfernen", st.session_state['tasks'].keys())
    if st.button("Aufgabe entfernen"):
        del st.session_state['tasks'][task_to_remove]
        st.rerun()
else:
    st.write("Keine Aufgaben vorhanden.")
