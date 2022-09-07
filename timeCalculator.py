# Import Regex capabilities
import re

def next_day(weekday) :
  switch = {
    'monday' : 'tuesday',
    'tuesday' : 'wednesday',
    'wednesday' : 'thursday',
    'thursday' : 'friday',
    'friday' : 'saturday',
    'saturday' : 'sunday',
    'sunday' : 'monday',
  }
  return switch.get(weekday)

def add_time(startTime, duration, day = '') :
  
  amPm = f'{startTime[-2:]}'
  newTime = re.sub(r':|AM|PM', '', startTime)
  newDur = re.sub(r':', '', duration)
  timeLength = 0
  if day != '' :
    day = day.lower()
  
  if amPm == 'PM' :
    int(newTime) + 1200
    
  endTime = int(newTime) + int(newDur)

  splitTime = [*str(endTime)] 
  
  minutes = int(''.join(splitTime[-2:]))
  hour = int(''.join(splitTime[:-2]))
    
  while minutes >= 60 : 
    minutes = minutes - 60
    hour = hour + 1
    if minutes == 0:
      minutes = '00'
  
  while hour >= 12 :
    if amPm == 'AM' :
      amPm = 'PM'
    else :
      amPm = 'AM'
      timeLength = timeLength + 1  
    hour = hour - 12

  if minutes > 0 and minutes < 60 and hour >= 0 and hour < 13 :
    if hour == 0 :
      hour = 12
    if minutes < 10 : 
      minutes = f'0{str(minutes)}'
    output = f'{hour}:{minutes} {amPm}'
    
    if day != '' : 
      output = f'{output} {day.title()}'
    
    if timeLength > 0:
      if timeLength == 1 :
        output = f'{output} (next day)'
      else : 
        output = f'{output} ({timeLength} days later)'
      
    print(output)
    
  
print('TEST###1:', '\n', add_time("3:00 PM", "3:10"), '\n')
# Should Return: 6:10 PM

print('TEST###2:', '\n', add_time("11:30 AM", "2:32", "Monday"), '\n')
# Should Return: 2:02 PM, Monday

print('TEST###3:', '\n', add_time("11:43 AM", "00:20"), '\n')
# Should Return: 12:03 PM

print('TEST###4:', '\n', add_time("10:10 PM", "3:30"), '\n')
# Should Return: 1:40 AM (next day)

print('TEST###5:', '\n', add_time("11:43 PM", "24:20", "tueSday"), '\n')
# Should Return: 12:03 AM, Thursday (2 days later)

print('TEST###6:', '\n', add_time("6:30 PM", "205:12"), '\n')
# Should Return: 7:42 AM (9 days later)