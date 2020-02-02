import sys
import os

todos = ["but milk", "buy coffe"]

def print_menu(): 
  os.system("clear")
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
  print("'{}' has been added to your todos".format(name))

def update_todo():
  try:
    todo_id = int(input("Enter todo id: ")) - 1
    if todo_id >= 0 and todo_id < len(todos):
      print("Old name: {}".format(todos[todo_id]))
      new_name = input("New name: ")
      todos[todo_id] = new_name
      print("Updated successfully")
    else:
      print("Entered invalid todo id")
  except:
    print("Entered invalid todo id")
    
def delete_todo():
  try:
    todo_id = int(input("Enter todo id: ")) - 1
    if todo_id >= 0 and todo_id < len(todos):
      del todos[todo_id]
      print("Deleted successfully")
    else:
      print("Entered invalid todo id")
  except:
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

while True:
  print_menu()
  select_option()
