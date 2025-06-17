import json

import requests
from PIL import Image
import re

# list of letters that cannot be used for filename
badchars = ["\\","/",":","*","?","\"","<",">","|"]

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
    if i.isdigit() is False:
        # Extracts Experience id from game link.
        result = re.search('https://www.roblox.com/games/(.*)/', i)
        if result:
            print(f"Got Experience Id from Link {result.group(1)}")
            i = result.group(1)
        else:
            print("Error: Entered Experience Id is Invalid.")
            Main()
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
    test_name = name
    for x in badchars:
        test_name = test_name.replace(x, '')

    print(test_name)

    with open(f"{test_name}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        f.write(f"URL=roblox://placeId={i}")
    Main()

Main()