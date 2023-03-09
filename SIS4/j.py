import json

# Load the JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Print the header
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
""")
# print the required atributes
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print('{:<51}{:<22}{:<9}{}'.format(imdata[i][j]["dn"], imdata[i][j]["descr"], imdata[i][j]["speed"], imdata[i][j]["mtu"]))