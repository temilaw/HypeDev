"""
Prompt the user to input their age and store it in the variable age as an integer
If age is greater than 100:
    - Display "Sorry you're dead."
Else if age is greater than 65:
    - Display "Enjoy your retirement!"
Else if age is greater than 40:
    - Display "You're over the hill."
Else if age is equal to 21:
    - Display "Congrats on your 21st!"
Else if age is less than 13:
    - Display "You qualify for the kiddie discount."
Otherwise:
    - Display "Age is but a number."

"""
age = int(input("Please enter your age: "))
if age > 100:
    print("Sorry you're dead.")
elif age >= 65:
    print("Enjoy your retirement!") 
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")