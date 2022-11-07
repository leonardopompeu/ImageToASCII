from PIL import Image, ImageDraw, ImageFont
import math

img = Image.open('eu2.jpg')

scaleFactor = 0.1

oneCharWidth = 8
oneCharHeight = 18

width, height = img.size
img = img.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = img.size
pix = img.load()

#chars = "$@B$8&WM#*oahkbdpqwmZO0QLCJUYXzcvunrxjft/\\|()1{}[]?-_+~<>i!1I;:,\"^`'. "[::-1]
chars = '#Wo- '[::-1]
charArray = list(chars)
charLenght = len(charArray)
interval = charLenght/256

fnt = ImageFont.truetype('/home/leobp/.fonts/Roboto-Regular.ttf', 15)

text_file = open("Output.txt", "w")

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

print(width, height)

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3) # MAKE GRAYSCALE
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight), getChar(h), font=fnt, fill=(r,g,b))

    text_file.write('\n')

#img.save('output.jpg') # TEST GRAYSCALE
outputImage.save('output.jpg')