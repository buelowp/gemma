import board, neopixel, time, random
numpix = 12
myRed = (0xFF, 0x00, 0x00)
myYellow = (0xFF, 0xFF, 0x00)
myWhite = (0xFF, 0xFF, 0xFF)
pattern = 0
blinks = 30

pixels = neopixel.NeoPixel(board.D1, numpix)

def twinklePixel(colorIn, pixel, steps):
    colorOut = (0xFF, 0xFF, 0xFF)
    
    if pixel >= numpix:
        return
    
    for i in range(1, steps + 1):
        r = ((colorIn[0] * (steps - i)) + (colorOut[0] * i)) / steps
        g = ((colorIn[1] * (steps - i)) + (colorOut[1] * i)) / steps
        b = ((colorIn[2] * (steps - i)) + (colorOut[2] * i)) / steps

        pixels[pixel] = (int(r), int(g), int(b))
        pixels.show()
        
    for i in range(1, steps + 1):
        r = ((colorOut[0] * (steps - i)) + (colorIn[0] * i)) / steps
        g = ((colorOut[1] * (steps - i)) + (colorIn[1] * i)) / steps
        b = ((colorOut[2] * (steps - i)) + (colorIn[2] * i)) / steps

        pixels[pixel] = (int(r), int(g), int(b))
        pixels.show()

def fadeColors(colorIn, colorOut, steps, interval):
    for i in range(1, steps + 1):
        r = ((colorIn[0] * (steps - i)) + (colorOut[0] * i)) / steps
        g = ((colorIn[1] * (steps - i)) + (colorOut[1] * i)) / steps
        b = ((colorIn[2] * (steps - i)) + (colorOut[2] * i)) / steps

        myColor = (int(r), int(g), int(b))
        pixels.fill(myColor)
        pixels.show()

        time.sleep(interval)

while True:   
    currentColor = myRed
    blinks = 30
   
    if pattern > 2:
        pattern = 0
        
    if pattern == 0:
        pixels.fill(myYellow)
        fadeColors(myYellow, myRed, 128, 0.1)
    elif pattern == 1:
        pixels.fill(myRed)
        fadeColors(myRed, myWhite, 128, 0.1)
        currentColor = myWhite
    elif pattern == 2:
        pixels.fill(myWhite)
        fadeColors(myWhite, myYellow, 128, 0.1)
        currentColor = myYellow

    if pattern != 1:
        if random.randint(0, 1) == 1:
            while blinks > 0:
                nextPixel = random.randint(0, numpix - 1)
                twinklePixel(currentColor, nextPixel, 128)
                blinks = blinks - 1
        else:
            time.sleep(30)
    else:
        time.sleep(30)

    pattern = pattern + 1

