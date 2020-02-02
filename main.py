import sys
import os

todos = []

def print_menu(): 
  print("Todo manager\n")
  print("1. Show todos")
  print("2. Add todo")
  print("3. Update todo")
  print("4. Delete todo")
  print("9. Exit")

def print_todos():
  if len(todos) > 0:
    print("Your todos:")
    for (index, todo) in enumerate(todos):
      print("{}. {}".format(index + 1, todo))
  else:
    print("You have not any todos left")

def add_todo():
  name = input("Enter new todo name: ")
  todos.append(name)

  with open("todos.txt", "a") as todos_file:
    todos_file.write("\n{}".format(name))

  print("'{}' has been added to your todos".format(name))

def get_validated_todo_id():
  try:
    todo_id = int(input("Enter todo id: ")) - 1
    if todo_id >= 0 and todo_id < len(todos):
      return todo_id, True 
    else:
      return -1, False
  except:
      return -1, False

def update_todo():
  todo_id, is_valid = get_validated_todo_id()
  if is_valid:
    print("Old name: {}".format(todos[todo_id]))
    new_name = input("New name: ")
    with open("todos.txt", "r") as todos_file:
      lines = todos_file.readlines()
    with open("todos.txt", "w") as todos_file:
      for line in lines:
        if line.strip("\n") == todos[todo_id]:
          todos_file.write("{}\n".format(new_name))
        else:
          todos_file.write(line)

    todos[todo_id] = new_name
    print("Updated successfully")
  else:
    print("Entered invalid todo id")
 
    
def delete_todo():
  todo_id, is_valid = get_validated_todo_id()

  if is_valid:
    del todos[todo_id]
    with open("todos.txt", "r") as todos_file:
      lines = todos_file.readlines()
    with open("todos.txt", "w") as todos_file:
      for (index, line) in enumerate(lines):
        if index != todo_id:
          todos_file.write(line)

    print("Deleted successfully")
  else:
    print("Entered invalid todo id")

def close():
  sys.exit()

def select_option():
  option = input("\nSelect option: ")
  os.system("clear")

  if option == "1":
    print_todos()
  elif option == "2":
    add_todo()
  elif option == "3":
    update_todo()
  elif option == "4":
    delete_todo()
  elif option == "9":
    close()
  else:
    print("Invalid option")

  input("\nPress any key to continue...")

def load_todos():
  try:
    with open("todos.txt", "r") as todos_file:
      for todo in todos_file:
        todos.append(todo.strip())
  except:
    todos_file = open("todos.txt", "w")
    todos_file.close()

load_todos()
while True:
  os.system("clear")
  print_menu()
  select_option()

