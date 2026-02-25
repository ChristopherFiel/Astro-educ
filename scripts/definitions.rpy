init python:
    import re

    # 1. Define Tints
    tint_dark = im.matrix.tint(0.44, 0.44, 0.75) * im.matrix.brightness(-0.02)
    tint_sunset = im.matrix.tint(0.85, 0.60, 0.45) * im.matrix.brightness(0.10)
    tint_dim = im.matrix.tint(0.90, 0.90, 1.0) * im.matrix.brightness(-0.1)

    # 2. Automate Image Loading
    for file in renpy.list_files():
        
        # --- BACKGROUNDS (images/bg/) ---
        if file.startswith('images/bg/'):
            img_path = re.sub(r'images/', '', file)
            # Supports .png, .jpg, and .webp
            match = re.match(r'images/bg/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)

                renpy.image(img_name + "_day", img_path)
                renpy.image(img_name + "_dusk", im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night", im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_sepia", im.Sepia(img_path))

                # Added a final 'True' condition at the end to prevent crashes
                renpy.image(img_name, ConditionSwitch(
                    "time_of_day == 'DAY'", img_name + "_day",
                    "time_of_day == 'DUSK'", img_name + "_dusk",
                    "time_of_day == 'NIGHT'", img_name + "_night",
                    "time_of_day == 'SEPIA'", img_name + "_sepia",
                    "True", img_name + "_day" 
                ))

        if file.startswith('images/sprites/'):
            img_path = re.sub(r'images/', '', file)
            # Regex updated to handle the 'sprites' folder depth
            match = re.match(r'images/sprites/.*/(.+)\.(png|jpg|webp)', file)
            if match:
                img_name = match.group(1)

                renpy.image(img_name + "_day", img_path)
                renpy.image(img_name + "_dusk", im.MatrixColor(img_path, tint_sunset))
                renpy.image(img_name + "_night", im.MatrixColor(img_path, tint_dark))
                renpy.image(img_name + "_dim", im.MatrixColor(img_path, tint_dim))
                renpy.image(img_name + "_sepia", im.Sepia(img_path))

                renpy.image(img_name, ConditionSwitch(
                    "sprite_effect == 'DIM'", img_name + "_dim",
                    "time_of_day == 'DAY'", img_name + "_day",
                    "time_of_day == 'DUSK'", img_name + "_dusk",
                    "time_of_day == 'NIGHT'", img_name + "_night",
                    "time_of_day == 'SEPIA'", img_name + "_sepia",
                    "True", img_name + "_day" # Fallback: defaults to day version
                ))

# 3. Global Variables (Make sure these are outside the python block)
default time_of_day = 'DAY'
default sprite_effect = None