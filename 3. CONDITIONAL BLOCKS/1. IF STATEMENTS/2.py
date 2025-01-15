# Program to print the largest of the three numbers.
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
print("Number1:",num1)
print("Number2:",num2)
print("Number3:",num3)
if num1>num2 and num1>num3:
    print("Number1 is greater: ",num1)
if num2>num1 and num2>num3:
    print("Number2 is greater: ",num2)
if num3>num1 and num3>num2:
    print("Number3 is greater: ",num3)