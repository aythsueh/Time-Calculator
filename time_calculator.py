def add_time(start, duration, week=False):

    weekday = dict({
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7})

    if week == False:
        weekcount = 99
    else:
        week_s = week.capitalize()
        weekcount = weekday[week_s]

    start_time, ampm_s = start.split()
    hour_s, minute_s = start_time.split(":")
    hour_d, minute_d = duration.split(":")
    hour_sum = int(hour_s) + int(hour_d)
    minute_sum = int(minute_s) + int(minute_d)

    if minute_sum > 59:
        hour_sum += 1
        minute_sum -= 60

    days = 0
  
    hours_left = hour_sum % 24
    days += hour_sum // 24

    while hour_sum > 11:
        hour_sum -= 12
        if ampm_s == "AM":
            ampm_s = 'PM'
            days -= 1
        else:
            ampm_s = "AM"
            days += 1
  
    ampm_sum = ampm_s

    if hour_sum == 0:  # 12AM or 12PM
        hour_sum = 12
        if ampm_sum == "AM":
            pass
        else:
            days += 1

    days_display = ""
    if days < 1:
        days_display = ""
    elif days == 1:
        days_display = " (next day)"
    else:
        days_display = " (" + str(days) + " days later)"

    new_weekday = {v: k for k, v in weekday.items()}
    
    if weekcount > 7:
        week_sum = ""
    else:
        weekcount_d = days % 7
        weekcount += weekcount_d
        if weekcount > 7 :
            weekcount %= 7
        week_sum = new_weekday[weekcount]

    hour_sum = str(hour_sum)

    if minute_sum < 10:
        minute_sum = "0" + str(minute_sum)
    else:
        minute_sum = str(minute_sum)

    if week == False:
        new_time = hour_sum + ":" + minute_sum + " " + ampm_sum + days_display
    else:
        new_time = hour_sum + ":" + minute_sum + " " + ampm_sum + ", " + week_sum + days_display

    return new_time
