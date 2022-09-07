import re

def add_time(startTime, duration, day = '') :
  print('STARTIME:', startTime)
  print('DURATION:', duration)  
  if day != '' : print('DAY OF THE WEEK:', day)
  
  amPm = f'{startTime[-2:]}'
  print('AM/PM:', amPm)
  newTime = re.sub(r':|AM|PM', '', startTime)
  print('NEWTIME:', newTime)
  newDur = re.sub(r':', '', duration)
  print('NEWDURATION1:', newDur)
  timeLength = 0
  
  if amPm == 'PM' : 
    newTime = int(newTime) + 1200
  endTime = int(newTime) + int(newDur)
  
  print('ENDTIME:', endTime)
  if amPm == 'AM' and endTime > 1159 : 
    amPm = 'PM'

  # # if endTime > 2400 : 

  if amPm == 'PM' and endTime < 2400 and endTime > 1200: 
    endTime = endTime - 1200 
  
  print(endTime)
  splitTime = [*str(endTime)] 
  print(splitTime)
  
  minutes = int(''.join(splitTime[-2:]))
  hour = int(''.join(splitTime[:-2]))
  
  print('MINUTES:', minutes)
  print('MINUTES:', type(minutes))
  print('HOUR:', hour)
  print('AM/PM:', amPm)
    
  while minutes >= 60 : 
    minutes = minutes - 60
    hour = hour + 1
    if minutes == 0:
      minutes = '00'
    
  
  while hour > 12 :
    hour = hour - 12
    if amPm == 'AM' :
      amPm = 'PM'
    if amPm == 'PM' :
      amPm = 'AM'
      # timeLength = timeLength + 1
  
  print('MINUTES:', minutes)
  print('HOUR:', hour)
  print('AM/PM:', amPm)
  
  if minutes > 0 and minutes < 60 and hour > 0 and hour < 13 :
    if minutes < 10 : 
      minutes = f'0{str(minutes)}'
    output = f'{hour}:{minutes} {amPm}'
    
    if day != '' : 
      output = f'{output} {day}'
    
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