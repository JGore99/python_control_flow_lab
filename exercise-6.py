# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input("Enter month using the first three letters")
day = input("Enter the day")
season = "" 
# season = None
if month == "Jan" or month == "Feb":
  season = "Winter"
  print(f"{month} {day} is in {season}")
if month == "Apr" or month == "May":
  season = "Spring"
  print(f"{month} {day} is in {season}")
if month == "Jul" or month == "Aug":
  season = "Summer"
  print(f"{month} {day} is in {season}")
if month == "Oct" or month == "Nov":
  season = "Fall"
  print(f"{month} {day} is in {season}")
if month == "Mar":
  if int(day) in range(1, 20):
    season = "Winter"
    print(f"{month} {day} is in {season}")
  if int(day) in range(21, 31):
    season = "Spring"
    print(f"{month} {day} is in {season}")
if month == "Jun":
  if int(day) in range(1, 20):
    season = "Spring"
  if int(day) in range(21, 31):
    season = "Summer"
  print(f"{month} {day} is in {season}")
if month == "Sep":
  if int(day) in range(1, 20):
    season = "Summer"
  if int(day) in range(21, 31):
    season = "Fall"
  print(f"{month} {day} is in {season}") 
if month == "Dec":
  if int(day) in range(1, 20):
    season = "Fall"
  if int(day) in range(21, 31):
    season = "Winter"
  print(f"{month} {day} is in {season}") 
    
