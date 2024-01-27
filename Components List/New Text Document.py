rawdata = []
with open("New Text Document.txt",'r') as f:
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

    if "smd" in partialstrippedData[i].lower():
        continue
    if componentType.replace(" ","").replace("\n","").replace("\t","") == "":
        continue
    
    strippedData.append([partialstrippedData[i],componentType,partialstrippedData[i+1].replace("CAT.NO:","")])
print(strippedData)
