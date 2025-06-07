import requests

# Gets Universe id from Place id
def getUniverseId(i):
    r = requests.get(f"https://apis.roblox.com/universes/v1/places/{i}/universe")
    js = r.json()
    print(js)
    return js['universeId']

# Gets Place name from Place id
def getData(i):
    r = requests.get(f"https://games.roblox.com/v1/games?universeIds={i}")
    js = r.json()
    print(js)
    return js['data'][0]['name']

def Main():
    i = input("Experience Id:")
    universeId = getUniverseId(i)
    name = getData(universeId)
    with open(f"{name}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        f.write(f"URL=roblox://placeId={i}")
    Main()

Main()