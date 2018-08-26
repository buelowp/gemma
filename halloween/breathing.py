import board, neopixel, time, random, analogio
numpix = 12
myOrange = (0xFF, 0x40, 0x00)
myPurple = (0x94, 0x00, 0xD3)
myGreen = (0x00, 0xFF, 0x00)
whichColor = 0
bright = 1.0
multiplier = 0.02
direction = 1
changeColor = 18
analogTwoValue = analogio.AnalogIn(board.A1)
analogThreeValue = analogio.AnalogIn(board.A2)
random.seed(analogTwoValue.value + 10 * analogThreeValue.value)
pixels = neopixel.NeoPixel(board.D1, numpix, brightness=bright)

while True:
    changeDirection = random.randint(0, 30)
    
    if changeColor == 18:
        pixels.fill(myOrange)
    elif changeColor == 27:
        pixels.fill(myGreen)
    elif changeColor == 56:
        pixels.fill(myPurple)
    
    pixels.brightness = bright
    pixels.show()

    if changeDirection == 25:
        multiplier = multiplier * -1
        
    if bright >= 1.0:
        multiplier = -0.02
    elif bright <= .4:
        multiplier = 0.02
        
    bright = bright + multiplier
    changeColor = random.randint(0, 32792)
    time.sleep(0.04)
