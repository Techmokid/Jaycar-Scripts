vin = float(input("Please enter your input voltage: "))
vout = float(input("Please enter your output voltage: "))
res1 = float(input("Please enter the resistance of R1: "))
print("R2 will have a rough resistance of: " + str(vout*R1/(vin-vout)) + " ohms")
