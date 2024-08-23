import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()

label = pyglet.text.Label('Hello, world',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

image = pyglet.resource.image('resourse/background.jpg')
sprit = pyglet.resource.image('sprites/test_s.png')
music = pyglet.resource.media('music/music.mp3')
icon1 = pyglet.image.load('icon/icon_16x16.png')
icon2 = pyglet.image.load('icon/icon_32x32.png')

event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)
sound = pyglet.resource.media('music/blaster.mp3', streaming=False)

batch = pyglet.graphics.Batch()

sprites = [pyglet.sprite.Sprite(sprit, batch=batch),
]

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
        music.play()
    elif symbol == key.W:
        print('The left arrow key was pressed.')
    elif symbol == key.D:
        print('The enter key was pressed.')

def on_key_release(symbol, modifiers):
      if symbol == key.A:
        print('The "A" key was .')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        sound.play()
        print('The left mouse button was pressed.')

@window.event
def on_draw():
    window.clear()
    image.blit(100, 100)
    label.draw()
    batch.draw()
    window.set_icon(icon1, icon2)
    window.set_minimum_size(320, 200)
    window.set_maximum_size(1024, 768)

pyglet.app.run()
