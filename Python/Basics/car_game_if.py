status = "stopped"
while True:
    
    command= input ("> ")
    command=command.upper()
    if command == "help".upper():
        print("""
start - to start the car
stop - to stop the car
quit - to exit
""")
    elif command == "start".upper():  
        if status == "started":
            print("your car already started")
        else:
            print("your car started")
        status = "started"
        
    elif command =="stop".upper():
        if status == "stopped":
            print("your car already stopped")
        else:
            print("your car stopped")
        status = "stopped"
    
    elif command == "quit".upper():
        break
    
    else:
        print("I don't understand that")
