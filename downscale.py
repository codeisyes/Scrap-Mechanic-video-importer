from PIL import Image
import numpy

targetwidth = 15
targetheight = 20


def getpixel(data, x, y, ylen, xlen):
    x = round(x)
    y = round(y)
    return data[int((y * xlen) + x)]

def imagedowsample(image, tagetwidth, targetheight):
    # doesent work
    pixels = []
    x = 0
    y = 0
    while y <= image.size[0]:
        row = []
        while x <= image.size[1]:
            row.append(getpixel(image.getdata(), x * (image.size[0] / tagetwidth), y * (image.size[1] / targetheight), image.size[0], image.size[1]))
            x += 1
        pixels.append(numpy.array(row))
        y += 1
    array = numpy.array(pixels)
    print(array[0][0][3].__class__)
    myimage = Image.fromarray(array)
    return myimage

def main():
    im = Image.open("bob/Image0000.png")
    data = im.getdata()
    print(getpixel(data, 6.0, 14.0, im.size[1], im.size[0]))

if __name__ == "__main__":
    main()


