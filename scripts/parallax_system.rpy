################################################################################
##
##  LAYERED PARALLAX SYSTEM  ·  parallax_system.rpy
##  Drop this file into your game/ directory — no other changes needed.
##
##  FEATURES
##    • Mouse-driven parallax with per-layer depth control
##    • Smooth lerp so layers glide instead of snap
##    • Auto-scale (cover-fit) on every layer & plain backgrounds
##    • Enable / disable at any time without scene teardown
##    • Adjustable strength, smoothing, and per-layer depth at runtime
##
################################################################################


## ─────────────────────────────────────────────────────────────────────────────
##  1.  CORE PYTHON CLASS  (init priority -10 so it loads before everything)
## ─────────────────────────────────────────────────────────────────────────────

init -10 python:

    class ParallaxSystem(object):

        def __init__(self):
            self.enabled  = True   # Toggle the whole effect on / off
            self.strength = 40     # Max pixel offset from centre (each direction)
            self.smooth   = 0.08   # Lerp factor per frame  (lower = smoother lag)
            self._layers  = []     # [(displayable, depth), ...]
            self._ox      = 0.0    # Current smoothed X offset
            self._oy      = 0.0    # Current smoothed Y offset

        # ── Layer management ─────────────────────────────────────────────────

        def set_layers(self, layers):
            """Replace all layers at once.  layers = [(img, depth), ...]"""
            self._layers = list(layers)

        def add_layer(self, image, depth=0.5):
            """Append a single layer."""
            self._layers.append((image, float(depth)))

        def clear_layers(self):
            """Remove every layer."""
            self._layers = []

        # ── Runtime control ──────────────────────────────────────────────────

        def toggle(self):
            """Flip enabled state.  Resets offsets when disabling."""
            self.enabled = not self.enabled
            if not self.enabled:
                self._ox = 0.0
                self._oy = 0.0

        def enable(self):
            self.enabled = True

        def disable(self):
            self.enabled = False
            self._ox = 0.0
            self._oy = 0.0

        # ── Internal helpers (called by the screen every frame) ───────────────

        def _update(self):
            """
            Smoothly interpolate current offset toward the mouse-driven target.
            Call once per frame inside the parallax_bg screen.
            """
            if not self.enabled or not self._layers:
                self._ox = 0.0
                self._oy = 0.0
                return

            mx, my = renpy.get_mouse_pos()
            sw = float(renpy.config.screen_width)
            sh = float(renpy.config.screen_height)

            # Normalise mouse to −1 … +1, then scale by strength
            tx = (mx / sw - 0.5) * 2.0 * self.strength
            ty = (my / sh - 0.5) * 2.0 * self.strength

            # Smooth lerp
            f        = max(0.0, min(1.0, self.smooth))
            self._ox += (tx - self._ox) * f
            self._oy += (ty - self._oy) * f

        def _layer_transform(self, displayable, depth):
            """
            Build a cover-fitted Transform for one layer, offset by its depth.
            The image is expanded by (strength * 2) on each axis so there is
            always pixel data to reveal as the layer slides around.
            """
            s  = int(self.strength)
            ox = int(self._ox * depth)
            oy = int(self._oy * depth)
            sw = renpy.config.screen_width
            sh = renpy.config.screen_height

            return Transform(
                child   = displayable,
                xysize  = (sw + s * 2, sh + s * 2),  # oversized canvas
                fit     = "cover",                    # auto-scale to fill
                xpos    = -s + ox,                    # slide left/right
                ypos    = -s + oy,                    # slide up/down
                xanchor = 0,
                yanchor = 0,
            )

    # ── Global singleton ─────────────────────────────────────────────────────
    parallax = ParallaxSystem()


## ─────────────────────────────────────────────────────────────────────────────
##  2.  AUTO-SCALE TRANSFORMS  (for regular, non-parallax backgrounds)
## ─────────────────────────────────────────────────────────────────────────────

# Cover-fit: fills the screen completely, cropping if needed (no black bars).
transform bg_autoscale:
    xysize (config.screen_width, config.screen_height)
    fit    "cover"
    xalign 0.5
    yalign 0.5

# Contain-fit: fits entirely inside the screen (may have letterbox bars).
transform bg_autoscale_contain:
    xysize (config.screen_width, config.screen_height)
    fit    "contain"
    xalign 0.5
    yalign 0.5

# Stretch: ignores aspect ratio, always fills 100 %.
transform bg_autoscale_stretch:
    xysize (config.screen_width, config.screen_height)


## ─────────────────────────────────────────────────────────────────────────────
##  3.  THE PARALLAX SCREEN
##      Show this screen whenever you want active parallax.
##      Hide it (hide screen parallax_bg) to remove all parallax layers.
## ─────────────────────────────────────────────────────────────────────────────

screen parallax_bg():
    zorder -100   # Draw behind everything else

    # Update the smoothed offsets once per frame
    $ parallax._update()

    # Draw every layer
    for _img, _depth in parallax._layers:
        add parallax._layer_transform(_img, _depth)

    # Redraw at ~60 fps so smoothing animates even when the mouse is still
    timer 0.016 repeat True action Function(renpy.restart_interaction)


## ─────────────────────────────────────────────────────────────────────────────
##  4.  CONVENIENCE LABEL  — activate / configure parallax in one call
## ─────────────────────────────────────────────────────────────────────────────

label activate_parallax(layers=None, strength=40, smooth=0.08):
    """
    Call from any label:
        call activate_parallax(layers=[("bg_sky",0.1),("bg_trees",0.7)])

    Parameters
    ----------
    layers   – list of (image, depth) tuples  (see class docstring)
    strength – max pixel shift  (default 40)
    smooth   – lerp factor  (default 0.08)
    """
    python:
        parallax.strength = strength
        parallax.smooth   = smooth
        if layers is not None:
            parallax.set_layers(layers)
        parallax.enable()
    show screen parallax_bg
    return


label deactivate_parallax():
    """Hide the parallax screen and reset offsets."""
    $ parallax.disable()
    hide screen parallax_bg
    return


## ─────────────────────────────────────────────────────────────────────────────
##  5.  DEMO  —  run `renpy . --test` or jump to label demo_parallax
## ─────────────────────────────────────────────────────────────────────────────

#  Uncomment the block below if you want a runnable demo.
#  Replace the image paths with real files in your project.

##  ┌─ demo images (replace with your own assets) ───────────────────────────┐
# image demo_sky      = "gui/main_menu.png"   # reuse any image you have
# image demo_mid      = "gui/main_menu.png"
# image demo_fore     = "gui/main_menu.png"
##  └─────────────────────────────────────────────────────────────────────────┘

# label start:
#
#     ## ── Example 1: Full parallax scene ──────────────────────────────────
#     scene black
#
#     python:
#         parallax.set_layers([
#             ("demo_sky",  0.10),   # Far background — barely moves
#             ("demo_mid",  0.40),   # Mid-ground
#             ("demo_fore", 0.80),   # Foreground — moves the most
#         ])
#         parallax.strength = 40
#         parallax.smooth   = 0.08
#
#     show screen parallax_bg
#
#     "Move your mouse — each layer drifts at its own speed."
#     "The images are auto-scaled to cover the screen on every resolution."
#
#     ## ── Example 2: Plain background with auto-scale ─────────────────────
#     hide screen parallax_bg
#     scene demo_sky at bg_autoscale
#
#     "This is a regular background, auto-scaled with [bg_autoscale]."
#
#     ## ── Example 3: Single-layer parallax (subtle depth on one image) ────
#     python:
#         parallax.set_layers([("demo_sky", 0.25)])
#         parallax.strength = 20
#
#     show screen parallax_bg
#
#     "Even a single layer gives a nice floating feeling."
#
#     ## ── Toggle off mid-scene ─────────────────────────────────────────────
#     menu:
#         "Disable parallax?"
#         "Yes":
#             $ parallax.toggle()
#             "Parallax disabled — layers are locked in place."
#         "No":
#             pass
#
#     hide screen parallax_bg
#     return


################################################################################
##  QUICK-REFERENCE CHEAT SHEET
##
##  ┌──────────────────────────────────────────────────────────────────────────┐
##  │  # Set / change layers at any point                                      │
##  │  python:                                                                 │
##  │      parallax.set_layers([                                               │
##  │          ("img_name_or_path",  depth_0_to_1),                           │
##  │          ...                                                             │
##  │      ])                                                                  │
##  │                                                                          │
##  │  # Show the parallax screen                                              │
##  │  show screen parallax_bg                                                 │
##  │                                                                          │
##  │  # Hide it                                                               │
##  │  hide screen parallax_bg                                                 │
##  │                                                                          │
##  │  # Or use the convenience labels                                         │
##  │  call activate_parallax(layers=[...], strength=50, smooth=0.06)         │
##  │  call deactivate_parallax                                                │
##  │                                                                          │
##  │  # Plain background with auto-scaling (no parallax needed)              │
##  │  scene my_bg at bg_autoscale                                             │
##  │                                                                          │
##  │  # Tweak settings at runtime                                             │
##  │  python:                                                                 │
##  │      parallax.strength = 60   # pixels  (default 40)                   │
##  │      parallax.smooth   = 0.05 # 0.01=very smooth … 0.3=snappy          │
##  └──────────────────────────────────────────────────────────────────────────┘
################################################################################
