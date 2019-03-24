"""
Determine whether the number entered is even or odd.

Prompt the user for a number. Then print a message indicating whether the number is even or odd.
This is homework option 4.
"""
#  Ask the user to enter a number.
no_given = int(input("Please enter an integer number  "))

#  Evaluate the number entered by the user. Print a message indicating whether the number entered is even or odd.
if no_given % 2 == 0:
    print("\nYou entered " + str(no_given) + ". That number is even.")
else:
    print("\nYou entered " + str(no_given) + ". That number is odd.")
