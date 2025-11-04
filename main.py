import json
import os
import re

# Loads settings.json file
file = open("settings.json")
settingsjson = json.load(file)

added_imports = {"requests": False, "pillow": False}

# checks if packages are missing and sets variables
try:
    import requests
    added_imports['requests'] = True
except ImportError as error:
    print(error)
    print('Warning: some features will be unusable')
    print('Note: This session\'s nameMode has been set to manual and downloadExperienceIcon to False due to "requests" package missing.')
    settingsjson['nameMode'] = -1
    settingsjson['downloadExperienceIcon'] = False
    pass

try:
    from PIL import Image, ImageOps
    added_imports['pillow'] = True
except ImportError as error:
    print(error)
    print('Warning: some features will be unusable')
    print('Note: This session\'s downloadExperienceIcon has been set to False due to "pillow" package missing.')
    settingsjson['downloadExperienceIcon'] = False
    pass


# list of symbols that cannot be used for filename
badchars = ["\\","/",":","*","?","\"","<",">","|"]

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
        x.close()
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

# Gets private server id out of "privateServerLinkCode" variable in the link.
def getPrivateServer():
    i = input("Enter your private server link/code or leave empty to cancel: ")
    if i == '':
        return ''
    if i.isdigit() is False:
        # Extracts Experience id from game link.
        result = re.search('privateServerLinkCode=(.*)#', i)
        if result:
            print(f"Got Private Server Id from Link {result.group(1)}")
            i = result.group(1)
            return i
        else:
            print("Error: Entered Experience Id is Invalid.")
            getPrivateServer()
    else:
        return ''

# returns contents for "URL=" line
def updateWriteUrl(id, PrivateID):
    send = f'roblox://place={id}'
    if PrivateID != '':
        send += f'&linkCode={PrivateID}'
    return send

def writeDeepLink(name, i, PrivateID):
    with open(f"{name}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        if PrivateID == None:
            f.write(f"URL=roblox://navigation/share_links?code={i}&type=Server")
        else:
            urlwrite = updateWriteUrl(i, PrivateID)
            f.write(f"URL={urlwrite}\n")
        if settingsjson["downloadExperienceIcon"]:
            icon_file = downloadIcon(i)
            f.write(f"IconFile={icon_file}\nIconIndex=0\nHotKey=0")
        f.close()

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
            result = re.search("\\?code=(.*)&", i)
            if result:
                print("Detected private server id")
                settingsjson['privateServer'] = False
                settingsjson['downloadExperienceIcon'] = False
                i = result.group(1)
            else:
                print("Error: Entered Experience Id is Invalid.")
                Main()
    name = "0"
    PrivateID = ''
    if i.isdigit():
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
    else:
        input_name = input("Enter a Name for your Private Server Deep Link or leave empty for default: ")
        if input_name != '':
            name = input_name
        else:
            name = i
        PrivateID = None

    if settingsjson['privateServer'] == True:
        print("Would you like to enter Private Server link/code? \n     Y - Yes      N - No")
        private_i = input("> ")
        if private_i.upper() == "Y":
            PrivateID = getPrivateServer()

    # Cleans String from bad symbols.
    for x in badchars:
        name = name.replace(x, '')

    # Creates an Deep link file.
    writeDeepLink(name, i, PrivateID)

    Main()

Main()