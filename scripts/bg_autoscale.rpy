init -1 python:
    # This automatically gets the width and height you set in options.rpy
    SCREEN_W = config.screen_width
    SCREEN_H = config.screen_height

# This transform will stretch/shrink an image to fit your screen exactly
transform resizer:
    size (SCREEN_W, SCREEN_H)

transform fill_screen:
    subpixel True
    xalign 0.5 yalign 0.5
    size (SCREEN_W, None) 
    fit "cover"

init python:
    import os

    for file in renpy.list_files():
        # Make sure the path matches your folder structure exactly
        if file.startswith("images/bg/") and file.lower().endswith((".png", ".jpg", ".webp")):
            
            # This extracts 'park' from 'images/bg/park.png'
            name = os.path.splitext(os.path.basename(file))[0]
            
            renpy.image("bg " + name, At(file, resizer))

init python:
    def auto_aspect_ratio(d):
        return Frame(d, size=(SCREEN_W, SCREEN_H))

# Use 'At(file, resizer)' for stretching
# Use 'Frame(file, SCREEN_W, SCREEN_H)' for smart cropping