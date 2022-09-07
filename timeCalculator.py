import re

def add_time(startTime, duration, day = '') :
  print('STARTIME:', startTime)
  print('DURATION:', duration)  
  if day != '' : print('DAY OF THE WEEK:', day)
  
  amPm = f' {startTime[-2:]}'
  print('AM/PM:', amPm)
  newTime = re.sub(r':|AM|PM', '', startTime)
  print('NEWTIME:', newTime)
  newDur = re.sub(r':', '', duration)
  print('NEWDURATION1:', newDur)
  
  endTime = int(newTime) + int(newDur)
  
  # if endTime < 2400 : 
  
  
  splitTime = [*str(endTime)]
  splitTime.insert(-2, ':')
  splitTime.append(amPm)
  
  if day != '' :
    splitTime.append(f' {day}')  
  print(''.join(splitTime))
  
add_time("3:00 PM", "3:10")
# Should Return: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Should Return: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# Should Return: 12:03 PM

# add_time("10:10 PM", "3:30")
# Should Return: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# Should Return: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Should Return: 7:42 AM (9 days later)