from functions import get_todos, write_todos
import time #modulo estandar de python.

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True : 
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()  #se utiliza para eliminar espacios en blanco de una cadena.

    
    if user_action.startswith("add"):
            
        todo = user_action[4:]
        todos = get_todos()
        todos.append(f"{todo}\n")
        write_todos(todos) #como no retorna nada, es solo un procedimiento, no lo almacenamos en una variable.

    elif user_action.startswith("show"):
  
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            #otra forma (por afuera del for se haria):
            #new_todos = [item.strip("\n") for item in todos] 
            row = f"{index + 1} - {item}"
            print(row)      

    elif user_action.startswith("edit"):
               
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:    
            number = int(user_action[9:])
            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            message = f"todo {todo_to_remove} was removed from the list"
            print(message)
        except ValueError:
            print("Your command is not valid")
            continue
        except IndexError:
            print("There is no item with that number.")

    elif user_action.startswith("exit"):   
        break #break rompe el bucle, hace que deje de ejecutarse. 

    else: 
        print("Hey, debes ingresar alguna de las opcions.. ")
        
print("Bye!")


   
    
    



