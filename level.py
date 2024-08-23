
import pyglet
from settings import *

class Platform(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        platform_image = pyglet.resource.image(PLATFORM_IMAGE_PATH)
        super().__init__(platform_image, *args, **kwargs)
        self.width = platform_image.width * 1.5
        self.height = platform_image.height * 1.5

class Background:
    def __init__(self, background_image_path, *args, **kwargs):
        self.background_image = pyglet.resource.image(background_image_path)
        self.background_sprite = pyglet.sprite.Sprite(self.background_image)
        self.platforms = []
        self.camera = None

    def update_background_size(self, width, height):
        self.background_sprite.width = width
        self.background_sprite.height = height
        self.background_sprite.scale_x = width / self.background_image.width
        self.background_sprite.scale_y = height / self.background_image.height

    def draw(self):
        self.background_sprite.draw()
        for platform in self.platforms:
            platform.draw()
