import streamlit as st
st.title("My first project")
name = st.text_input("Kak se kazvash?")
if name:
  st.write(f"Zdravei, {name}!")
