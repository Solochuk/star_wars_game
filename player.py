import pyglet
import time
import pyglet.media
import random
from settings import *

class Player(pyglet.sprite.Sprite):
    def __init__(self, stand_animation, walk_animation, run_animation, attack_animation,
                 jump_animation, attack_5_animation, attack_4_animation,
                 attack_3_animation, attack_2_animation, *args, **kwargs):
        super().__init__(stand_animation, *args, **kwargs)
        self.stand_animation = stand_animation
        self.walk_animation = walk_animation
        self.run_animation = run_animation
        self.jump_animation = jump_animation
        self.attack_animation = attack_animation

        self.attack_animations = {
            'attack_5': attack_5_animation,
            'attack_4': attack_4_animation,
            'attack_3': attack_3_animation,
            'attack_2': attack_2_animation
        }

        self.sword_sounds = [
            pyglet.media.load('gamedata/lightsaber_sound/laser_sword_strike01.mp3', streaming=False),
            pyglet.media.load('gamedata/lightsaber_sound/laser_sword_strike02.mp3', streaming=False),
            pyglet.media.load('gamedata/lightsaber_sound/laser_sword_strike03.mp3', streaming=False),
            pyglet.media.load('gamedata/lightsaber_sound/laser_sword_strike05.mp3', streaming=False),
        ]
        self.current_attack = None
        self.scale_x = 2
        self.scale_y = 2
        self.is_walking = False
        self.is_running = False
        self.is_jumping = False
        self.is_attacking = False
        self.facing_right = True
        self.vx = 0
        self.vy = 0
        self.on_ground = True
        self.hp = 100
        self.jump_strength = PLAYER_JUMP_STRENGTH
        self.attack_duration = 2
        self.attack_start_time = 0
        self.damage_dealt = False
        self.jump_animation_played = False

        self.hitbox = pyglet.shapes.Rectangle(self.x, self.y, self.width, self.height, color=(0, 0, 0, 0))

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_dead(self):
        return self.hp <= 0

    def jump(self):
        if self.on_ground and not self.is_attacking:
            self.on_ground = False
            self.is_jumping = True
            self.jump_animation_played = False
            self.vy = self.jump_strength
            self.image = self.jump_animation

    def attack(self, attack_type='attack'):
        if not self.is_attacking:
            self.is_attacking = True
            self.attack_start_time = time.time()
            self.damage_dealt = False
            self.current_attack = attack_type
            self.image = self.attack_animations.get(attack_type, self.attack_animation)

            random_sword_sound = random.choice(self.sword_sounds)
            random_sword_sound.play()

    def update(self, dt, platforms, other_players):
        if not self.is_attacking:
            self.x += self.vx * dt
            self.y += self.vy * dt

        self.update_hitbox()

        if not self.on_ground:
            self.vy -= 1000 * dt

        for platform in platforms:
            if self.collides_with(platform):
                self.y = platform.y + platform.height
                self.vy = 0
                self.on_ground = True
                self.is_jumping = False
                self.image = self.stand_animation

        if self.is_attacking and not self.damage_dealt:
            for other_player in other_players:
                if self != other_player and self.hitbox_intersects(other_player.hitbox):
                    other_player.take_damage(5)
                    self.damage_dealt = True
                    break

        self.update_animation()

    def update_hitbox(self):
        if self.facing_right:
            self.hitbox.x = self.x
        else:
            self.hitbox.x = self.x - self.width

        self.hitbox.y = self.y
        self.hitbox.width = self.width
        self.hitbox.height = self.height

    def update_animation(self):
        if self.is_attacking:
            if time.time() - self.attack_start_time < self.attack_duration:
                attack_animation = self.attack_animations.get(self.current_attack, self.attack_animation)
                if self.image != attack_animation:
                    self.image = attack_animation
            else:
                self.is_attacking = False
                self.current_attack = None
                self.image = self.stand_animation if not self.is_walking and not self.is_running else self.image

        elif self.is_jumping:
            if not self.jump_animation_played:
                self.image = self.jump_animation
                self.jump_animation_played = True
                
            elif self.on_ground:
                self.is_jumping = False
                self.jump_animation_played = False
                self.image = self.stand_animation

        elif self.is_running:
            if self.image != self.run_animation:
                self.image = self.run_animation

        elif self.is_walking:
            if self.image != self.walk_animation:
                self.image = self.walk_animation

        else:
            if self.image != self.stand_animation:
                self.image = self.stand_animation

        if not self.facing_right:
            self.scale_x = -2
        else:
            self.scale_x = 2

    def collides_with(self, platform):
        if (
            self.x + self.width > platform.x and
            self.x < platform.x + platform.width and
            self.y + self.height > platform.y and
            self.y < platform.y + platform.height
        ):
            self.y = platform.y
            self.vy = 0
            self.on_ground = True
            self.is_jumping = False
            return True
        return False

    def hitbox_intersects(self, other_hitbox):
        return (
            self.hitbox.x < other_hitbox.x + other_hitbox.width and
            self.hitbox.x + self.hitbox.width > other_hitbox.x and
            self.hitbox.y < other_hitbox.y + other_hitbox.height and
            self.hitbox.y + self.hitbox.height > other_hitbox.y
        )

    def draw(self):
        super().draw()

        if self.facing_right:
            hp_x = self.x + self.width // 2
        else:
            hp_x = self.x - self.width // 2

        label = pyglet.text.Label(
            f'HP: {self.hp}',
            font_name='Arial',
            font_size=14,
            x=hp_x,
            y=self.y + self.height + 10,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 255)
        )
        label.draw()
