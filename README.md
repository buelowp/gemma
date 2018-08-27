# Neopixel work for the Adafruit Gemma M0

In this repo, you can find work related to some Neopixel controls for the Gemma M0 board. The motivation was to create some wall hangers for our Halloween Disney cruise, so you will find routines related to that. However, usage of the routines is pretty simple, and can be pulled out and used elsewhere.

## Hardware

The M0 is a wonderful micro, super low power, efficient, and micropython is a treat for simple use cases

https://www.adafruit.com/product/3501

There are a variety of these, but I mostly use the 12 and 16 pixel rings for my toys

https://www.adafruit.com/product/1463

Depending on your lighting needs, the Gemma + 16 pixels may last as much as 8 to 10 hours on this battery, but is possibly less if you light them up full brightness

https://www.adafruit.com/product/328

You'll need a charger

https://www.adafruit.com/product/1304

## Notes

Use the LiPoly batteries, they are safer than LiIon batteries for failure cases. I think all Adafruit batteries have low voltage and overcharge protection, but use a safe charger. Remember, Lithium is volatile, and can fail spectacularly. It is safe as long as you remember to treat it well

## Usage

For the Gemma, you can use my files directly. Just copy them onto the Gemma renaming them to main.py when you do so. They will run as expected. If you have a different number of LED's, just change the numpix value to match.

## License

You are free to use at your leisure anything you find here. Questions can be asked via github. I do not warranty this code, nor do I promise it does what you need it to. It works for me, that's what I care most about. I hope it is useful to you as well.
