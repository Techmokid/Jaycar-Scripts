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
    if (partialstrippedData[i+1].replace("CAT.NO:","") in ["RE6250","RC5399","RR1697","RR1680","RR2000","RR0680","XB9008","XB9008","RM7190","RG5199"]):
        continue
    
    strippedData.append([partialstrippedData[i+1].replace("CAT.NO:",""),componentType,partialstrippedData[i]])

resistorsData = []
capacitorsData = []
for i in range(0,len(strippedData)):
    if ("Resistor" in strippedData[i][1]):
        tmp = []
        tmp.append(strippedData[i][0])
        tmp.append(strippedData[i][1])
        
        if ("Wire Wound Resistor" in strippedData[i][2]):
            tmp.append("Wire Wound")
            tmp.append("1")

            resSpecs = strippedData[i][2].replace(" Watt Wire Wound Resistor","").split(" Ohm ")
            tmp.append(resSpecs[0])
            tmp.append(resSpecs[1])
        elif ("Carbon Film Resistor" in strippedData[i][2]):
            tmp.append("Carbon Film")

            digits_only = ''.join([char for char in strippedData[i][2].split(" - ")[1] if char.isdigit()])
            tmp.append(digits_only)

            resSpecs = strippedData[i][2].split(" Watt Carbon Film ")[0].split(" Ohm ")
            tmp.append(resSpecs[0])
            tmp.append(resSpecs[1])
        elif ("Metal Film Resistor" in strippedData[i][2]):
            tmp.append("Metal Film")

            digits_only = ''.join([char for char in strippedData[i][2].split(" - ")[1] if char.isdigit()])
            tmp.append(digits_only)

            resSpecs = strippedData[i][2].split(" Watt Metal Film ")[0].split(" Ohm ")
            tmp.append(resSpecs[0])
            tmp.append(resSpecs[1])
        else:
            print("UNKNOWN RESISTOR TYPE: " + str(strippedData[i]))
            continue

        if (tmp[4] != tmp[4].replace("k","")):
            val = tmp[4].replace("k","")
            val = str(float(val)*1000).split(".")[0]
            tmp[4] = val
        strippedData[i] = tmp
        resistorsData.append(strippedData[i])
        #print(strippedData[i])
    if ("Capacitor" in strippedData[i][1]):
        #print(strippedData[i])

        tmp = []
        tmp.append(strippedData[i][0])
        tmp.append(strippedData[i][1])
        if ("Polyester" in strippedData[i][2]):
            tmp.append("MKT Polyester")
        elif ("Greencap" in strippedData[i][2]):
            tmp.append("Greencap")
        elif ("Metallised Polypropylene" in strippedData[i][2]):
            tmp.append("Polyprop")
        elif("Tantalum" in strippedData[i][2]):
            tmp.append("Tantalum")
        elif("Monolithic" in strippedData[i][2]):
            tmp.append("Monolithic")
        elif("Electrolytic Crossover" in strippedData[i][2]):
            tmp.append("Crossover")
        elif("Electrolytic RB" in strippedData[i][2]):
            tmp.append("Electrolytic RB")
        elif("Bipolar" in strippedData[i][2]):
            tmp.append("Bipolar Electrolytic")
        elif("Low Leakage Electrolytic" in strippedData[i][2]):
            tmp.append("Low Leakage Electrolytic")
        elif("Low ESR Electrolytic" in strippedData[i][2]):
            tmp.append("Low ESR Electrolytic")
        elif("Electrolytic" in strippedData[i][2]):
            tmp.append("Electrolytic")
        elif("Ceramic" in strippedData[i][2]):
            tmp.append("Ceramic")
        elif("Super Capacitor" in strippedData[i][2]):
            tmp.append("Super Capacitor")

        if (len(strippedData[i][2].split(" - Pack of ")) == 1):
            tmp.append("1")
        else:
            tmp.append(strippedData[i][2].split(" - Pack of ")[1])

        if (strippedData[i][0] == "RG5181"):
            tmp.append("4.7uF")
            tmp.append("100v")
        else:
            tmp.append(strippedData[i][2].split(" ")[0])
            tmp.append(strippedData[i][2].split(" ")[1])
        tmp[5] = tmp[5].replace("k","000")
        tmp[5] = ''.join([char for char in tmp[5] if char.isdigit()])
        
        strippedData[i] = tmp
        capacitorsData.append(tmp)
        #print(str(tmp) + "\t\t\t\t" + str(strippedData[i]))
        #print()

print(capacitorsData)

