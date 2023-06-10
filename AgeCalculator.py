print("==================AgeCalculator======================+")

from datetime import date
year = int(input("Birth Year: "))
month = int(input("Birth month: "))
day = int(input("Birth Day: "))

today = date.today()
birthdate = date(year, month, day)
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

print("Your age is: " , age, "years")

