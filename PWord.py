import datetime
now = datetime.datetime.now()
year=now.year
month=now.month
day=datetime.datetime.today().weekday()
count=0
day2=""
weekdays=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in range (0,7):
    if day==x:
        day2=weekdays[x]
year=str(year)
month=str(month)
username=""
username=(day2+month+year)
print(username)
