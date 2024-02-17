from datetime import datetime

def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)
    
    
    difference_seconds = difference.total_seconds()
    
    return difference_seconds


date_format = "%Y-%m-%d %H:%M:%S"

date1_str = input("Enter the first date in format 'YYYY-MM-DD HH:MM:SS': ")
date2_str = input("Enter the second date in format 'YYYY-MM-DD HH:MM:SS': ")

date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)


difference_seconds = date_difference_in_seconds(date1, date2)

print( difference_seconds)


