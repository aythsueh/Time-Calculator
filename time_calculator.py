def add_time(start, duration, week=False):

  # adjust day of the week, build a dictionary for key(day of week)-value(1 to 7)
  weekday = dict({
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7
  })

  if week == False:
    weekcount = 99
    print("No day of week info entered, and weekcount=", weekcount)  #cccc 
  else:
    week_s = week.capitalize()
    weekcount = weekday[week_s]
    print("The day of week was entered: ", week_s, "; weekcount=", weekcount)  #cccc

  # split start time into 2, time & AM/PM; split time into hour and minute
  start_time, ampm_s = start.split()
  hour_s, minute_s = start_time.split(":")
  print("Starting time -- hour: ", hour_s, "; minute: ", minute_s, "; AM/PM: ", ampm_s)  #cccc

  # split duration time into hour and minute
  hour_d, minute_d = duration.split(":")
  print("Duration -- hour: ", hour_d,"; minute: ", minute_d)  #cccc

  # do the calculation
  hour_sum = int(hour_s) + int(hour_d)
  minute_sum = int(minute_s) + int(minute_d)
  print("Sum -- hour: ", hour_sum, "; minute: ", minute_sum)  # cccc

  # calculate if add hour by 1 when minute greater than 60
  if minute_sum > 59:
    hour_sum += 1
    minute_sum -= 60
  else:
    pass
  print("compute if sum minute > 60. Sum -- hour: ", hour_sum, "; minute: ", minute_sum)  #cccc

  # define the day count to zero first
  days = 0
  
  hours_left = hour_sum % 24
  days += hour_sum // 24
  print("Day count: ", days,
        "; number of hours left for following calculation: ", hours_left)  #cccc

  # calculate when end time greater than 12
  while hour_sum > 11:
    hour_sum -= 12
    if ampm_s == "AM":
      ampm_s = 'PM'
      days -= 1
    else:
      ampm_s = "AM"
      days += 1
  print("Day count after while loop for >12hrs: ", days)  #cccc
  
  ampm_sum = ampm_s

  if hour_sum == 0:  # 12AM or 12PM
    print("12AM or 12PM. hour_sum should be zero: ", hour_sum)  #cccc
    hour_sum = 12
    print("12AM or 12PM. hour_sum set to 12: ", hour_sum)  #cccc
    if ampm_sum == "AM":
      pass
    else:
      days += 1

  # calculate NA or next day or n days later
  days_display = ""
  if days < 1:
    days_display = ""
    print("Day count should be 0: ", days)  #cccc
  elif days == 1:
    days_display = " (next day)"
    print("Day count should be 1: ", days)  #cccc
  else:
    days_display = " (" + str(days) + " days later)"
    print("Day count should be >= 2 : ", days)  #cccc

  # adjust day of the week, reverse key(day of week) and value(1 to 7) in weekday
  new_weekday = {v: k for k, v in weekday.items()}
  print("weekcount: ", weekcount)
  if weekcount > 7:
    week_sum = ""
    print("weekcount > 7 aka week==False")  #cccc
  else:
    weekcount_d = days % 7
    print("days later: ", weekcount_d)  #cccc
    weekcount += weekcount_d
    print("The day of the week after adding: ", weekcount)  #cccc
    if weekcount > 7 :
      weekcount %= 7
      print("weekcount %= 7: ", weekcount)  #cccc
    week_sum = new_weekday[weekcount]
    print("Retrieve the day of the week from dictionary new_weekday: ", week_sum)  #cccc

  # adjust format of time, and convert from integer to strings for concatenation
  hour_sum = str(hour_sum)
  print("hour_sum: ", hour_sum)  # for checking

  if minute_sum < 10:
    minute_sum = "0" + str(minute_sum)
  else:
    minute_sum = str(minute_sum)
  print("minute_sum: ", minute_sum)  # for checking

  # concatenate the new_time variable and display it
  if week == False:
    new_time = hour_sum + ":" + minute_sum + " " + ampm_sum + days_display
  else:
    new_time = hour_sum + ":" + minute_sum + " " + ampm_sum + ", " + week_sum + days_display

  print(new_time)

  return new_time
