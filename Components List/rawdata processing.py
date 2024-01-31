rawdata = []
with open("rawdata.txt",'r') as f:
    rawdata = f.readlines()

newlinelessdata = []
for i in rawdata:
    if (i.replace(" ","").replace("\n","").replace("\t","") != ""):
        newlinelessdata.append(i.replace("\n",""))
rawdata = newlinelessdata

def contains(x,arr):
    for i in arr:
        if (x == i):
            return True
    return False

partialstrippedData = []
for i in range(0,len(rawdata)):
    if ("$" in rawdata[i]):
        continue
    if contains(rawdata[i],["1","ADD TO CART","COMPARE","WISHLIST","CHECK STORE","STORE PICKUP","CHECK STORE STOCK","DISCONTINUED"]):
        continue
    if (i != len(rawdata)-1)and(rawdata[i] == rawdata[i+1]):
        continue
    
    partialstrippedData.append(rawdata[i])

strippedData = []
for i in range(0,len(partialstrippedData),2):
    componentType = "         "
    if "resistor" in partialstrippedData[i].lower():
        componentType = "Resistor "
    elif "capacitor" in partialstrippedData[i].lower():
        componentType = "Capacitor"
    elif "greencap" in partialstrippedData[i].lower():
        componentType = "Capacitor"
    elif "electrolytic" in partialstrippedData[i].lower():
        componentType = "Capacitor"

    if "smd" in partialstrippedData[i].lower():
        continue
    #if componentType.replace(" ","").replace("\n","").replace("\t","") == "":
    #    continue
    if (partialstrippedData[i+1].replace("CAT.NO:","") in ["RR1697","RR1680","RR2000","RR0680"]):
        continue
    
    strippedData.append([partialstrippedData[i+1].replace("CAT.NO:",""),componentType,partialstrippedData[i]])

for i in range(0,len(strippedData)):
    if ("Resistor" in strippedData[i][1]):
        if ("Wire Wound Resistor" in strippedData[i][2]):
            tmp = []
            tmp.append(strippedData[i][0])
            tmp.append(strippedData[i][1])
            tmp.append("Wire Wound")
            tmp.append("1")

            resSpecs = strippedData[i][2].replace(" Watt Wire Wound Resistor","").split(" Ohm ")
            tmp.append(resSpecs[0] + " Ohms")
            tmp.append(resSpecs[1] + " Watts")
            strippedData[i] = tmp
            print(strippedData[i])
        elif ("Carbon Film Resistor" in strippedData[i][2]):
            tmp = []
            tmp.append(strippedData[i][0])
            tmp.append(strippedData[i][1])
            tmp.append("Carbon Film")

            digits_only = ''.join([char for char in strippedData[i][2].split(" - ")[1] if char.isdigit()])
            tmp.append(digits_only)

            resSpecs = strippedData[i][2].split(" Watt Carbon Film ")[0].split(" Ohm ")
            tmp.append(resSpecs[0] + " Ohms")
            tmp.append(resSpecs[1] + " Watts")
            strippedData[i] = tmp
            print(strippedData[i])
        elif ("Metal Film Resistor" in strippedData[i][2]):
            tmp = []
            tmp.append(strippedData[i][0])
            tmp.append(strippedData[i][1])
            tmp.append("Metal Film")

            digits_only = ''.join([char for char in strippedData[i][2].split(" - ")[1] if char.isdigit()])
            tmp.append(digits_only)

            resSpecs = strippedData[i][2].split(" Watt Metal Film ")[0].split(" Ohm ")
            tmp.append(resSpecs[0] + " Ohms")
            tmp.append(resSpecs[1] + " Watts")
            strippedData[i] = tmp
            print(strippedData[i])
        else:
            print("UNKNOWN RESISTOR TYPE: " + str(strippedData[i]))
