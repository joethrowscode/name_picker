import streamlit as st
import random

names = [""]

st.title("Name Picker")
st.subheader("Input names and randomly choose one of them.")


def add_name():
    name = st.session_state["new_name"] + '\n'
    names.append(name)


for index, box_name in enumerate(names):
    checkbox = st.checkbox(box_name, key=box_name)
    if checkbox:
        names.pop(index)
        del st.session_state[box_name]
        st.rerun()


st.text_input(label="Enter a name and press return/enter: ",
              placeholder="Add new name here.",
              on_change=add_name, key="new_name")