rawdata = []
with open("C:\\Users\\aj200\\Documents\\GitHub\\Jaycar-Scripts\\Components List\\TmpRes.txt",'r') as f:
    rawdata = f.readlines()

resultingJSON = "[\n"
x = 1
for i in range(0,len(rawdata)):
    if x%3 == 1:
        catcode = "RR" + rawdata[i][:-1]
        type = "Wire Wound"
        resistance = float(rawdata[i+1][:-1])
        wattage = float(rawdata[i+2][:-1])
        packsize = 1

        if resistance == int(resistance):
            resistance = int(resistance)
        if wattage == int(wattage):
            wattage = int(wattage)

        if wattage == 1:
            type = "Carbon Film"
            packsize = 2
        elif wattage == 0.5:
            type == "Metal Film"
            packsize = 8
        elif wattage == 0.25:
            type = "Carbon Film"
            packsize = 8
        
        json = ["\t\"catcode\": \"" + catcode + "\",",
                "\t\"type\": \"" + type + "\",",
                "\t\"resistance\": " + str(resistance) + ",",
                "\t\"wattage\": " + str(wattage) + ",",
                "\t\"packsize\": " + str(packsize)]

        msg = ""
        for i in range(0,len(json)):
            msg += "\t" + json[i] + "\n"
            if (i == len(json) - 1):
                msg = msg[:-1]
        
        if x == 1:
            msg = "\t{\n" + msg
        elif x == len(rawdata) - 2:
            msg = "\n\t},{\n" + msg + "\n\t}\n"
        else:
            msg = "\n\t},{\n" + msg
        resultingJSON += msg

        print(catcode + "\t" + str(resistance) + "\t" + str(wattage))
    x += 1
resultingJSON += "]"

with open("C:\\Users\\aj200\\Documents\\GitHub\\Jaycar-Scripts\\Components List\\Resistors.json",'w+') as f:
    f.write(resultingJSON)
    f.close()
