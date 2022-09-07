import re

def add_time(startTime, duration, day = False) :
  print('STARTIME:', startTime)
  print('DURATION:', duration)  
  if day : print('DAY OF THE WEEK:', day)
  
  newTime = re.sub(r':|AM|PM', '', startTime)
  print('NEWTIME:', newTime)
  newDur = re.sub(r':', '', duration)
  print('NEWDURATION1:', newDur)
  
  endTime = int(newTime) + int(newDur)
  print(endTime)
  
add_time("3:00 PM", "3:10")
# Should Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# # Should Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# # Should Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# # Should Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# # Should Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# # Should Returns: 7:42 AM (9 days later)