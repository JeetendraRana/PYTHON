#  PROGRAM TO PRINT THE LARGEST OF THE THREE NUMBERS USING NESTED IF STATEMENT.
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
print("Number1: ",num1)
print("Number2: ",num2)
print("Number3: ",num3)
if num1>num2:
    if num1>num3:
        print("Number1 is greater")
if num2>num1:
    if num2>num3:
        print("Number2 is greater")
if num3>num1:
    if num3>num2:
        print("Number 3 is greater")