# ExperienceShortcuts
Simple script for roblox shortcuts/deep links creation.
# How to use
1. Download [Zip File](https://github.com/Fe10ny/ExperienceShortcuts/releases/latest) from Releases Tab and extract it.
2. Start main.py and enter your Experience id or Experience Link (e.g. 47324)
3. Enter a Name for new Deep link if needed.
4. The script will create a Deep link in the same folder as main.py is.
5. Open Deep link file.
# Settings
Available variables and modes in settings.json file:
- nameMode - Sets Deep link's Name based on selected mode.
- - -1 - Enter Deep link's name Manually.
- - 0 - Set Experience Id as the Deep link name.
- - 1 - Set Experience's name as the Deep link name.
- downloadExperienceIcon - Downloads Experience's icon and applies onto Deep link.
- - true - Enable Experience Icon Downloading.
- - false - Disable Experience Icon Downloading.
# Requirements
- Python version 3.12.4
- requests~=2.32.3
- pillow~=11.2.1