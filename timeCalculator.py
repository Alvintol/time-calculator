# Import Regex capabilities
import re

# Provides the following weekday if provided
def next_day(weekday) :
  if weekday == '' : return ''
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
      day = next_day(day)  
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