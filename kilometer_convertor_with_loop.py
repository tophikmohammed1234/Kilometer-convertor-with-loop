# -*- coding: utf-8 -*-
"""Kilometer convertor with loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1S0wdfVM7Uw_0dV4EjxbYLg8K5_eQt40u
"""

# this Function convert killometer to mile
def mile(num1):
	return num1 * 0.62137119

# this Function convert killometer to meter
def meter(num1):
	return num1 * 1000

# this Function convert killometer to foot
def foot(num1):
	return num1 * 3280.8399

# this Function convert killometer to inch
def inch(num1):
	return num1 * 39370.0787

print("Please select operation -\n" \
		"1. mile\n" \
		"2. meter\n" \
		"3. foot\n" \
		"4. inch\n")
cont = 1
while(cont == 1):
  # Take input from the user
  select = int(input("Select operations form 1, 2, 3, 4 :"))

  number_1 = int(input("Enter the number you want to convert: "))

  if select == 1:
    print(number_1, "*", 0.62137119, "=")

  elif select == 2:
    print(number_1, "*", 1000, "=")
  elif select == 3:
    print(number_1, "*", 3280.8399, "=")
  elif select == 4:
    print(number_1, "*", 39370.0787, "=")
  else:
    print("Invalid input")
  cont= int(input("Do you want to continue? If yes press 1 if not press any key:-  "))