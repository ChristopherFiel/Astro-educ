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

transform frantic_shake:
    subpixel True
    pos (0.5, 0.5) anchor (0.5, 0.5)
    zoom 1.05 
    
    block:
        choice:
            linear 0.05 xoffset 18  yoffset -12 blur 2
        choice:
            linear 0.05 xoffset -20 yoffset 15 blur 10
        choice:
            linear 0.05 xoffset 14  yoffset 20 blur 4
        choice:
            linear 0.05 xoffset -16 yoffset -18 blur 8
        choice:
            linear 0.05 xoffset 22  yoffset 10 blur 0
        choice:
            linear 0.05 xoffset -12 yoffset -22 blur 12
        repeat

transform shake_settle(t=3.0):
    subpixel True
    xoffset 20 yoffset -20 blur 10
    easeout t xoffset 0 yoffset 0 blur 0

# ── Particles screen ─────────────────────────────────────────────────────────
transform wisp_a:
    subpixel True
    alpha 0.0 xoffset 0 yoffset 0
    pause 0.0
    parallel:
        linear 1.2 xoffset -90 yoffset -55
    parallel:
        linear 0.3 alpha 0.6
        linear 0.9 alpha 0.0

transform wisp_b:
    subpixel True
    alpha 0.0 xoffset 0 yoffset 0
    pause 0.18
    parallel:
        linear 1.5 xoffset -140 yoffset -30
    parallel:
        linear 0.4 alpha 0.5
        linear 1.1 alpha 0.0

transform wisp_c:
    subpixel True
    alpha 0.0 xoffset 0 yoffset 0
    pause 0.35
    parallel:
        linear 1.0 xoffset -70 yoffset -80
    parallel:
        linear 0.25 alpha 0.7
        linear 0.75 alpha 0.0

transform wisp_d:
    subpixel True
    alpha 0.0 xoffset 0 yoffset 0
    pause 0.55
    parallel:
        linear 1.3 xoffset -120 yoffset -20
    parallel:
        linear 0.3 alpha 0.45
        linear 1.0 alpha 0.0

transform wisp_e:
    subpixel True
    alpha 0.0 xoffset 0 yoffset 0
    pause 0.08
    parallel:
        linear 1.6 xoffset -60 yoffset -110
    parallel:
        linear 0.2 alpha 0.55
        linear 1.4 alpha 0.0

screen wind_particles(xpos=0.5, ypos=0.5):
    zorder 5
    fixed:
        pos (xpos, ypos) anchor (0.5, 0.5)
        add Transform(Solid("#CCCCCC"), size=(8, 8))  at wisp_a
        add Transform(Solid("#BBBBBB"), size=(5, 5))  at wisp_b
        add Transform(Solid("#DDDDDD"), size=(10, 10)) at wisp_c
        add Transform(Solid("#CCCCCC"), size=(6, 6))  at wisp_d
        add Transform(Solid("#AAAAAA"), size=(7, 7))  at wisp_e


# ── Main wind blow-away transform ────────────────────────────────────────────

transform wind_blow_away:
    subpixel True

    parallel:
        linear 0.12 xoffset -10
        linear 0.12 xoffset  6
        linear 0.12 xoffset -4
        linear 0.04 xoffset  0
    parallel:
        linear 0.4 yoffset 0   # hold

    parallel:
        easeout 1.8 xoffset -500 yoffset -120
    parallel:
        easeout 1.8 zoom 0.70
    parallel:
        linear 0.3 alpha 0.85
        linear 0.7 alpha 0.4
        linear 0.8 alpha 0.0
    parallel:
        easeout 1.8 blur 20


# ── Crumble/upward dissolve variant ──────────────────────────────────────────

transform crumble_dissolve:
    subpixel True

    parallel:
        linear 0.06 xoffset  4  yoffset -2
        linear 0.06 xoffset -5  yoffset  3
        linear 0.06 xoffset  3  yoffset -3
        linear 0.06 xoffset -2  yoffset  2
        linear 0.06 xoffset  0  yoffset  0
    parallel:
        zoom 1.0   # hold

    parallel:
        easeout 2.0 yoffset -80
    parallel:
        easeout 2.0 zoom 0.60
    parallel:
        linear 0.5 alpha 0.7
        linear 0.7 alpha 0.3
        linear 0.8 alpha 0.0
    parallel:
        easeout 2.0 blur 14


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