from datetime import date

lastIncident = date(2023, 1, 1)
#currentDate = date.today()

dateInput = input("What date is it: ")
dateArray = dateInput.split('/')
if (len(dateArray) == 1):
    dateArray = dateInput.split('-')
if (len(dateArray) == 1):
    dateArray = dateInput.split('_')

if (len(dateArray[2]) == 2):
    dateArray[2] = "20" + dateArray[2]

day = int(dateArray[0])
month = int(dateArray[1])
year = int(dateArray[2])

currentDate = date(year, month, day)
delta = currentDate - lastIncident 
  
print("FUSE day counter: " + str(delta.days + 1) + " on date " + str(currentDate))
print()
print()
input("Press enter to close")
