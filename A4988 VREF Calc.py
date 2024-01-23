I1 = float(input("What is the desired low current  (mA): "))/1000
I2 = float(input("What is the desired high current (mA): "))/1000
R =  float(input("What is the onboard resistor (Ohms):   "))
vref_LOW = I1*R/2
vref_HIGH = I2*R/2
print("Resulting VREF: " + str(vref_LOW) + "v -> " + str(vref_HIGH) + "v")
