from datetime import datetime , timedelta
now_date = datetime.now()
yesterday = now_date - timedelta(days=1)
tomorow = now_date + timedelta(days=1)
today = now_date
print(yesterday )
print(today)
print(tomorow)
