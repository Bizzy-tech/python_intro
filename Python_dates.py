from datetime import date, timedelta

today = date.today()

print(today)
f_date = today.strftime("%d/%m/%Y")
print(f_date)
expiry_date = today + timedelta(days=30)
print(expiry_date)

date1 = date(2005,1,16)
date2 = date(1998,12,25)
difference = date1 - date2
print(difference)