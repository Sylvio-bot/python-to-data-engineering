import json

data = '''
{
    "name" : "Herimampionona",
    "phone" : {
        "type" : "intl",
        "number" : "+261 38 81 468 91"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
#loads become a json the string
info = json.loads(data)
print('Name:',info["name"])
print('Tel:',info["phone"]["number"])
