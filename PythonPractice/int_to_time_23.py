time = int(input("Enter number of seconds: "))

days = 0
hours = 0
minutes = 0
seconds = time

one_day = 24 * 60 * 60
if seconds > one_day:
    days = seconds // one_day
    seconds -= days * one_day

one_hour_seconds = 60 * 60

if seconds > one_hour_seconds:
    hour = seconds // one_hour_seconds
    seconds -= hour * one_hour_seconds

one_minute_seconds = 60

if seconds > one_hour_seconds:
    minute = seconds // one_minute_seconds
    seconds -= minute * one_minute_seconds

print(f"{time}:, seconds equals to {days} days, and {hours} hours, and {minutes} minutes, and {seconds} seconds.")

 





