import listen
import random


def farbe_waehlen():
    farbe = random.choice(list(listen.neon_farben.values()))
    return farbe


def get_random_neon_color():
    return random.choice(list(listen.neon_farben.values()))
