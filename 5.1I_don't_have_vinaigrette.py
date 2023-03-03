import datetime
import random

print('Enter a date YYYY-MM-DD:')
date1 = input()
print('Enter another date YYYY-MM-DD:')
date2 = input()
date1=date1.split('-')
date1=datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
date2=date2.split('-')
date2=datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))
if(date2<date1):
    temp=date1
    date1=date2
    date2=temp
time_delta=date2-date1

r=random.randint(0, time_delta.days)
print(date1+datetime.timedelta(days=r))