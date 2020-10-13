# Receiving input
user_name = input("What is your name? ")
birth_year = input("Which year were you born? ")

# Type conversion ? int() / str() / bool() / float()
age = 2020 - int(birth_year)
print("Hello, " + user_name.upper())

# A string of characters
win = "Jane"
won = False

# A variable is used to store data temporalily in a computers memory
win_name = user_name.upper()
confirmation = win.upper()

# Statements and Logical operators
if confirmation in win_name:
    won = True
else:
    print("You lose!")

if won is True:
    weight = input("Enter your weight: ")
    unit = input("Units (Enter Kgs or Lbs): ")
    if unit.upper() in "KGS":
        c_weight = float(weight)
        converted = c_weight / 0.45
        print("Name: " + user_name.upper())
        print("Age: " + str(age))
        print("Weight: " + str(converted) + " lbs")
        print("You're can get it " + user_name.upper())
    elif unit.upper() in "LBS":
        c_weight = float(weight)
        converted = c_weight * 0.45
        print("Name: " + user_name.upper())
        print("Age: " + str(age))
        print("Weight: " + str(converted) + " kgs")
        print("You can get it " + user_name.upper())
