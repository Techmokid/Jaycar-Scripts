vin  = float(input("What is the input voltage to the divider (In volts): "))
vout = float(input("What is the desired output voltage (In volts):       "))
I    = float(input("What is the required amount of current (In amps):    "))

R1 = round(vin/I,2)
P1 = round(I*I*R1,2)
#R2 = vout/(vin*(R1+1)) #This doesn't seem right?
R2 = (vout/vin)/(0.5/(R1))
P2 = 2*vout*vout/R2

print()
print("Resistor specs:")
print(" - R1: " + str(R1) + " ohms")
print(" - P1: " + str(P1) + " watts")
print(" - R2: " + str(R2) + " ohms")
print(" - P2: " + str(P2) + " watts")