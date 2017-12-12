import sys
import pygame as pg


def check_keydown_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    if event.key == pg.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    if event.key == pg.K_LEFT:
        ship.moving_left = False


def check_events(ship):
    # 监视键盘和鼠标事件
    for event in pg.event.get():
        # 点 X 退出
        if event.type == pg.QUIT:
            print("*" * 8 + " game is quited " + "*" * 8)
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最近绘制的屏幕课间
    pg.display.flip()
