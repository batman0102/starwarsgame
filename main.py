import random
import arcade
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "starwars"
LAZER_SPEED=5

class Lazer(arcade.Sprite):
    def __init__(self):
        super().__init__('laser.png',0.8)
        self.center_x=window.falcon.center_x
        self.bottom=window.falcon.top
        self.change_y=LAZER_SPEED
        self.laser_sound=arcade.load_sound("laser.wav")
    def update(self):
        self.center_y+=self.change_y
        if self.center_y >SCREEN_HEIGHT:
            self.kill()


class Falcon(arcade.Sprite):

    def __init__(self):
        super().__init__('falcon.png',0.3)
        self.center_x = SCREEN_WIDTH/2
        self.center_y = 100
    def update(self):
        self.center_x+=self.change_x
class Game(arcade.Window):
    def __init__(self,width,height,title):
        super().__init__(width,height,title)
        self.bg=arcade.load_texture('background.jpg')
        self.falcon=Falcon()
        self.set_mouse_visible(False)
        self.lasers=arcade.SpriteList()
        self.setup()

    # размешение обьектов на сцене или в игре
    def setup(self):
        pass
    # отрисовка спрайтов
    def on_draw(self):
        self.clear((255,255,255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,
                                      SCREEN_WIDTH,SCREEN_HEIGHT,
                                      self.bg)
        self.falcon.draw()


    def update(self, delta_time: float):
        self.falcon.update()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.falcon.center_x=x

window= Game(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)


arcade.run()