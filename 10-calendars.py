import calendar

# print a text calendar (week start day is Sunday)
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2020, 1, 0, 0)
print (str)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2020, 1)
print (str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2020, 2):
  print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print (name)

for day in calendar.day_name:
  print (day)

# first Wednesday of every month
print ("First Wednesday of the month:")
for m in range(1,13):
  cal = calendar.monthcalendar(2020, m)
  weekone = cal[0]
  weektwo = cal[1]

  if weekone[calendar.WEDNESDAY] != 0:
    firstwednesday = weekone[calendar.WEDNESDAY]
  else:
    # if the first wednesday isn't in the first week, it must be in the second
    firstwednesday = weektwo[calendar.WEDNESDAY]
      
  print ("%10s %2d" % (calendar.month_name[m], firstwednesday))


