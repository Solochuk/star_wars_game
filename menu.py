import pyglet
from settings import *

class Menu:
    def __init__(self, window):
        self.window = window
        self.menu_background = pyglet.image.load_animation('gamedata/animation/menu/gopery.gif')
        self.menu_background_sprite = pyglet.sprite.Sprite(self.menu_background)
        self.episode_animation = pyglet.image.load_animation('gamedata/animation/menu/star_wars_episode_3.gif')
        self.episode_sprite = pyglet.sprite.Sprite(self.episode_animation)
        self.window_width = window.width
        self.window_height = window.height
        self.is_active = True
        self.update_menu_background_size(self.window_width, self.window_height)

        self.button_label = pyglet.text.Label(
            'Start Game',
            font_name='Arial',
            font_size=24,
            x=window.width // 2,
            y=window.height // 4,
            anchor_x='center',
            anchor_y='center',
            color=(255, 255, 255, 255)
        )

        self.button_width = 200
        self.button_height = 50
        self.button_x = self.button_label.x - self.button_width // 2
        self.button_y = self.button_label.y - self.button_height // 2

    def update_menu_background_size(self, window_width, window_height):
        self.menu_background_sprite.scale_x = window_width / self.menu_background_sprite.width
        self.menu_background_sprite.scale_y = window_height / self.menu_background_sprite.height

        scale_factor = 1.5
        self.episode_sprite.scale = scale_factor
        self.episode_sprite.x = window_width // 2 - self.episode_sprite.width // 2
        self.episode_sprite.y = window_height // 2 - self.episode_sprite.height // 2

    def draw(self):
        self.menu_background_sprite.draw()
        self.episode_sprite.draw()
        self.button_label.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if (self.button_x <= x <= self.button_x + self.button_width and
            self.button_y <= y <= self.button_y + self.button_height):
            self.is_active = False

    def update(self, dt):
        pass
