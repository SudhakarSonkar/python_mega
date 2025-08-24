import functions
import FreeSimpleGUI as sg
import time

sg.theme('Black')  # Set a theme for the GUI

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button(tooltip='Add todo', key='Add')
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

layout = [[clock], 
          [label], 
          [input_box, add_button], 
          [list_box, edit_button, complete_button],
          [exit_button]]
window = sg.Window('My To-Do App', 
                   layout=layout,
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)  # Update every secon
    window['clock'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))
    match event:
        case "Add":
            todo = functions.get_todos()
            todo.append(values['todo'] + '\n')
            functions.write_todos(todo)
            window['todos'].update(values=todo)
        
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select a to-do item first.")
        case "Complete":
            try:
                todo_to_remove = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_remove)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select a to-do item first.")
        case 'Exit':
            functions.write_todos(functions.get_todos())
            break
        
        case 'todos':
            window['todo'].update(value=values['todos'][0].strip())
        
        case sg.WIN_CLOSED:
            break    
        
window.close()
