# Character dialogue sfx system
init python:
    renpy.music.register_channel("dialogue_sfx", mixer="sfx")

    def dawn_callback(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogue_sfx/me.mp3", channel="dialogue_sfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="dialogue_sfx", fadeout=0.1)

    def default_callback(event, **kwargs):
        if event == "show":
            renpy.sound.play("audio/dialogue_sfx/Honk.mp3", channel="dialogue_sfx", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="dialogue_sfx", fadeout=0.1)
    
    config.character_callback = default_callback


# Character Definitions
define d = Character("Dawn", image="sprites/Dawn", color="#e6cc90", callback=dawn_callback)
define d_unknown = Character("???",  image="sprites/Dawn", color="#e6cc90", callback=dawn_callback)
define d_top = Character("Dawn", window_yalign=0.05, callback=dawn_callback)
define p = Character("Player", color="#f0f8ff", callback=default_callback)


# Dialogue sfx transition
define config.say_attribute_transition = Dissolve(0.1)


# Character blink transforms
transform blinkwait:
    choice:
        4.0
    choice:
        3.0
    choice:
        2.0
    choice:
        1.0

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