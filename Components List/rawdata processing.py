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
        componentType = "Resistor"
    elif "capacitor" in partialstrippedData[i].lower():
        componentType = "Capacitor"
    elif "greencap" in partialstrippedData[i].lower():
        componentType = "Capacitor"
    elif "electrolytic" in partialstrippedData[i].lower():
        componentType = "Capacitor"
    elif "mosfet" in partialstrippedData[i].lower():
        componentType = "MOSFET"
    elif "transistor" in partialstrippedData[i].lower():
        componentType = "Transistor"
    elif "voltage regulator" in partialstrippedData[i].lower():
        componentType = "Rectifier"
    elif "regulator" in partialstrippedData[i].lower():
        componentType = "Regulator"
    elif "crystal" in partialstrippedData[i].lower():
        componentType = "Crystal"
    elif "IC" in partialstrippedData[i]:
        componentType = "IC"
    elif "diode" in partialstrippedData[i].lower():
        componentType = "Diode"
    elif "SCR" in partialstrippedData[i]:
        componentType = "SCR"
    elif "socket" in partialstrippedData[i].lower():
        componentType = "Socket"
    elif "microcontroller" in partialstrippedData[i].lower():
        componentType = "IC"
    elif "sensor" in partialstrippedData[i].lower():
        componentType = "Sensor"
    elif "choke" in partialstrippedData[i].lower():
        componentType = "RF Choke"
    elif ("standoff" in partialstrippedData[i].lower()) and ("ke" in partialstrippedData[i].lower()):
        componentType = "Diode"
    elif "74h" in partialstrippedData[i].lower():
        componentType = "IC"
    elif "74l" in partialstrippedData[i].lower():
        componentType = "IC"
    elif "rectifier" in partialstrippedData[i].lower():
        componentType = "Rectifier"
    elif "triac" in partialstrippedData[i].lower():
        componentType = "Triac"
    elif "j-fet" in partialstrippedData[i].lower():
        componentType = "FET"
    elif "sleeve" in partialstrippedData[i].lower():
        continue
    elif "core" in partialstrippedData[i].lower():
        continue
    elif "ferrite" in partialstrippedData[i].lower():
        continue
    elif "coil" in partialstrippedData[i].lower():
        continue
    elif "mount" in partialstrippedData[i].lower():
        continue
    elif "silicon" in partialstrippedData[i].lower():
        continue
    elif "rubber" in partialstrippedData[i].lower():
        continue
    elif ("emi" in partialstrippedData[i].lower()) and ("filter" in partialstrippedData[i].lower()):
        continue
    elif "DIP" in partialstrippedData[i]:
        componentType = "IC"
    elif "FET" in partialstrippedData[i]:
        componentType = "FET"
    elif partialstrippedData[i+1].replace("CAT.NO:","") in ["ZK8879","ZL3974","ZK8874","ZC4069","ZC4538","ZL3482","ZC4543","ZC4056","ZZ8900","ZC4007"]:
        componentType = "IC"
    elif partialstrippedData[i+1].replace("CAT.NO:","") in ["ZT2397","ZT2452"]:
        componentType = "FET"
    elif partialstrippedData[i+1].replace("CAT.NO:","") in ["ZX7192"]:
        componentType = "DIAC"
    elif "STP16NF06" in partialstrippedData[i]:
        componentType = "MOSFET"
    elif "MBR20100CT" in partialstrippedData[i]:
        componentType = "Rectifier"
    elif "ZV1624" in partialstrippedData[i+1].replace("CAT.NO:",""):
        componentType = "Rectifier"
    
    if "smd" in partialstrippedData[i].lower():
        continue
    #if componentType.replace(" ","").replace("\n","").replace("\t","") == "":
    #    continue
    
    if (partialstrippedData[i+1].replace("CAT.NO:","") in ["ZZ8806","RE6250","RC5399","RR1697","RR1680","RR2000",
                                                           "RR0680","XB9008","XB9008","RM7190","RG5199","ZL3000",
                                                           "ZL3003","ZM9904","ZD1900"]):
        continue
    if (componentType == "         "):
        if (partialstrippedData[i+1].replace("CAT.NO:","")[0] != "Z"):
            continue
    
    strippedData.append([partialstrippedData[i+1].replace("CAT.NO:",""),componentType,partialstrippedData[i]])

resistorsData = []
capacitorsData = []
transistorsData = []
MOSFETsData = []
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
    elif ("Capacitor" in strippedData[i][1]):
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
    elif "MOSFET" in strippedData[i][1]:
        continue
    elif "FET" in strippedData[i][1]:
        continue
    elif "IC" in strippedData[i][1]:
        continue
    elif "Regulator" in strippedData[i][1]:
        continue
    elif "Transistor" in strippedData[i][1]:
        continue
    elif "Diode" in strippedData[i][1]:
        continue
    elif "Crystal" in strippedData[i][1]:
        continue
    elif "SCR" in strippedData[i][1]:
        continue
    elif "Sensor" in strippedData[i][1]:
        continue
    elif "Socket" in strippedData[i][1]:
        continue
    elif "Rectifier" in strippedData[i][1]:
        continue
    elif "RF Choke" in strippedData[i][1]:
        continue
    elif "Triac" in strippedData[i][1]:
        continue
    elif "DIAC" in strippedData[i][1]:
        continue
    else:
        if (("RL6404" not in strippedData[i]) and ("RL6426" not in strippedData[i])):
            print("Unknown component: " + str(strippedData[i]))

capacitorsData.append(["RL6404","Capacitor","Low Leakage Electrolytic","1","150nF", "50"])
capacitorsData.append(["RL6426","Capacitor","Low Leakage Electrolytic","1","6.8uF", "35"])






arr = resistorsData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Component type\":\"" + arr[i][2] + "\"," + endline
    msg += "\"Pack size\":\"" + arr[i][3] + "\"," + endline
    msg += "\"Resistance\":\"" + arr[i][4] + "\"," + endline
    msg += "\"Wattage\":\"" + arr[i][5] + "\""
msg += "\n\t}\n]"
with open("Resistors.json",'w+') as f:
    f.write(msg)

arr = capacitorsData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Component type\":\"" + arr[i][2] + "\"," + endline
    msg += "\"Pack size\":\"" + arr[i][3] + "\"," + endline
    msg += "\"Capacitance\":\"" + arr[i][4] + "\"," + endline
    msg += "\"Voltage\":\"" + arr[i][5] + "\""
msg += "\n\t}\n]"
with open("Capacitors.json",'w+') as f:
    f.write(msg)








