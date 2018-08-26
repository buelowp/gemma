import board, neopixel, time, random
numpix = 12
myPink = (0xFF, 0x00, 0xFF)
myRed = (0xFF, 0x00, 0x00)
myYellow = (0xFF, 0xFF, 0x00)
pattern = 0    

pixels = neopixel.NeoPixel(board.D1, numpix)

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
    if pattern > 2:
        pattern = 0
        
    if pattern == 0:
        pixels.fill(myYellow)
        fadeColors(myYellow, myRed, 128, 0.1)
    elif pattern == 1:
        pixels.fill(myRed)
        fadeColors(myRed, myPink, 128, 0.1)
    elif pattern == 2:
        pixels.fill(myPink)
        fadeColors(myPink, myYellow, 128, 0.1)
        
    time.sleep(20)
    pattern = pattern + 1

