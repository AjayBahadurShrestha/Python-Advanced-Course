from datetime import datetime,timedelta
today=datetime.now()
future=today+timedelta(days=7)
print(f'Today: {today}')
print(f"The day after 7 days is {future}")

past=today-timedelta(days=3)
print(f"The day before 3 days is {past}")
