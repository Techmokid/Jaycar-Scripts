#Constants
hoursPracticalSunlight = 8
SLA_min_charge_perc = 0.6
AGM_min_charge_perc = 0.85
Cost_per_kW = 0.23

# 1. User Inputs
#powerRequiredPerDay = float(input("How many kW of power do you use on average per day: "))
#powerRequiredPerDay = float(input("How many W of power do you use on average per hour: "))*24/1000
#powerRequiredPerDay = float(input("How many kW of power do you use on average per hour: "))*24

# 2. Manual power calc
#powerRequiredPerDay = 1200*10 # Aircon
#powerRequiredPerDay += 750*8  # Tyler PC
#powerRequiredPerDay += 750*24 # My PC
#powerRequiredPerDay += 1200/2 # Dryer
#powerRequiredPerDay += 1000/2 # Washing Machine
#powerRequiredPerDay /= 1000
#powerRequiredPerDay = 24*12/1000
powerRequiredPerDay = 24*180/1000

#Calculations
powerRequiredPerHour = powerRequiredPerDay/24
storedPowerNeeded = (24-hoursPracticalSunlight)*powerRequiredPerHour

#Helper Functions
def strRnd(x):
	return str(round(x,2))

def getCableGaugeFromCurrent(amps):
	if (amps <= 7.5):
		return "18"
	elif (amps <= 15):
		return "15"
	elif (amps <= 25):
		return "12"
	elif (amps <= 40):
		return "10"
	elif (amps <= 56):
		return "8"
	elif (amps <= 65):
		return "6"
	elif (amps <= 100):
		return "4"
	elif (amps <= 150):
		return "2"
	elif (amps <= 200):
		return "0"
	else:
		return "UNKNOWN"

#Display Resulting Data
print("Average power usage per year:   " + strRnd(powerRequiredPerDay*365.25) + " kW/yr")
print("Average power usage per week:   " + strRnd(powerRequiredPerDay*7) + " kW/wk")
print("Average power usage per day:    " + strRnd(powerRequiredPerDay) + " kW/day")
print("Average power usage per hour:   " + strRnd(powerRequiredPerHour) + " kW/h")
print()
print("Cost of power per year:         $" + strRnd(365.25*Cost_per_kW*powerRequiredPerDay))
print("Cost of power per bimonth:      $" + strRnd((365.25*2)/12*Cost_per_kW*powerRequiredPerDay))
print("Cost of power per month:        $" + strRnd((365.25/12)*Cost_per_kW*powerRequiredPerDay))
print("Cost of power per week:         $" + strRnd(7*Cost_per_kW*powerRequiredPerDay))
print("Cost of power per day:          $" + strRnd(Cost_per_kW*powerRequiredPerDay))
print()
print("Required stored power:          " + strRnd(storedPowerNeeded) + " kW")
print()
print("Required stored capacity (12v): " + strRnd(1000*storedPowerNeeded/12) + " Ah")
print(" - AGM 12v batteries:           " + strRnd((1000*storedPowerNeeded/12)/AGM_min_charge_perc) + " Ah")
print(" - SLA 12v batteries:           " + strRnd((1000*storedPowerNeeded/12)/SLA_min_charge_perc) + " Ah")
print()
print("Required stored capacity (24v): " + strRnd(1000*storedPowerNeeded/24) + " Ah")
print(" - AGM 24v batteries:           " + strRnd((1000*storedPowerNeeded/24)/AGM_min_charge_perc) + " Ah")
print(" - SLA 24v batteries:           " + strRnd((1000*storedPowerNeeded/24)/SLA_min_charge_perc) + " Ah")
print()
print("Required generated power:       " + strRnd(powerRequiredPerDay) + " kW per day")
print("Solar panel generation ability: " + strRnd(powerRequiredPerDay/hoursPracticalSunlight) + " kW")
print()
chrgRate = 1000*(powerRequiredPerDay/hoursPracticalSunlight)/12
print("Battery 12v charge rate:        " + strRnd(chrgRate) + " Amps")
print("Recommended gauge cable:        " + getCableGaugeFromCurrent(chrgRate) + " AWG")
chrgRate = 1000*(powerRequiredPerDay/hoursPracticalSunlight)/24
print("Battery 24v charge rate:        " + strRnd(chrgRate) + " Amps")
print("Recommended gauge cable:        " + getCableGaugeFromCurrent(chrgRate) + " AWG")
