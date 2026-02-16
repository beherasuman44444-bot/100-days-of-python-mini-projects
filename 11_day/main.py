from datetime import datetime
date_1 = datetime(2020, 2, 25)

date_2 = datetime(2020, 9, 17)
delta = None
if date_1>date_2:
    print("date 1 is greater")
    delta = date_1 - date_2
else:
    print("date 2 is greater")
    delta = date_2 -date_1
print(delta.days)