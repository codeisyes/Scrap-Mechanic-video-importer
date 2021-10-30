import json

settings = {"path":"your blueprint file path",
            "xres":20,
            "yres":15,
            "startframe":0,
            "framecount":1,
            "prefix":"Image",
            "postfix":".png",
            "charachtercount":4,
            "folder":"bob",
            "layers":27}

path = "settings.txt"


def loadsettings():
    global settings

    my_file = open(path)

    contents = my_file.read()

    settings = json.loads(contents)

    my_file.close()


def savesettings():
    global settings

    contents = json.dumps(settings)

    my_file = open(path, mode="w")

    my_file.write(contents)

    my_file.close()


def getvalue(key):
    print("value for key: '" + str(key) + "' is: '" + str(settings[key]) + "'")
    return settings[key]

def main():
    print("main")

if __name__ == "__main__":
    print("save settings")
    savesettings()