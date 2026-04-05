transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level

define arrow_wipe_up    = ImageDissolve("images/wipes/arrow_up.png",    0.5, ramplen=1)
define arrow_wipe_down  = ImageDissolve("images/wipes/arrow_down.png",  0.5, ramplen=1)
define arrow_wipe_left  = ImageDissolve("images/wipes/arrow_left.png",  0.5, ramplen=1)
define arrow_wipe_right = ImageDissolve("images/wipes/arrow_right.png", 0.5, ramplen=1)

define arrow_wipe_up_fast    = ImageDissolve("images/wipes/arrow_up.png",    0.3, ramplen=1)
define arrow_wipe_down_fast  = ImageDissolve("images/wipes/arrow_down.png",  0.3, ramplen=1)
define arrow_wipe_left_fast  = ImageDissolve("images/wipes/arrow_left.png",  0.3, ramplen=1)
define arrow_wipe_right_fast = ImageDissolve("images/wipes/arrow_right.png", 0.3, ramplen=1)

define arrow_wipe_up_slow    = ImageDissolve("images/wipes/arrow_up.png",    1.0, ramplen=1)
define arrow_wipe_down_slow  = ImageDissolve("images/wipes/arrow_down.png",  1.0, ramplen=1)
define arrow_wipe_left_slow  = ImageDissolve("images/wipes/arrow_left.png",  1.0, ramplen=1)
define arrow_wipe_right_slow = ImageDissolve("images/wipes/arrow_right.png", 1.0, ramplen=1)

define fast_wipeup = CropMove(0.25, "wipeup")
define fast_wipedown  = CropMove(0.25, "wipedown")
define fast_wipeleft  = CropMove(0.25, "wipeleft")
define fast_wiperight = CropMove(0.25, "wiperight")