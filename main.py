import json
import os, sys
import re


try:
    import requests
    from PIL import Image, ImageOps
except ImportError:
    print(f"Error: One or More of Pip Packages are missing")
    input(f"Press enter to exit...")
    sys.exit()

# list of letters that cannot be used for filename
badchars = ["\\","/",":","*","?","\"","<",">","|"]

# Loads settings.json file
file = open("settings.json")
settingsjson = json.load(file)

size = (100,100)

# Downloads .jpg of Experience icon and replaces it with .ico file.
def downloadIcon(i):
    r = requests.get(f"https://thumbnails.roblox.com/v1/places/gameicons?placeIds={i}&returnPolicy=PlaceHolder&size=512x512&format=Png&isCircular=false")
    js = r.json()
    url = js['data'][0]['imageUrl']

    image = requests.get(url).content
    with open(f'icons/{i}.jpg', 'wb') as x:
        x.write(image)
        with Image.open(f'icons/{i}.jpg') as im:
            ImageOps.fit(im, size).save(f'icons/{i}.ico')
        path = os.path.abspath(f'icons/{i}.ico')
    os.remove(f'icons/{i}.jpg')
    return path

# Gets Universe id from Place id
def getUniverseId(i):
    r = requests.get(f"https://apis.roblox.com/universes/v1/places/{i}/universe")
    js = r.json()
    return js['universeId']

# Gets Experience name from Universe id
def getData(i):
    r = requests.get(f"https://games.roblox.com/v1/games?universeIds={i}")
    js = r.json()
    return js['data'][0]['name']


def Main():
    i = input("Experience Id: ")
    universeId = None
    if i.isdigit() is False:
        # Extracts Experience id from game link.
        result = re.search('games/(.*)/', i)
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
            if universeId == None:
                print("Error: Invalid Experience id")
                Main()
            name = getData(universeId)
        case default:
            print("Warning: Invalid 'nameMode' variable.\nThe Deep link name will be set to Experience Id...")
            name = i

    # Cleans String from bad characters.
    for x in badchars:
        name = name.replace(x, '')

    # Creates an Deep link file.
    with open(f"{name}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        f.write(f"URL=roblox://placeId={i}\n")
        if settingsjson["downloadExperienceIcon"]:
            icon_file = downloadIcon(i)
            f.write(f"IconFile={icon_file}\nIconIndex=0\nHotKey=0")

    Main()

Main()