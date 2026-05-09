"""
These are the conditions used to identify leap years.
1.if the year can be evenly divided by 4, it is then a leap year
2.but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year
3.but if the year is evenly divided by 4 and also by 400, then it is a leap year
Ask a year input from user. And tell if the year entered by user is leap or
not.
"""
year = int(input("Enter a year: "))

if year%400==0:
    print(year, "is a Leap Year")
elif year%100==0:
    print(year, "is NOT a Leap Year")
elif year%4==0:
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

