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
  
  # Isolates AM/PM designation
  amPm = f'{startTime[-2:]}'
  # Isolates starting time variable to just digits
  newTime = re.sub(r':|AM|PM', '', startTime)
  # Isolates duration time variable to just digits
  newDur = re.sub(r':', '', duration)
  # How many days from start time to end duration
  daysLength = 0
  # If weekday is provided, lowercase provided spelling
  if day != '' :
    day = day.lower()
  
  # If starting time is PM, convert time to 24 hour clock
  if amPm == 'PM' :
    int(newTime) + 1200
    
  endTime = int(newTime) + int(newDur)

  # Splits total end time to individual digits in order to isolate hour/minutes 
  splitTime = [*str(endTime)] 
  
  # Isolates minutes to usable integer
  minutes = int(''.join(splitTime[-2:]))
  # Isolates hours to usable integer
  hour = int(''.join(splitTime[:-2]))
    
  # Converts all excess minutes into hours
  while minutes >= 60 : 
    minutes = minutes - 60
    hour = hour + 1
  
  # Converts all excess 12 day time hours into evening hours 
  while hour >= 12 :
    if amPm == 'AM' :
      amPm = 'PM'
    else :
  # Converts all excess 12 day time hours into evening hours & 
  # Updates weekday for every 24 hours converted   
      amPm = 'AM'
      daysLength = daysLength + 1
      day = next_day(day)  
    hour = hour - 12

  if minutes > 0 and minutes < 60 and hour >= 0 and hour < 13 :
    # Converts all 0 hours to midnight/noon
    if hour == 0 :
      hour = 12
    # Converts single digit minutes to readable time
    if minutes < 10 : 
      minutes = f'0{str(minutes)}'
    output = f'{hour}:{minutes} {amPm}'
    
    # Title cases weekday if provided
    if day != '' : 
      output = f'{output} {day.title()}'
      
    # Adds ending string based on days length
    if daysLength > 0:
      if daysLength == 1 :
        output = f'{output} (next day)'
      else : 
        output = f'{output} ({daysLength} days later)'
      
    print(output)