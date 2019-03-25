#  coding: utf-8
"""
Request a temperature in Fahrenheit. Convert it to the equivalent temperature in Celsius and print the result.
"""

#  Prompt the user for a temperature in degrees Celsius.
f_temp = int(input("Please enter the temperature in degrees Fahrenheit. Enter as an integer.  "))

#  Convert to the equivalent temperature in Fahrenheit.
c_temp = (f_temp - 32) * 5 / 9

#  Print the results.
print("You entered " + str(f_temp) + "°F. The eqivalent in Celsius is " + str(c_temp) + "°C.")
