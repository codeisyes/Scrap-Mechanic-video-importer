from PIL import Image
import downscale
import json
import math
import settingsloader

settingsloader.loadsettings()

path = "C:/Users/inven/AppData/Roaming/Axolot Games/Scrap Mechanic/User/User_76561198800807534/Blueprints/f9a1780f-6abf-4a0f-9400-085c18038de0/blueprint.json"
path = settingsloader.getvalue("path")

my_file = open(path)

contents = my_file.read()

contentsdict = json.loads(contents)

blockidcount = 0

# config

xres = settingsloader.getvalue("xres")

yres = settingsloader.getvalue("yres")

frame = settingsloader.getvalue("startframe")
frames = settingsloader.getvalue("framecount")

prefix = settingsloader.getvalue("prefix")

postfix = settingsloader.getvalue("postfix")

namecharachters = settingsloader.getvalue("charachtercount")

folder = settingsloader.getvalue("folder")

layercount = int(math.ceil((frames - frame) / 250))


contentsdict["bodies"][0]["childs"] = []


def makelayer(blockdic, xlen, ylen, ypos):
    global blockidcount
    y = 0
    while y < ylen:
        x = 0
        while x < xlen:
            contentsdict["bodies"][0]["childs"].append({'color': '000000',
                                                        'controller': {'active': False, 'controllers': None,
                                                                       'id': blockidcount, 'joints': None, 'mode': 1},
                                                        'pos': {'x': x, 'y': ypos, 'z': y},
                                                        'shapeId': '9f0f56e8-2c31-4d83-996c-d00a9b296c3f', 'xaxis': 3,
                                                        'zaxis': 1})
            print(blockidcount)
            print(str(x) + " " + str(y) + " " + str(ypos))
            blockdic[str(x) + " " + str(y)] = blockidcount
            x += 1
            blockidcount += 1
        y += 1

# making layers
print("creating layers...")
layers = []
i = 0
while i < layercount:  # should be 27
    layers.append({})
    makelayer(layers[i], xres, yres, min(i, 1))
    i += 1
print(layers)
print("done")

# connect leyers to screen leyer
print("connecting layers to screen...")
for screenblock in contentsdict["bodies"][0]["childs"]:
    if screenblock["pos"]["y"] == 0:  # found screen block
        for block in contentsdict["bodies"][0]["childs"]:
            if (block["pos"]["x"] == screenblock["pos"]["x"]) & (block["pos"]["z"] == screenblock["pos"]["z"]) & (
                    block["pos"]["y"] != 0):  # found block in layer behind
                block["controller"]["controllers"] = []
                block["controller"]["controllers"].append({"id": screenblock["controller"]["id"]})
print("done")
# connect pixels
# frame = 0
# frames = 5000 #6514
# prefix = "Image"
# postfix = ".png"
# namecharachters = 4
# folder = "bob"

print("connecting pixels...")
firsttimelineblock = blockidcount
while frame < frames:
    im = Image.open(folder + "/" + prefix + ("0" * (namecharachters - len(str(frame)))) + str(frame) + postfix)
    y = 0
    # create block for this frame
    contentsdict["bodies"][0]["childs"].append({'color': '222222',
                                                'controller': {'active': False, 'controllers': None, 'id': blockidcount,
                                                               'joints': None, 'mode': 1},
                                                'pos': {'x': -1, 'y': (min(frame, 1)), 'z': 0},
                                                'shapeId': '9f0f56e8-2c31-4d83-996c-d00a9b296c3f', 'xaxis': 3,
                                                'zaxis': 1})
    blockidcount += 1
    contentsdict["bodies"][0]["childs"][len(contentsdict["bodies"][0]["childs"]) - 1]["controller"]["controllers"] = []
    if not (frame == frames - 1):
        contentsdict["bodies"][0]["childs"][len(contentsdict["bodies"][0]["childs"]) - 1]["controller"][
            "controllers"].append({"id": blockidcount})
    print(contentsdict["bodies"][0]["childs"][len(contentsdict["bodies"][0]["childs"]) - 1]["controller"])
    while y < yres:
        x = 0
        while x < xres:
            scalingfactor = (
                (
                        (im.size[0] - 1) / (xres - 1)
                ),
                (
                        (im.size[1] - 1) / (yres - 1)
                )
            )

            if downscale.getpixel(
                    im.getdata(),
                    x * scalingfactor[0],
                    (im.size[1] - 1) - (y * scalingfactor[1]),
                    im.size[1],
                    im.size[0],
            )[2] > 128:
                print("On frame " + str(frame) + " connect x: " + str(x) + " y: " + str(y) + " to layer: " + str(
                    int(math.floor(frame / 250))))
                contentsdict["bodies"][0]["childs"][len(contentsdict["bodies"][0]["childs"]) - 1]["controller"][
                    "controllers"].append({"id": layers[int(math.floor(frame / 250))][str(x) + " " + str(y)]})
            x += 1
        y += 1
    frame += 1
print("done")

print("finishing up")
# adding start logic
contentsdict["bodies"][0]["childs"].append({'color': '222222',
                                            'controller': {'active': False, 'controllers': [{"id": blockidcount + 1}],
                                                           'id': blockidcount, 'joints': None, 'mode': 4},
                                            'pos': {'x': -1, 'y': 0, 'z': 2},
                                            'shapeId': '9f0f56e8-2c31-4d83-996c-d00a9b296c3f', 'xaxis': 3, 'zaxis': 1})
blockidcount += 1
contentsdict["bodies"][0]["childs"].append({'color': '222222',
                                            'controller': {'active': False, 'controllers': [{'id': firsttimelineblock}],
                                                           'id': blockidcount, 'joints': None, 'mode': 0},
                                            'pos': {'x': -1, 'y': 0, 'z': 1},
                                            'shapeId': '9f0f56e8-2c31-4d83-996c-d00a9b296c3f', 'xaxis': 3, 'zaxis': 1})
blockidcount += 1
contentsdict["bodies"][0]["childs"].append({'color': '00ff00', 'controller': {'active': False,
                                                                              'controllers': [{'id': blockidcount - 2},
                                                                                              {'id': blockidcount - 1}],
                                                                              'id': blockidcount, 'joints': None, },
                                            'pos': {'x': -1, 'y': -1, 'z': 1},
                                            'shapeId': '1e8d93a4-506b-470d-9ada-9c0a321e2db5', 'xaxis': 3, 'zaxis': 1})
blockidcount += 1

print("wrinting to file")
# writing file
if True:
    my_file.close()

    contents = json.dumps(contentsdict)

    my_file = open(path, mode="w")

    my_file.write(contents)

    my_file.close()

print("blueprint successfully modified")