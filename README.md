# ExperienceShortcuts
Simple script for roblox shortcuts/deep links creation.
# How to use
1. Download [Zip File](https://github.com/Fe10ny/ExperienceShortcuts/releases/latest) from Releases Tab and extract it.
2. Start main.py and enter your Experience id or Experience Link (e.g. 47324)
3. Enter a Name for new Deep link if prompted.
4. The script will create a Deep link in the same folder as main.py is.
5. Open Deep link file.
# How to get private server id
## Auto method (Recommended):
1. Open script
2. Generate a new private server link (e.g. `https://www.roblox.com/share?code=60434bbd0fe2db8810d2cec4c2829f44&type=Server`)
3. Copy it and paste it instead of Experience id.
4. Done.
## Manual method:
1. Open Script
2. Generate a new private server link (e.g. `https://www.roblox.com/share?code=ca1899def65902ad6279356efc83d0e0&type=Server`)
3. Open newly Generated link in your browser.
4. The browser will replace link with new one containing: `?privateServerLinkCode=`
5. Proceed with script until it asks for Private server id/link (Requires "privateServer" setting to be set to true)
6. Enter private server id/link from 4th step (e.g. `12345` or `https://www.roblox.com/games/47324/Experience-Name?privateServerLinkCode=12345#!/game-instances`)
7. Done.
# Settings
Available variables and modes in settings.json file:
- nameMode - Sets Deep link's Name based on selected mode.
- - -1 - Enter Deep link's name Manually.
- - 0 - Set Experience Id as the Deep link name.
- - 1 - Set Experience's name as the Deep link name. (Requires request package)
- privateServer - Prompt for private server id
- - true - Asks for private server id
- - false - Dont ask for private server id
- downloadExperienceIcon - Downloads Experience's icon and applies onto Deep link. (Requires pillow and requests package)
- - true - Enable Experience Icon Downloading. 
- - false - Disable Experience Icon Downloading.
# Requirements
- Python version 3.12.4
- requests~=2.32.3 (Optional)
- pillow~=11.2.1 (Optional)