import re #for regex
import json 

with open("petrol.html", "r") as file : #open the file as file
    data = file.read() #read the content in the file

pattern = r'₹(\d+\.\d{2})' #regex to match the first occurance
match = re.search(pattern, data) #try to find a match for the regex pattern

price = None
if match :
    price = match.group(1)
else :
    print("No match found")

if price :
    with open("price.json", "w") as jsn :
        jsn.write(json.dumps({"petrol_price" : int(price)}))
