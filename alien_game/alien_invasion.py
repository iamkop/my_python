import pygame as pg

from alien_game.settings import Settings
from alien_game.ship import Ship
import alien_game.game_functions as gf


def run_game():
    print("*" * 8 + " game is begin " + "*" * 8)

    ali_settings = Settings()
    # 初始化并创建一个屏幕对象
    pg.init()
    screen = pg.display.set_mode((ali_settings.screen_width, ali_settings.screen_height))
    pg.display.set_caption('外星生物入侵')
    # 创建一搜飞船
    ship = Ship(ali_settings, screen)
    print("*" * 8 + " create a ship " + "*" * 8)
    # 主循环
    while True:
        # 监听事件的代码
        gf.check_events(ship)
        ship.update()
        # 每次循环都重新绘制屏幕
        gf.update_screen(ali_settings, screen, ship)


run_game()
