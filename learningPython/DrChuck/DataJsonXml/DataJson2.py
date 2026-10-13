import json

input ='''
[
    {
        "id" : "001",
        "x" : 2,
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : 7,
        "name" : "Rr"
    }
]'''

info = json.loads(input)
print("user count:", len(info),'\n')

for item in info:
    print('Name',item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'],'\n')

print(info[0]['x'] + info[1]['x'])
