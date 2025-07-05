import time

from functions import get_todos, write_todos

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)


while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'  # Add newline

        todos = get_todos()
            
        todos.append(todo)
        
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
    
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1} - {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            
            todos = get_todos()
                
            new_todo = input("Enter new todo: ") + '\n'
            todos[number] = new_todo
            
            write_todos(todos)
            
        except (ValueError, IndexError):
            print("Invalid number for edit command.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = get_todos('todos.txt')

            todo_to_remove = todos.pop(index).strip('\n')

            write_todos(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)
        except (ValueError, IndexError):
            print("Invalid number for complete command.")

    elif user_action == 'exit':
        break

    else:
        print("Command is not valid.")
        
print("Bye!")
