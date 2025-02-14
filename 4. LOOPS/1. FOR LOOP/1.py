#  1. PRINT NUMBER FROM 1 TO 10
# for i in range(1,11):
#     print(i,end=" ")


# 2. SUM OF FIRST N NATURAL NUMBERS
# n=int(input("Enter a number: "))
# sum_n=0
# for i in range(1, n+1):
#     sum_n+=i
# print("sum: ",sum_n)

# 3. MULTIPLICATION TABLE OF A NUMBER
# num=5
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# 4. REVERSE A STRING
# string = "python"
# rev_string=""
# for char in string:
#     rev_string=char+rev_string
# print("Reversed: ", rev_string)

# 5. FACTORIAL OF A NUMBER
# num = 5
# fact=1
# for i in range(1, num+1):
#     fact*=i
# print("Factorial: ", fact)

# 6. PRINT EVEN NUMBERS FROM 1 TO 20
# for i in range(2,21,2):
#     print(i, end=" ")

# 7. FABONACCI SERIES UP TO N TERMS
# n=10
# a, b=0, 1
# for _ in range(n):
#     print(a, end=" ")
#     a, b=b, a+b

# 8. CHECK IF A NUMBER IS PRIME OR NOT 
# num=20
# is_prime = True
# for i in range(2, int(num**0.5)+1):
#     if num%i==0:
#         is_prime=False
#         break
# if is_prime:
#     print(f"{num} is prime")
# else:
#     print(f"{num} is not prime")
