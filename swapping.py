# using thier variable:
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

print(f"Numbers before swapping are number 1: {num1} and number 2: {num2}.")

temp = num1
num1 = num2
num2 = temp

print(f"Numbers after swapping are number 1: {num1} and number 2: {num2}.")

# without using third variable

num1 = num1+num2     
num2 = num1-num2
num1 = num1-num2

print(f"Again we swap the numbers without using third variable so result is number 1: {num1} and number 2: {num2}.")

"""
Dry run:
num1 = 5
num2 = 3
num1= 5+3 =8
num2= 8-3 =5
num1= 8-5 =3
"""