from datetime import datetime ,timedelta
now_date = datetime.now()
withoutmicro = now_date.replace(microsecond=0)
print(withoutmicro)