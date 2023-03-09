import json

# Load the JSON file
with open("sample-data.json", "r") as file:
    data = json.load(file)

# Print the header
print('Interface Status')
print('='*80)
print("DN", " " * 40, "Description"," " * 10, "Speed  ", "  MTU")
print('-'*80)

# print the required atributes
for imdata in data["imdata"]:
    for i in imdata:
        for j in imdata[i]:
            print('{:<51}{:<15}{:<10}{}'.format(imdata[i][j]["dn"], imdata[i][j]["descr"], imdata[i][j]["speed"], imdata[i][j]["mtu"]))