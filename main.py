import pyglet
from settings import *
from anakin import Anakin
from obiwan import ObiWan
from level import Background, Platform
from menu import Menu
from movement import MovementHandler
from pyglet.window import key

window = pyglet.window.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

level = Background(BACKGROUND_IMAGE_PATH)
level.update_background_size(window.width, window.height)
level.platforms.append(Platform(x=-50, y=-50))

music = pyglet.resource.media('gamedata/music/anakin-vs-obi-wan.mp3', streaming=False)
music_player = pyglet.media.Player()
music_player.queue(music)

menu_music = pyglet.resource.media('gamedata/music/fanfaryi.mp3', streaming=False)
menu_music_player = pyglet.media.Player()
menu_music_player.queue(menu_music)
menu_music_player.play()

r2d2_sound = pyglet.resource.media('gamedata/music/r2d2.mp3', streaming=False)

anakin = Anakin(x=100, y=50)
obiwan = ObiWan(x=1100, y=50)
obiwan.facing_right = False

anakin_movement = MovementHandler(anakin, key.A, key.D, key.W, key.LCTRL, key.F, key.R,
                                  key.T, key.E, key.C)
obiwan_movement = MovementHandler(obiwan, key.LEFT, key.RIGHT, key.UP, key.NUM_0, key.NUM_1,
                                  key.NUM_2, key.NUM_3, key.NUM_4, key.NUM_5)

menu = Menu(window)

window.push_handlers(anakin_movement.keys)
window.push_handlers(obiwan_movement.keys)
window.push_handlers(menu)

game_over = False

@window.event
def on_draw():
    window.clear()
    if menu.is_active:
        menu.draw()
    elif game_over:
        show_game_over_message()
    else:
        level.draw()
        anakin.draw()
        obiwan.draw()

def update(dt):
    global game_over
    if not menu.is_active and not game_over:

        if menu_music_player.playing:
            menu_music_player.pause()

        if not music_player.playing:
            music_player.play()
        anakin_movement.update(dt)
        obiwan_movement.update(dt)
        anakin.update(dt, level.platforms, [obiwan])
        obiwan.update(dt, level.platforms, [anakin])
        if anakin.is_dead() or obiwan.is_dead():
            game_over = True
            music_player.pause()
            r2d2_sound.play()

def show_game_over_message():
    label = pyglet.text.Label(
        'Game Over',
        font_name='Arial',
        font_size=36,
        x=window.width // 2,
        y=window.height // 2,
        anchor_x='center',
        anchor_y='center',
        color=(255, 0, 0, 255)
    )
    label.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    menu.on_mouse_press(x, y, button, modifiers)

@window.event
def on_key_release(symbol, modifiers):
    if not menu.is_active:
        anakin_movement.keys.on_key_release(symbol, modifiers)
        obiwan_movement.keys.on_key_release(symbol, modifiers)

pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()
