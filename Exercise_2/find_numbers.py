"""
5.	Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

"""
values = []
for i in range(2000,3201):  # Check numbers one at a time in ascending order.
    if i % 7 == 0 and i % 5 != 0:  # Look for numbers evenly divisible by 7 but not by 5
        values.append(i)  # Capture each number with the right characteristics
print(values)

