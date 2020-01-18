# SuperMarket.py - This program creates a report that lists weekly hours worked 
# by employees of a supermarket. The report lists total hours for 
# each day of one week. 
# Input:  Interactive
# Output: Report. 

# Declare variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "Day Total "
SENTINEL = "done"   # Named constant for sentinel value
hoursWorked = 0     # Current record hours
hoursTotal = 0      # Hours total for a day
prevDay = ""        # Previous day of week
notDone = True      # loop control
monHours = 0
tuesHours = 0
wedHours = 0
thurHours = 0
friHours = 0
satHours = 0
sunHours = 0

def dayChange(hoursWorked, dayHours):
    dayHours += int(hoursWorked)
    return dayHours

# Print two blank lines.
print("\n\n")
# Print heading.
print("\t" + HEAD1)
# Print two blank lines.
print("\n\n")

# Read first record 
dayOfWeek = input("Enter day of week or done to quit: ")
if dayOfWeek == SENTINEL:
    notDone = False
else:
    hoursWorked = input("Enter hours worked: ")
    if dayOfWeek == "Monday":
        monHours = dayChange(hoursWorked, monHours)
    #print(monHours)
    
while notDone == True:
    # Implement control break logic here
    # Include work done in the dayChange() function
    print("\n\n")
    print("\t" + HEAD1)
    print("\n\n")
    dayOfWeek = input("Enter day of week or done to quit: ")
    if dayOfWeek  == SENTINEL:
        notDone = False
    else:
        hoursWorked = input("Enter hours worked: ")
        print(monHours)
        monHours = dayChange(hoursWorked, monHours)

print("Monday Hours:")    
print("\t" + DAY_FOOTER + str(monHours))

print("Tuesday Hours:")
print("\t" + DAY_FOOTER + str(tuesHours))

print("Wednesday Hours:")    
print("\t" + DAY_FOOTER + str(wedHours))

print("Thursday Hours:")   
print("\t" + DAY_FOOTER + str(thurHours))

print("Friday Hours:")   
print("\t" + DAY_FOOTER + str(friHours))

print("Saturday Hours:")    
print("\t" + DAY_FOOTER + str(satHours))

print("Sunday Hours:")   
print("\t" + DAY_FOOTER + str(sunHours))