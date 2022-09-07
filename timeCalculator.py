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
  
  if amPm == ' PM' : 
    newTime = int(newTime) + 1200
  endTime = int(newTime) + int(newDur)
  
  if amPm == ' AM' and endTime > 1159 : 
    amPm = ' PM'

  # if endTime > 2400 : 

  if amPm == ' PM' and endTime < 2400 and endTime > 1200: 
    endTime = endTime - 1200 
  
  print(endTime)
  splitTime = [*str(endTime)] 
  print(splitTime)
  
  minutes = int(''.join(splitTime[-2:]))
  hour = int(''.join(splitTime[:-2]))
  
  if minutes > 0 and minutes < 60 and hour > 0 and hour < 13 :
    splitTime.insert(-2, ':')
    splitTime.append(amPm)

    if day != '' :
      splitTime.append(f' {day}')  
    print(''.join(splitTime))
    
  while minutes >= 60 : 
    minutes = minutes - 60
    hour = hour + 1

    
    
    
  
add_time("3:00 PM", "3:10")
# Should Return: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Should Return: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Should Return: 12:03 PM

# add_time("10:10 PM", "3:30")
# Should Return: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# Should Return: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Should Return: 7:42 AM (9 days later)