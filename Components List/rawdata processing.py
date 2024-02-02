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
    elif "regulator" in partialstrippedData[i].lower():
        componentType = "Regulator"
    elif "crystal" in partialstrippedData[i].lower():
        componentType = "Crystal"
    elif "socket" in partialstrippedData[i].lower():
        continue
    elif "IC" in partialstrippedData[i]:
        componentType = "IC"
    elif "diode" in partialstrippedData[i].lower():
        componentType = "Diode"
    elif "SCR" in partialstrippedData[i]:
        componentType = "SCR"
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
FETsData = []
ICsData = []
regulatorsData = []
diodesData = []
crystalsData = []
rectifiersData = []
chokesData = []
triacsData = []
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
        if strippedData[i][0] == "ZK8821":
            continue
        
        tmp = [strippedData[i][0],strippedData[i][1]]
        componentType = ""
        if "n-ch" in strippedData[i][2].lower():
            componentType = "N-Channel"
        elif "p-ch" in strippedData[i][2].lower():
            componentType = "P-Channel"
        elif strippedData[i][0] in ["ZT2466","ZT2277"]:
            componentType = "N-Channel"
        tmp.append(componentType)

        if strippedData[i][0] == "ZT2467":
            tmp.append(100) #Volts
            tmp.append(23)  #Amps
            tmp.append(140)  #Watts
        elif strippedData[i][0] == "ZT2450":
            tmp.append(60)
            tmp.append(60)
            tmp.append(110)
        elif strippedData[i][0] == "ZT2277":
            tmp.append(60)
            tmp.append(16)
            tmp.append(45)
        elif strippedData[i][0] == "ZT2466":
            tmp.append(100)
            tmp.append(33)
            tmp.append(130)
        elif strippedData[i][0] == "ZT2468":
            tmp.append(55)
            tmp.append(169)
            tmp.append(330)
        elif strippedData[i][0] == "ZT2464":
            tmp.append(60)
            tmp.append(53)
            tmp.append(104)
        elif strippedData[i][0] == "ZT2460":
            tmp.append(160)
            tmp.append(7)
            tmp.append(100)
        strippedData[i] = tmp
        FETsData.append(tmp)
    elif "FET" in strippedData[i][1]:
        if strippedData[i][0] == "ZT2397":
            continue
        
        tmp = [strippedData[i][0],"FET","N-Channel"]
        if "J-FET" in strippedData[i][2]:
            tmp[1] = "JFET"
        
        if strippedData[i][0] == "ZT2400":
            tmp.append(60) #Volts
            tmp.append(0.2)  #Amps
            tmp.append(0.4)  #Watts
        elif strippedData[i][0] == "ZT2262":
            tmp.append(25) #Volts
            tmp.append(0.01)  #Amps
            tmp.append(0.35)  #Watts
        elif strippedData[i][0] == "ZT2225":
            tmp.append(50) #Volts
            tmp.append(14)  #Amps
            tmp.append(40)  #Watts
        elif strippedData[i][0] == "ZT2266":
            tmp.append(25) #Volts
            tmp.append(0.01)  #Amps
            tmp.append(0.31)  #Watts
        elif strippedData[i][0] == "ZT2375":
            tmp.append(25) #Volts
            tmp.append(0.01)  #Amps
            tmp.append(0.31)  #Watts
        elif strippedData[i][0] == "ZT2452":
            tmp.append(60) #Volts
            tmp.append(1)  #Amps
            tmp.append(0.9)  #Watts
        strippedData[i] = tmp
        FETsData.append(tmp)
    elif "IC" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        if "microcontroller" in strippedData[i][2].lower():
            tmp.append("Microcontroller")
        elif "atmega" in strippedData[i][2].lower():
            tmp.append("Microcontroller")
        elif "attiny" in strippedData[i][2].lower():
            tmp.append("Microcontroller")
        elif "74l" == strippedData[i][2][:3].lower():
            tmp.append("Logic IC")
        elif "74h" == strippedData[i][2][:3].lower():
            tmp.append("Logic IC")
        elif (strippedData[i][1] == "IC") and ("gate" in strippedData[i][2].lower()):
            tmp.append("Logic IC")
        elif (strippedData[i][0] == "ZC4025"):
            tmp.append("Logic IC")
            strippedData[i][2] = strippedData[i][2].replace("Gare","Gate")
        elif "eprom" in strippedData[i][2].lower():
            tmp.append("Memory IC")
        elif "memory" in strippedData[i][2].lower():
            tmp.append("Memory IC")
        elif "opamp" in strippedData[i][2].lower():
            tmp.append("Amplifier")
        elif "op-amp" in strippedData[i][2].lower():
            tmp.append("Amplifier")
        elif "amplifier" in strippedData[i][2].lower():
            tmp.append("Amplifier")
        elif "audio amp" in strippedData[i][2].lower():
            tmp.append("Amplifier")
        elif "buffer" in strippedData[i][2].lower():
            tmp.append("Buffer")
        elif "multiplexer" in strippedData[i][2].lower():
            tmp.append("Multiplexer")
        elif "shift" in strippedData[i][2].lower():
            tmp.append("Shift Register")
        else:
            tmp.append("Other")
        tmp.append(strippedData[i][2])
        ICsData.append(tmp)
    elif "Regulator" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        if strippedData[i][2][:2] == "78":
            tmp.append("78xx VReg")
            if strippedData[i][2][2:3] == "L":
                #Here we have a 78Lxx series
                tmp.append(str(int(strippedData[i][2][3:6])))
                tmp.append("0.1")
            else:
                #Here we have a 78xx series
                tmp.append(str(int(strippedData[i][2][2:5])))
                tmp.append("1")
        elif strippedData[i][2][:2] == "79":
            tmp.append("79xx VReg")
            if strippedData[i][2][2:3] == "L":
                #Here we have a 78Lxx series
                tmp.append("-"+str(int(strippedData[i][2][3:6])))
                tmp.append("0.1")
            else:
                #Here we have a 78xx series
                tmp.append("-"+str(int(strippedData[i][2][2:5])))
                tmp.append("1")
        elif "low" in strippedData[i][2].lower():
            tmp.append("Low Voltage Dropout")
            tmp.append("12")
            tmp.append("1")
            if (strippedData[i][0] == "ZV1560"):
                tmp[3] = "5"
            elif (strippedData[i][0] == "ZV1565"):
                tmp[3] = "3.3"
            elif (strippedData[i][0] == "ZV1564"):
                tmp[4] = "3"
        elif "adj" in strippedData[i][2].lower():
            tmp.append("Adjustable Voltage Regulator")
            tmp.append("")
            tmp.append("")
        elif "voltage regulator" in strippedData[i][2].lower():
            tmp.append("Voltage Regulator")
            tmp.append("")
            tmp.append("")
        elif "boost regulator" in strippedData[i][2].lower():
            tmp.append("Boost Regulator")
            tmp.append("")
            tmp.append("")
        else:
            print("UNKNOWN  VREG: " + strippedData[i][2])
            continue
        tmp.append(strippedData[i][2])
        regulatorsData.append(tmp)
    elif "Transistor" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        if "pack" in strippedData[i][2].lower():
            continue
        elif "NPN" in strippedData[i][2]:
            tmp.append("NPN")
            strippedData[i][2] = strippedData[i][2].replace("NPN","").replace("Transistor","")
        elif "PNP" in strippedData[i][2]:
            tmp.append("PNP")
            strippedData[i][2] = strippedData[i][2].replace("PNP","").replace("Transistor","")
        else:
            continue
        if (strippedData[i][2][0] == " "):
            strippedData[i][2] = strippedData[i][2][1:]
        strippedData[i][2] = strippedData[i][2].replace("\t"," ").split(" ")[0]
        tmp.append(strippedData[i][2])
        transistorsData.append(tmp)
    elif "Diode" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]

        if "zener" in strippedData[i][2].lower():
            tmp.append("Zener")
            vals = strippedData[i][2].split(" ")
            tmp.append(vals[1])
            tmp.append(vals[0].replace("V",""))
            tmp.append(vals[2])
        elif "schottky" in strippedData[i][2].lower():
            tmp.append("Schottky")
            if strippedData[i][0] == "ZR1141":
                tmp.append("BAT46/BAT48")
                tmp.append("100")
                tmp.append("0.15")
            else:
                tmp.append(strippedData[i][2].replace("Diode ","").split(" ")[0])

                voltage = None
                amps = None
                for x in strippedData[i][2].split(" "):
                    if x[-1] == "V":
                        voltage = x[:-1]
                    if x[-1] == "A":
                        amps = x[:-1]
                if not voltage:
                    voltage = "70"
                    amps = "0.015"
                tmp.append(voltage)
                tmp.append(amps)
        elif "fast" in strippedData[i][2].lower():
            tmp.append("Fast")
            tmp.append(strippedData[i][2].split(" ")[0])
            if strippedData[i][0] == "ZR1034":
                tmp.append("200")
                tmp.append("1")
            elif strippedData[i][0] == "ZR1028":
                tmp.append("150")
                tmp.append("8")
        else:
            tmp.append("Standard")
            strippedData[i][2] = strippedData[i][2].replace("Diode ","").replace("DIODE ","")
            if strippedData[i][0] in ["ZR1005","ZD1955"]:
                continue
            
            if strippedData[i][0] in ["ZR1105","ZR1100"]:
                tmp.append("1N914/1N4148")
                tmp.append("100")
                tmp.append("0.45")
            elif "P4KE" in strippedData[i][2]:
                tmp[2] = "TVS - P4KE"
                vals = strippedData[i][2].split(" ")
                tmp.append(vals[1].replace("V",""))
                tmp.append(vals[2].replace("A","").replace("C",""))
                tmp.append("400")
                tmp.append(vals[5])
            elif "1.5KE" in strippedData[i][2]:
                tmp[2] = "TVS - 1.5KE"
                vals = strippedData[i][2].split(" ")
                tmp.append(vals[1].replace("V",""))
                tmp.append(vals[2].replace("A","").replace("C",""))
                tmp.append("1500")
                tmp.append(vals[5])
            else:
                vals = strippedData[i][2].split(" ")
                tmp.append(vals[0])
                voltage = None
                amps = None
                for x in vals:
                    if x[-1] == "V":
                        voltage = x[:-1]
                    if x[-1] == "A":
                        amps = x[:-1]
                tmp.append(voltage)
                tmp.append(amps)
        diodesData.append(tmp)
    elif "Crystal" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        if "R/C Crystal TX/RX Pair " in strippedData[i][2]:
            tmp.append(strippedData[i][2].replace("R/C Crystal TX/RX Pair ",""))
        else:
            val = strippedData[i][2].replace("Crystal","").replace("CRYSTAL","").replace("38k","38KHz").replace("kHz","KHz")
            if val[0] == " ":
                val = val[1:]
            if "ATMEGA328P" in val:
                continue
            tmp.append(val.split(" ")[0])
        crystalsData.append(tmp)
    elif "SCR" in strippedData[i][1]:
        #print(strippedData[i][2])
        continue
    elif "Sensor" in strippedData[i][1]:
        #print(strippedData[i][2])
        continue
    elif "Socket" in strippedData[i][1]:
        continue
    elif "Rectifier" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        if ("Bridge" in strippedData[i][2]) or ("ZR1362" == strippedData[i][0]):
            tmp.append("Bridge")
            vals = strippedData[i][2].split(" ")
            voltage = None
            amps = None
            for x in vals:
                if x[-1] == "V":
                    voltage = x[:-1]
                if x[-1] == "A":
                    amps = x[:-1]
            tmp.append(voltage)
            tmp.append(amps)
        elif "ZV1624" == strippedData[i][0]:
            continue
        elif "ZR1039" == strippedData[i][0]:
            continue
        rectifiersData.append(tmp)
    elif "RF Choke" in strippedData[i][1]:
        if "Chokes" in strippedData[i][2]:
            continue
        strippedData[i][2] = strippedData[i][2].split(" ")[0]
        chokesData.append(strippedData[i])
    elif "Triac" in strippedData[i][1]:
        tmp = [strippedData[i][0],strippedData[i][1]]
        vals = strippedData[i][2].split(" ")
        tmp.append(vals[0])
        tmp.append(vals[1].replace("V",""))
        tmp.append(vals[2].replace("A",""))
        triacsData.append(tmp)
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

arr = transistorsData
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
    msg += "\"Transistor identifier\":\"" + arr[i][3] + "\""
msg += "\n\t}\n]"
with open("Transistors.json",'w+') as f:
    f.write(msg)

arr = FETsData
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
    msg += "\"Volts\":\"" + str(arr[i][3]) + "\"," + endline
    msg += "\"Amps\":\"" + str(arr[i][4]) + "\"," + endline
    msg += "\"Watts\":\"" + str(arr[i][5]) + "\""
msg += "\n\t}\n]"
with open("FETs.json",'w+') as f:
    f.write(msg)

arr = ICsData
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
    msg += "\"Description\":\"" + str(arr[i][3]) + "\""
msg += "\n\t}\n]"
with open("ICs.json",'w+') as f:
    f.write(msg)

arr = regulatorsData
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
    msg += "\"Volts\":\"" + str(arr[i][3]) + "\"," + endline
    msg += "\"Amps\":\"" + str(arr[i][4]) + "\"," + endline
    msg += "\"Description\":\"" + str(arr[i][5]) + "\""
msg += "\n\t}\n]"
with open("Regulators.json",'w+') as f:
    f.write(msg)

arr = diodesData
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
    if "TVS" in arr[i][2]:
        msg += "\"Volts\":\"" + str(arr[i][3]) + "\"," + endline
        msg += "\"Amps\":\"" + str(arr[i][4]) + "\"," + endline
        msg += "\"Watts\":\"" + str(arr[i][5]) + "\"," + endline
        msg += "\"AC/DC\":\"" + str(arr[i][6]) + "\""
    else:
        msg += "\"Diode Identifier\":\"" + str(arr[i][3]) + "\"," + endline
        msg += "\"Volts\":\"" + str(arr[i][4]) + "\"," + endline
        msg += "\"Amps\":\"" + str(arr[i][5]) + "\""
msg += "\n\t}\n]"
with open("Diodes.json",'w+') as f:
    f.write(msg)

arr = crystalsData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Frequency\":\"" + str(arr[i][2]) + "\""
msg += "\n\t}\n]"
with open("Crystals.json",'w+') as f:
    f.write(msg)

arr = rectifiersData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Component Type\":\"" + arr[i][2] + "\"," + endline
    msg += "\"Volts\":\"" + arr[i][3] + "\"," + endline
    msg += "\"Amps\":\"" + arr[i][4] + "\""
msg += "\n\t}\n]"
with open("Rectifiers.json",'w+') as f:
    f.write(msg)

arr = chokesData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Impedance\":\"" + str(arr[i][2]) + "\""
msg += "\n\t}\n]"
with open("RF Chokes.json",'w+') as f:
    f.write(msg)

arr = triacsData
msg = "["
for i in range(0,len(arr)):
    if (i == 0):
        msg += "\n\t{\n\t\t"
    else:
        msg += "\n\t},{\n\t\t"
    endline = "\n\t\t"

    msg += "\"Cat code\":\"" + arr[i][0] + "\"," + endline
    msg += "\"Component\":\"" + arr[i][1] + "\"," + endline
    msg += "\"Component Identifier\":\"" + arr[i][2] + "\"," + endline
    msg += "\"Volts\":\"" + arr[i][3] + "\"," + endline
    msg += "\"Amps\":\"" + arr[i][4] + "\""
msg += "\n\t}\n]"
with open("Triacs.json",'w+') as f:
    f.write(msg)



