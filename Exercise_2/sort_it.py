"""
4.	Write a program that accepts a comma-separated sequence of words
as input and prints the words in a comma-separated sequence after sorting
them alphabetically. Suppose the following input is supplied to the program:
without, hello, bag, world
Then, the output should be: bag, hello, without, world
Ask the user to enter a string, and check if it is a palindrome. If yes,
print True, or else print False.

Funny example: Taco cat.

"""
user_inp = input('Please enter a comma-separated list of words: ')
word_seq = user_inp.replace(" ","").split(",") #  Turn the string entered into a list of words

word_seq_sort = sorted(word_seq, key=str.lower)  # Sort words being mindful of case
print("Input list: "+user_inp)  #  Display the input list of words
print("Sorted list: "+(", ".join(word_seq_sort))) #  Display the sorted list of words


input_str = input("\nPlease enter a string ")
orig = []  # List of characters in the order entered by user
rev = []  # List of characters, order is reversed
for char in input_str:  # Process characters one at a time, starting with the first one
    if char.isalpha():  # Only letters are of interest
        orig.append(char.lower())  # Build list of characters in the order entered
        rev.insert(0, char.lower())  # Build list of characters in reverse order
print(orig == rev)  #  Tell the user whether it's a palindrome