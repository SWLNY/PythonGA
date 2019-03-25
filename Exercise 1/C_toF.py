#  coding: utf-8
"""
Request a temperature in Celsius. Convert it to the equivalent temperature in Fahrenheit and print the result.
"""

#  Prompt the user for a temperature in degrees Celsius.
c_temp = int(input("Please enter the temperature in degrees Celsius. Enter as an integer.  "))

#  Convert to the equivalent temperature in Fahrenheit.
f_temp = (c_temp * 9 / 5) + 32

#  Print the results.
print("You entered " + str(c_temp) + "°C. The eqivalent in Fahrenheit is " + str(f_temp) + "°F.")
