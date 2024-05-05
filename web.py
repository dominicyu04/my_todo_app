import streamlit as st
import functions


todos = functions.get_todos()
print("XXXXXXX")


def add_todo():
    todo = st.session_state["new todo"]+"\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is used to increase you productivity.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()# it will rerun automatically


# st.text_input(label="Enter a todo:") the label is on the top of the input box and label is a required argument
st.text_input(label="label", placeholder="Add a new todo", on_change=add_todo,
              key="new todo", )

print("Hello")
st.session_state
