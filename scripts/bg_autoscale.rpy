init -1 python:
    # This automatically gets the width and height you set in options.rpy
    SCREEN_W = config.screen_width
    SCREEN_H = config.screen_height

# This transform will stretch/shrink an image to fit your screen exactly
transform resizer:
    size (SCREEN_W, SCREEN_H)

# This transform fills the screen but keeps the aspect ratio (crops the edges)
transform fill_screen:
    xalign 0.5 yalign 0.5
    truecenter
    # This ensures the image is at least as big as the screen
    size (SCREEN_W, SCREEN_H)

init python:
    import os

    # Change "bg" to whatever your background folder is named
    for file in renpy.list_files():
        if file.startswith("images/bg/") and (file.endswith(".png") or file.endswith(".jpg") or file.endswith(".webp")):
            
            name = os.path.splitext(os.path.basename(file))[0]
            
            # This makes "show bg forest_day" automatically scale to your screen!
            renpy.image("bg " + name, At(file, resizer))

init python:
    def auto_aspect_ratio(d):
        # This function calculates if the image is too wide or too tall
        # and scales it so it covers the screen without stretching.
        return Frame(d, size=(SCREEN_W, SCREEN_H))

# Use 'At(file, resizer)' for stretching
# Use 'Frame(file, SCREEN_W, SCREEN_H)' for smart cropping