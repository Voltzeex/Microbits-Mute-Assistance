# Add your Python code here. E.g.
from microbit import *


while True:
gesture = accelerometer.current_gesture()
print(speaker.is_on())
    if button_a.is_pressed():
        display.show(Image.YES)
        sleep(4000)
    elif button_b.is_pressed():
        display.show(Image.NO)
        sleep(4000)
# Basic responses for those that don't speak in sign language, and so that the person doesn't have to write them down.
    elif pin0.is_touched():
        display.scroll('My owner is ... and they are ... years old. Nice to meet you!')
        sleep(4000)
    elif pin1.is_touched():
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        sleep(4000)
        display.scroll('My owner is lost,please assist them!')
# These are emergency responses, which can only be activated by touching GND and the respective pin. I wanted to put a more alarming sound to play, but I can't test out the noises myself.
    elif pin2.is_touched():
        break
# A way to conserve battery and turn off the nametag when not needed
    elif gesture == "face down" 
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        audio.play(Sound.SLIDE)
        sleep(4000)
        display.scroll('My owner seems to have fallen,please assist them!')
# I would make the text into audio instead, but I would need the physical microbit to test it sadly
    else display.scroll('I am mute, and cannot communicate other than through text,writing, or sign language. Thank you for being patient!')
    display.show(Image.HEART)
    sleep(2000)
    display.show(Image.HEART_SMALL)
    sleep(2000)
# Basic text scroll when it is idle, just to inform people