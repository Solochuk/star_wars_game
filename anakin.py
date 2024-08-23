import pyglet
from player import Player

class Anakin(Player):
    def __init__(self, *args, **kwargs):
        stand_animation = pyglet.image.load_animation('gamedata/animation/anakin/stand.gif')
        walk_animation = pyglet.image.load_animation('gamedata/animation/anakin/walk.gif')
        run_animation = pyglet.image.load_animation('gamedata/animation/anakin/running.gif')
        jump_animation = pyglet.image.load_animation('gamedata/animation/anakin/jump.gif')
        jump_back_animation= pyglet.image.load_animation('gamedata/animation/anakin/jump_back.gif')
        force_push_aimation = pyglet.image.load_animation('gamedata/animation/anakin/force_push.gif')
        force_attracts_animation = pyglet.image.load_animation('gamedata/animation/anakin/force_attracts.gif')
        force_anger_animation = pyglet.image.load_animation('gamedata/animation/anakin/force_anger.gif')
        cast_lightsaber_animation = pyglet.image.load_animation('gamedata/animation/anakin/cast_lightsaber.gif')
        attack_back_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack_back.gif')
        attack_5_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack__5.gif')
        attack_4_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack__4.gif')
        attack_3_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack__3.gif')
        attack_2_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack__2.gif')
        attack_animation = pyglet.image.load_animation('gamedata/animation/anakin/attack.gif')
        super().__init__(stand_animation, walk_animation, run_animation, attack_animation,
                         attack_5_animation, attack_4_animation,attack_3_animation, attack_2_animation,
                         jump_animation,*args, **kwargs)
