# Program to calculate 
# This program is used to perform operations like addition , substraction , division and multiplication

# Functions to perform operations :
def add(num1,num2):
    result=num1+num2
    return result
def sub(num1,num2):
    result=num1-num2
    return result
def multi(num1,num2):
    result=num1*num2
    return result
def div(num1,num2):
    result=num1/num2
    return result

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
# User Inputs
num1=int(input("Enter Number 1 :"))
num2=int(input("Enter Number 2 :"))

operation=input("Enter which operation should be performed among 1 to 4:")

if operation=="1":
    result=add(num1,num2)
elif operation=="2":
    result=sub(num1,num2)
elif operation=="3":
    result=multi(num1,num2)
else:
    result=div(num1,num2)

print(result)