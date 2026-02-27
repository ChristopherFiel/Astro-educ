# Declare characters used by this game. The color argument colorizes the
define d = Character("Dawn", image="sprites/Dawn", color="#e6cc90")

# Transforms/transitions for expressions/blinks
define config.say_attribute_transition = Dissolve(0.1)
# Randomize blinking time
transform blinkwait:
    choice:
        4.0
    choice:
        3.0
    choice:
        2.0

#Blinking Character Images
image Dawn normal:
    zoom 1.5
    "sprites/Dawn/Dawn_normal.png"
    blinkwait
    "sprites/Dawn/Dawn_normal_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_normal.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn normal2:
    zoom 1.5
    "sprites/Dawn/Dawn_normal2.png"
    blinkwait
    "sprites/Dawn/Dawn_normal2_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_normal2.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn lookaway:
    zoom 1.5
    "sprites/Dawn/Dawn_lookaway.png"
    blinkwait
    "sprites/Dawn/Dawn_lookaway_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_lookaway.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn surprised:
    zoom 1.5
    "sprites/Dawn/Dawn_surprised.png"
    blinkwait
    "sprites/Dawn/Dawn_surprised_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_surprised.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn pout:
    zoom 1.5
    "sprites/Dawn/Dawn_pout.png"
    blinkwait
    "sprites/Dawn/Dawn_pout_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_pout.png" with Dissolve(0.1)
    0.1
    repeat

image Dawn smile:
    zoom 1.5
    "sprites/Dawn/Dawn_smile.png"
    blinkwait
    "sprites/Dawn/Dawn_smile_blink.png" with Dissolve(0.1)
    0.3
    "sprites/Dawn/Dawn_smile.png" with Dissolve(0.1)
    0.1
    repeat