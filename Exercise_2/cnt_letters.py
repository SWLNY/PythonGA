"""
3. Write a program that accepts a sentence and calculate the number of
uppercase letters and lowercase letters. Suppose the following input
is supplied to the program.
"""
lower_cnt = 0  # The number of lower case letters
upper_cnt = 0  # The number of upper case letters

input_str = input("Please enter a string of characters: ")  # Get a string from user

for i in input_str:
    if ord(i) >= ord('a') and ord(i) <= ord('z'):  # Is the current character a lower case letter?
        lower_cnt += 1
    elif ord(i) >= ord('A') and ord(i) <= ord('Z'):  # Is the current character an upper case letter?
        upper_cnt += 1

print("You entered: " + input_str)
print("The number of upper case letters is: " + str(upper_cnt))
print("The number of lower case letters is: " + str(lower_cnt))
