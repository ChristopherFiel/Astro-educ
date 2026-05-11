transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level

transform dawn_pacing_left(speed=3.0):
    xanchor 0.5 yalign 1.0
    xpos -0.3
    easein speed xpos 1.3
    easein speed xpos -0.3
    repeat

transform dawn_pacing_right(speed=3.0):
    xanchor 0.5 yalign 1.0
    xpos 1.3
    easein speed xpos -0.3
    easein speed xpos 1.3
    repeat

transform meteor_shake:
    xoffset 0 yoffset 0
    linear 0.04 xoffset  24 yoffset -10
    linear 0.04 xoffset -20 yoffset   8
    linear 0.04 xoffset  16 yoffset  -6
    linear 0.04 xoffset -12 yoffset   4
    linear 0.04 xoffset   8 yoffset  -3
    linear 0.04 xoffset  -5 yoffset   2
    linear 0.04 xoffset   3 yoffset  -1
    linear 0.04 xoffset   0 yoffset   0

transform flash_in_out:
    alpha 0.0
    linear 0.06 alpha 1.0
    linear 0.55 alpha 0.0

transform ring_expand:
    xalign 0.99 yalign 0.35 # Tweak to change the impact point
    zoom 0.05 alpha 0.85
    parallel:
        linear 0.9 zoom 5.5
    parallel:
        linear 0.2 alpha 0.85
        linear 0.7 alpha 0.0

transform aftermath_dim:
    alpha 0.0
    0.5  
    linear 0.2 alpha 0.45
    linear 1.2 alpha 0.0

screen meteor_impact_fx():
    add Solid("#FFFFFF") at flash_in_out
    add "images/wipes/shockwave_ring.png" at ring_expand
    add Solid("#1a1a2e") at aftermath_dim

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