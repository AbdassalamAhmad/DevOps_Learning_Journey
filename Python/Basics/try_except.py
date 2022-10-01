try:
    age = int(input("age: "))
    print ("your age is: " + str(age))
# If we add a line to divide income by age we don't want to divide by zero error to occur.
except ZeroDivisionError:
    print("Age cannot be zero")
except ValueError:
    print ("Invalid input, enter a number.")
