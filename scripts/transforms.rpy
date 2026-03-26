transform zoom_to(target_x, target_y, zoom_level=2.0):
    xanchor target_x
    yanchor target_y
    xpos    target_x
    ypos    target_y
    zoom    zoom_level

transform pan_to(target_x, target_y, zoom_level=1.8, dur=1.0):
    linear dur xanchor target_x yanchor target_y xpos target_x ypos target_y zoom zoom_level