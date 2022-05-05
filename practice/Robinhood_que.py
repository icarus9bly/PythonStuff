"""

We are working on a security system for a badged-access room in our company's building.

We want to find employees who badged into our secured room unusually often. We have an unordered list of names and entry times over a single day. Access times are given as numbers up to four digits in length using 24-hour time, such as "800" or "2250".

Write a function that finds anyone who badged into the room three or more times in a one-hour period. Your function should return each of the employees who fit that criteria, plus the times that they badged in during the one-hour period. If there are multiple one-hour periods where this was true for an employee, just return the earliest one for that employee.

badge_times = [
  ["Paul",      "1355"], ["Jennifer",  "1910"], ["Jose",    "835"],
  ["Jose",       "830"], ["Paul",      "1315"], ["Chloe",     "0"],
  ["Chloe",     "1910"], ["Jose",      "1615"], ["Jose",   "1640"],
  ["Paul",      "1405"], ["Jose",       "855"], ["Jose",    "930"],
  ["Jose",       "915"], ["Jose",       "730"], ["Jose",    "940"],
  ["Jennifer",  "1335"], ["Jennifer",   "730"], ["Jose",   "1630"],
  ["Jennifer",     "5"], ["Chloe",     "1909"], ["Zhang",     "1"],
  ["Zhang",       "10"], ["Zhang",      "109"], ["Zhang",   "110"],
  ["Amos",         "1"], ["Amos",         "2"], ["Amos",    "400"],
  ["Amos",       "500"], ["Amos",       "503"], ["Amos",    "504"],
  ["Amos",       "601"], ["Amos",       "602"], ["Paul",   "1416"],
];

Expected output (in any order)
   Paul: 1315 1355 1405
   Jose: 830 835 855 915 930
   Zhang: 10 109 110
   Amos: 500 503 504

n: length of the badge records array

"""


badge_records = [
  ["Paul", "1355"],
  ["Jennifer", "1910"],
  ["Jose", "835"],
  ["Jose", "830"],
  ["Paul", "1315"],
  ["Chloe", "0"],
  ["Chloe", "1910"],
  ["Jose", "1615"],
  ["Jose", "1640"],
  ["Paul", "1405"],
  ["Jose", "855"],
  ["Jose", "930"],
  ["Jose", "915"],
  ["Jose", "730"],
  ["Jose", "940"],
  ["Jennifer", "1335"],
  ["Jennifer", "730"],
  ["Jose", "1630"],
  ["Jennifer", "5"],
  ["Chloe", "1909"],
  ["Zhang", "1"],
  ["Zhang", "10"],
  ["Zhang", "109"],
  ["Zhang", "110"],
  ["Amos", "1"],
  ["Amos", "2"],
  ["Amos", "400"],
  ["Amos", "500"],
  ["Amos", "503"],
  ["Amos", "504"],
  ["Amos", "601"],
  ["Amos", "602"],
  ["Paul", "1416"],
]

# Constraints:
# who badged into the room three or more times in a one-hour period
# times that they badged in during the one-hour
# multiple one-hour periods return the earliest one

# {"0th hour": [{Who1: times}, {Who1, times}],
#   "1st hour": }
from datetime import datetime
result = []
employee_record = {} # {name: [10,109,110]}
for records in badge_records:
    name = records[0]
    badge_time= records[-1]
    if name in employee_record:
        employee_record[name].append(int(badge_time))
    else:
        employee_record.update({name: [int(badge_time)]})

print(employee_record)
for k,v in employee_record.items():
    print(k,v)
    v.sort()
    parsed_dt = [datetime.strptime(str(dt), "%H%M") if len(str(dt)) != 1 else datetime.strptime(str(dt), "%H")  for dt in v]
    counter = 0
    for idx, elems in enumerate(parsed_dt):
        if idx == 0: continue
        diff = parsed_dt[idx] - parsed_dt[idx-1]
        if diff.seconds < 3600:
            counter +=1
            timeframe = (parsed_dt[idx], parsed_dt[idx-1])
        employee_record[k]= (counter, timeframe)
print(employee_record)
    