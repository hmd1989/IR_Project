import math
import datetime



today=datetime.date.today()
print(today)
thisYear=today.year
print(thisYear)
bornYear= input("Enter your birth year plz: ")
print("Year of born is : ", bornYear)
userAge=int(thisYear-bornYear)

print(" You are : %s " %userAge , "years old")





