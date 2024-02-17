from datetime import datetime, timedelta


now_date = datetime.now()


new_date = now_date - timedelta(days=5)
print(new_date)