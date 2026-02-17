# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Stella")
define a = Character("Alice", color="#f0f8ff")
    

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

    scene black
    with Pause(1)

    show text ""

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg temple

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show stella at bottom

    # These display lines of dialogue.

    s "Hi, this is Stella!"

    s "Thank you for downloading the 'Star GUI kit'!"

    s "This kit is free to use for both personal and commercial projects."

    s "All you have to do is credit me~"

    s "As you can see, everything is star-themed."

    menu:
        " What do you think?"

        "It's cute!":

            $ renpy.notify("Thank you!")

            s "I'm glad you like it!"

            s "If you appreciate my work, consider tipping me on Ko-fi."

            s "You don't have to, but it will help me create more content."
            

        "It's ok.":

            s "If you're looking for something else, try looking at my other UI assets."

            s "You can follow me as well, to stay updated on my new projects."

        "Could be better.":

            $ renpy.notify("ouch!!")

            s "I'm sorry to hear that, maybe you'll find something else to your liking on my profile?"

            s "I'll do my best to create different GUI kits in various styles to fit different projects."

    s "Look around and let me know what you think in the comments!"

    s "Oh, and don't forget to share your project with me, if you use this GUI kit."

    s "I'd love to take a look~"

    s "Well then, enjoy!"

    a "This is my color"
    

    # This ends the game.

    return
