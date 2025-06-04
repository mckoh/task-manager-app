import streamlit as st

st.title("Aufgaben verwalten")
if st.session_state['tasks']:
    task_to_remove = st.selectbox("Wähle eine Aufgabe zum Entfernen", st.session_state['tasks'])
    if st.button("Aufgabe entfernen"):
        st.session_state['tasks'].remove(task_to_remove)
        st.rerun()
else:
    st.write("Keine Aufgaben vorhanden.")
