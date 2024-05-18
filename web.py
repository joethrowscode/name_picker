import streamlit as st
import functions
import random

names = functions.get_names()

result = None

def add_name():
    name_added = st.session_state["new_name"] + '\n'
    names.append(name_added)
    functions.write_names(names)


def name_picker(name_list=names):
    picker_lower = 0
    picker_higher = len(name_list)
    name_result = random.randrange(picker_lower, picker_higher)
    picked_name = name_list[name_result]
    return picked_name


st.title("Name Picker")
st.subheader("Input values and randomly choose one of them.")

st.button(label="Pick a Name", key="picker_button")

if st.session_state.picker_button:
    result = name_picker()

st.text(result)

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

