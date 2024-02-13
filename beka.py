import random
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "starwars"
# 2.6 cкорость лазера
LASER_SPEED = 5


# 2 5 лазер
class Lazer(arcade.Sprite):

    def __init__(self):
        super().__init__('laser.png', 0.8)
        # спавн лазера у сокола
        self.center_x = window.falcon.center_x
        # спавн у носа лазера
        self.bottom = window.falcon.top
        # скорость лазера
        self.change_y = LASER_SPEED
        #         звук
        self.laser_sound = arcade.load_sound('laser.wav')

    # движение
    def update(self):
        self.center_y += self.change_y
        # eдаление лазера
        if self.center_y > SCREEN_HEIGHT:
            self.kill()


class Falcon(arcade.Sprite):
    def __init__(self):
        super().__init__('falcon.png', 0.3)
        self.center_x = SCREEN_WIDTH / 2

        self.center_y = 100

    # 2 1обновление кадров
    def update(self):
        self.center_x += self.change_x


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture('background.jpg')
        self.falcon = Falcon()
        # 2 4скрыть мышку
        self.set_mouse_visible(False)
        # 2.8
        self.lasers = arcade.SpriteList()
        self.setup()

    # размешение обьектов на сцене или в игре
    def setup(self):
        pass

    # отрисовка спрайтов
    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.bg)
        self.falcon.draw()

    def update(self, delta_time: float):
        # 2 2вызов обновления
        self.falcon.update()

    # 2 3движения курсора мышки
    def on_mouse_motion(self, x, y, dx, dy):
        self.falcon.center_x = x


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)


arcade.run()
