from datetime import datetime, timedelta


date = [int(x) for x in '2024-04-21 13:01:23'.split(" ")[0].split("-")] 
time = [int(x) for x in '2024-04-21 13:01:23'.split(" ")[1].split(":")] 
print(datetime(date[0],date[1],date[2], time[0], time[1], time[2]).strftime('%s'))
print(datetime(2024,4,21,13, 1, 23).strftime('%s'))