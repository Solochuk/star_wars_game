import pyglet
from player import Player

class ObiWan(Player):
    def __init__(self, *args, **kwargs):
        stand_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/stand.gif')
        walk_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/walking.gif')
        run_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/running.gif')
        jump_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/jump.gif')
        protection_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/protection.gif')
        force_stun_aimation = pyglet.image.load_animation('gamedata/animation/obi-wan/force_stun.gif')
        force_speed_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/force_speed.gif')
        force_shield_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/force_shield.gif')
        yoda_s_techning_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/yoda_s_techning.gif')
        jedi_s_devotion_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/jedi_s_devotion.gif')
        attack_5_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/attack__5.gif')
        attack_4_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/attack__4.gif')
        attack_3_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/attack__3.gif')
        attack_2_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/attack__2.gif')
        attack_animation = pyglet.image.load_animation('gamedata/animation/obi-wan/attack.gif')
        super().__init__(stand_animation, walk_animation, run_animation, attack_animation,
                         attack_5_animation, attack_4_animation,attack_3_animation, attack_2_animation,
                         jump_animation,*args, **kwargs)
