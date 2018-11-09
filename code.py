from adafruit_circuitplayground.express import cpx
import time

red = (40,0,0)
green = (0,40,0)
purple = (250,10,30)
off = (0,0,0)

while True:
    if cpx.switch:
        cpx.pixels.fill(purple)
    else:
        cpx.pixels.fill(off)