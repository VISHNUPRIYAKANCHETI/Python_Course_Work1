'''from datetime import date,time,datetime,timedelta
t=date.today()
print(t)
print(t.day)
print(t.month)
print(t.year)
print(t.weekday())
year,month,day=list(map(int,input("[YYYY-MM-DD]").split("-")))
print(date(year,month,day))'''
'''from datetime import time
tm = time (23,5,5)
print(tm)
print(tm.hour)
print(tm.minute)
print(tm.second)'''
'''
from datetime import datetime
dt=datetime.now()
print(dt)
print(dt.strftime('%d %m %y')) #y=26
print(dt.strftime('%d %m %Y')) #Y=2026
print(dt.strftime('%d-%m-%Y,%H:%M:%S')) 
print(dt.strftime('%d-%m-%y,%I:%M:%S %p')) #p -for AM or Pm
print(dt.strftime('%d-%m-%y,%I:%M:%S')) #I for 12 hours
print(dt.strftime('%d-%m-%b,%I:%M:%S'))
print(dt.strftime('%d-%m-%B,%I:%M:%S'))
print(dt.strftime('%a,%d-%B,%I:%M:%S'))
print(dt.strftime('%A-%d-%B,%I:%M:%S'))

'''
'''
from datetime import datetime,date,timedelta
dt=datetime.now()
t=date.today()
t7=dt+timedelta(days=7)
m15=dt+timedelta(minutes=15)
print(t7)
print(m15)
'''
from itertools import permutations,combinations
s='abc'
res1= list(permutations(s,2))
print([''.join(i) for i in res1])
res2=(list(combinations(s,2)))
print([''.join(i) for i in res2])

