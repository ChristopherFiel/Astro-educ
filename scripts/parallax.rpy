init -1 python:
    # These match your list: farthestBack, farBack, back, front, inyourface
    config.layers = ["farthestBack", "farBack", "back", "master", "front", "inyourface", "transient", "screens", "overlay"]

    class MouseParallax(renpy.Displayable):
        def __init__(self, layer_info):
            super(MouseParallax, self).__init__()
            self.xoffset, self.yoffset = 0.0, 0.0
            self.layer_info = layer_info
            
            # Apply the parallax transform to the layers
            for m, n in self.layer_info:
                renpy.layer_at_list([self.parallax(m)], n)

        def render(self, width, height, st, at):
            return renpy.Render(width, height)

        def parallax(self, m):
            def trans(d, st, at):
                # Only move if both the global setting AND the scene switch are ON
                if persistent.bg_parallax and parallax_active:
                    d.xoffset = int(round(m * self.xoffset))
                    d.yoffset = int(round(m * self.yoffset))
                else:
                    d.xoffset, d.yoffset = 0, 0
                return 0
            return Transform(function=trans)

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.MOUSEMOTION:
                # Calculate mouse position relative to center
                self.xoffset = (float(x) / config.screen_width) - 0.5
                self.yoffset = (float(y) / config.screen_height) - 0.5
            return None

    # 2. Initialize the displayable
    # This stays in the background but only 'moves' layers when parallax_active is True
    MouseParallax([(-20,"farthestBack"), (-50,"farBack"), (-80,"back"), (-30,"front"), (50,"inyourface")])

    # 3. Assign Dawn and other tags to the correct layers
    config.tag_layer = {
        'bg': 'farBack',
        'dawn': 'back',      # Your sprite Dawn is now assigned here
        'effects': 'front',
    }

# 4. The Control Variable
default parallax_active = False