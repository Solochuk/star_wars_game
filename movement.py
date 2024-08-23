from pyglet.window import key
from settings import *

class MovementHandler:
    def __init__(self, player, left_key, right_key, jump_key, run_key, attack_key, attack_2_key,
                 attack_3_key, attack_4_key, attack_5_key):
        self.player = player
        self.left_key = left_key
        self.right_key = right_key
        self.jump_key = jump_key
        self.run_key = run_key
        self.attack_key = attack_key
        self.attack_2_key = attack_2_key
        self.attack_3_key = attack_3_key
        self.attack_4_key = attack_4_key
        self.attack_5_key = attack_5_key
        self.keys = key.KeyStateHandler()

    def update(self, dt):
        move_speed = PLAYER_RUN_SPEED if self.keys[self.run_key] else PLAYER_MOVE_SPEED

        if self.keys[self.left_key]:
            self.player.vx = -move_speed
            self.player.facing_right = False
            self.player.is_walking = not self.keys[self.run_key]
            self.player.is_running = self.keys[self.run_key]
        elif self.keys[self.right_key]:
            self.player.vx = move_speed
            self.player.facing_right = True
            self.player.is_walking = not self.keys[self.run_key]
            self.player.is_running = self.keys[self.run_key]
        else:
            self.player.vx = 0
            self.player.is_walking = False
            self.player.is_running = False

        if self.keys[self.jump_key] and self.player.on_ground and not self.player.is_attacking:
            self.player.jump()

        if self.keys[self.attack_key] and not self.player.is_jumping and not self.player.is_attacking:
            self.player.attack('attack')
        elif self.keys[self.attack_2_key] and not self.player.is_jumping and not self.player.is_attacking:
            self.player.attack('attack_2')
        elif self.keys[self.attack_3_key] and not self.player.is_jumping and not self.player.is_attacking:
            self.player.attack('attack_3')
        elif self.keys[self.attack_4_key] and not self.player.is_jumping and not self.player.is_attacking:
            self.player.attack('attack_4')
        elif self.keys[self.attack_5_key] and not self.player.is_jumping and not self.player.is_attacking:
            self.player.attack('attack_5')
