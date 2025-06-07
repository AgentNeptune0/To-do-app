to_do_list = []
while True:
  print("--To do list--")
  print("1.View tasks ")
  print("2.Add tasks")
  print("3.Remove tasks")
  print("4.Exit")
  option= int(input("Choose an option (1-4) "))
  print("")
  if option == 1:
    
    print("Your tasks are:")
    print(to_do_list)
    print("")
  elif option == 2:
    task = str(input("What task do you want to add? "))
    to_do_list.append(task)
    print("The task is now in the list.")
    print("")
  elif option == 3:
    remove_task = str(input("What task would you like to remove? "))
    to_do_list.remove(remove_task)
    print("The task is now removed from the list. ")
  else:
    print("Thank you for using this app.Bye bye. ")
    break