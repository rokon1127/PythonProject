import calendar

year = int(input("Enter Calender year: "))
month = int(input("Enter Calender Month: "))

print("You Entered: ",  year)
print("You Entered: ", month)

yy = year #year
mm = month #month
#display the calender
print(calendar.month(yy, mm))

#todays date and time
import datetime
now =datetime.datetime.now()
print(now)


print("==============Thank You==================")



