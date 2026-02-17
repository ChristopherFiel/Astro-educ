# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stella")
define a = Character("Aris", color="#f0f8ff")
    

transform bottom:
    xalign 0.5
    yalign 0.0

# label splashscreen:
#     scene black
#     with Pause(1)

#     show text "Fiel & Sarmiento presents..." with dissolve
#     with Pause(2)

#     hide text with dissolve
#     with Pause(1)

#     return

# The game starts here.

label start:

    $ quick_menu = False  # This kills the menu logic
    window hide

    scene black
    with Pause(1)

    show text "Somewhere in the southern hemisphere" with dissolve
    pause 

    hide text with dissolve
    with Pause(1)

    $ quick_menu = True   # This brings the menu back
    window show

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg temple

    a "WAAAAAAAAAAAHHHHHHHH!!!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show stella at bottom

    # These display lines of dialogue.
    

    # This ends the game.

    return
