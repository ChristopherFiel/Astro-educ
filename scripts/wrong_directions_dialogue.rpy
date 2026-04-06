default forest_intro_seen = False
default forest_mistakes = 0


label forest_wrong_dialogue:
    python:
        if forest_mistakes <= 2:
            lines = [
                "I should try looking up again",
                "Hmm, this doesn't look like the path Dawn took.",
                "Wait, was it North-East? I might have missed a turn.",
            ]
        elif forest_mistakes <= 5:
            lines = [
                "I should give up acting like a compass there's literally a free one at the sky",
                "Am I walking in circles? I should Look up Now!.",
                "Dawn's going to think I'm an idiot if I don't find that camp soon."
            ]
        else:
            lines = [
                "Oh come on, Dawn taught me to LOOK UP, please!!!",
                "Looking up is free, it gives me direction to not be lost.",
                "I am definitely, 100 percent, lost.",
                "Okay, breathe. Think. North... East... where is that again?",
                "If I end up sleeping in a tree tonight, it's her fault for leaving me."
            ]
        
        selected_line = renpy.random.choice(lines)
    
    player_name "[selected_line]"
    return