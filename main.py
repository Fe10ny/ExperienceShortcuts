import json

import requests
from PIL import Image

# Loads settings.json file
file = open("settings.json")
settingsjson = json.load(file)


def downloadIcon(i):
    r = requests.get(f"https://thumbnails.roblox.com/v1/places/gameicons?placeIds={i}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false")
    js = r.json()
    url = js['data'][0]['imageUrl']

# Gets Universe id from Place id
def getUniverseId(i):
    r = requests.get(f"https://apis.roblox.com/universes/v1/places/{i}/universe")
    js = r.json()
    print(js)
    return js['universeId']

# Gets Experience name from Universe id
def getData(i):
    r = requests.get(f"https://games.roblox.com/v1/games?universeIds={i}")
    js = r.json()
    print(js)
    return js['data'][0]['name']


def Main():
    i = input("Experience Id: ")
    match settingsjson['nameMode']:
        case -1:
            name = input("Enter a Name for your Deep Link: ")
        case 0:
            name = i
        case 1:
            universeId = getUniverseId(i)
            name = getData(universeId)
        case default:
            print("Warning: Invalid 'nameMode' variable.\nThe Deep link name will be set to Experience Id...")
            name = i
    with open(f"{name}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        f.write(f"URL=roblox://placeId={i}")
    Main()

Main()