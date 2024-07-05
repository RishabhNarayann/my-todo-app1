import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    print(todo)


st.title("My Todo App")
st.subheader("This is my todo app:")
#  for simple text st,write
st.write("This app is to increase your productivity:")

# st.checkbox("Buy grocery")
# st.checkbox("Thw the trash")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
        print(checkbox)

# st.text("Rishabh")
st.text_input(label='', label_visibility="collapsed", placeholder="Add new0 todo.....",
              on_change=add_todo, key="new_todo")
# print("Hello")
#
# st.session_state
