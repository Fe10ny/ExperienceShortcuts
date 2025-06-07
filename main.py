def Main():
    i = input("Experience Id:")

    with open(f"{int(i)}.url", "w") as f:
        f.write("[InternetShortcut]\nIDList=\n")
        f.write(f"URL=roblox://placeId={i}")
    Main()

Main()