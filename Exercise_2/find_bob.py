"""
2. Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print Number of times bob occurs is: 2
Ask the user to input a string and then reversal the given input.
Input: "Programming in Python"
Output: nohtyP ni gnimmargorP
"""

bob_cnt = 0  # Counts the number of times 'bob' found
input_str = input("Please enter the character string to search: ")

for i in range(len(input_str) - 2):
    #  print(input_str[i:i+3])
    if input_str[i:i+3] == 'bob':  # Is the current three letter string 'bob'?
        bob_cnt += 1  # If 'bob' found, increment counter.
print("You entered: "+input_str)  # Inform the user
print("Number of times 'bob' found: "+str(bob_cnt))

input_str2 = input("\nPlease enter the string to reverse: ")
print(input_str2[::-1])  # Reverse the letters in the input string and display
