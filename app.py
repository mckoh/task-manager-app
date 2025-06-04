

import streamlit as st


st.title("Hello, Streamlit!")
st.markdown("This is a simple **Streamlit** app *to* demonstrate the `basic` setup.")

betreff = st.text_input("Task Betreff")
st.slider("Task Priority", 0, 100, 50)
st.checkbox("Task Completed")
st.button("Submit")

print(betreff)