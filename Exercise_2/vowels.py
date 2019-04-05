"""
1.	Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
"""
found_cnt = 0  # number of vowels in string
vowels = ('a','A','e','E','i','I','o','O','u','U')
s = "azcbobobEgghakl"  # String to search

for x in s:
    if x in vowels:  # Is the current character a vowel?
        found_cnt += 1  # Yes, increment counter
print('Number of vowels is ' + str(found_cnt))

