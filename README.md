To use dowload and extract "video makes.zip"

Python has to be installed https://www.python.org/ (may not work on version lower than 3.9)
Has to be run in a virtual environment


	Import Instruction:

1. Place Image sequence you wish to import in the "image sequence" folder
   Frames must be images named like this: prefix (optional), frame number with fixed amount
    of digits (eg. image0001.png, image0002.png, image0003.png etc or 0001.png, 0002.png, 0003.png, )
2. Adjust desired in game resolution (doesn't have to match image sequence resolution) (optional)
   Set start frame to the index of the first frame
   Set framecount to the amount of frames aka: last frame index + 1
   Set prefix, postfix and charachtercount accordingly (eg. if your images are "image001.png"
							set prefix to "image"
							set postfix to ".png"
							set charachtercount to 3)
3.Run "video maker.py"
4. Two ways to import into game:
	A: Create a blueprint in scrap mechanic, locate folder in
           "C:\Users\[user]\AppData\Roaming\Axolot Games\Scrap Mechanic\User\User_[uuid]\Blueprints"
	   find the "blueprint.json" inside folder and replace with "blueprint.json" in the converter folder

	B: Set "path" in "setting.txt" to the path of the blueprint file before running script


	Technical Details:

The script will consider a pixel to be on, if the blue channel is above 128
