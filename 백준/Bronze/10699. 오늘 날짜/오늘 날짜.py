import datetime

today = datetime.datetime.today() + datetime.timedelta(hours=9)
print(str(today)[:10])
