import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key='todo')
add_button = sg.Button("Add")

window = sg.Window('My To-Do App', 
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Add":
            todo = functions.get_todos()
            todo.append(values['todo'] + '\n')
            functions.write_todos(todo)
        case sg.WIN_CLOSED:
            break    
        

window.close()
