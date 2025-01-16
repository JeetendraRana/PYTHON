# PROGRAM TO CHECK IF THE INPUT YEAR IS A LEAP YEAR OR NOT
year=int(input("Enter year to be calculated: "))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year," is a leap year!")
else:
    print(year," isn't a leap year!")