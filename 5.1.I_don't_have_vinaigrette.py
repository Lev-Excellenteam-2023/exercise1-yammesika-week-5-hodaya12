import datetime
import random



date1 = input('Enter a date YYYY-MM-DD:')
date2 = input('Enter another date YYYY-MM-DD:')
date1=date1.split('-')
date2=date2.split('-')
try:
    date1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]))
    date2 = datetime.datetime(int(date2[0]), int(date2[1]), int(date2[2]))

    if date2 < date1:
        temp = date1
        date1 = date2
        date2 = temp

    time_delta = date2 - date1
    r = random.randint(0, time_delta.days)
    rand_date=date1 + datetime.timedelta(days=r)
    print("The random date between the two dates is: "+str(rand_date))
    if rand_date.strftime('%A')=="Monday":
        print("I dont have vinaigrette")

except:
  print("ERROR")
