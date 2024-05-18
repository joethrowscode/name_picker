import streamlit as st
import functions
import random

names = functions.get_names()


def add_name():
    name_added = st.session_state["new_name"] + '\n'
    names.append(name_added)
    functions.write_names(names)


st.title("Name Picker")
st.subheader("Input values and randomly choose one of them.")

st.button(label="Pick a Name", key="picker_button", on_click="name_picker()")

st.text(body="name_picker()")

st.write("Tick the checkbox to remove a value.")

st.text_input(label="Enter a name and press return/enter: ",
              placeholder="Add new name here.",
              on_change=add_name, key="new_name")

for index, box_name in enumerate(names):
    checkbox = st.checkbox(box_name, key=box_name)
    if checkbox:
        names.pop(index)
        functions.write_names(names)
        del st.session_state[box_name]
        st.rerun()

