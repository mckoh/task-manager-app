import streamlit as st
import pandas as pd

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = {}

st.title("Neue Aufgabe hinzufügen")

task_name = st.text_input("Aufgabenname", key="task_name")
task_priority = st.slider("Priorität", 1, 10, 5, key="task_prio")
task_due = st.date_input("Fälligkeitsdatum", key="task_due")

if st.button("Aufgabe hinzufügen"):
    if task_name:
        st.session_state['tasks'][task_name] = {
            'Beschreibung': task_name,
            'Priorität': task_priority,
            'Fälligkeitsdatum': task_due
        }
        st.success(f"Aufgabe '{task_name}' hinzugefügt!")
    else:
        st.error("Bitte gib einen Aufgabenname ein.")