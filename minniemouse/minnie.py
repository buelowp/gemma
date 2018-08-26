import board, neopixel, time, random
pixpin = board.D1
numpix = 12
myPink = (0xFF, 0x00, 0xFF)
myRed = (0xFF, 0x00, 0x00)
myYellow = (0xFF, 0xFF, 0x00)
pattern = 0    

pixels = neopixel.NeoPixel(pixpin, numpix)

while True:
    if pattern > 2:
        pattern = 0
        
    for i in range(numpix):
        if pattern == 0:
            pixels[i] = myPink
        elif pattern == 1:
            pixels[i] = myRed
        elif pattern == 2:
            pixels[i] = myYellow
            
        time.sleep(0.1)
        pixels.show()
        
    pattern = pattern + 1