#!/Users/lsy python
# coding:utf-8
# lsy
# 飞机大战
# 导入pygame库
import pygame
import Alienware.game_functions as gh
from Alienware.settings import Settings
from Alienware.ship import Ship
def run():
    # 初始化pygame,为使用硬件做准备
    pygame.init()
    # 获取Settings类中的配置
    ai = Settings()
    # 创建了一个窗口
    screen = pygame.display.set_mode((ai.screen_width, ai.screen_height))
    # 设置窗口标题
    pygame.display.set_caption("飞机大战")
    # 创建飞船
    ship = Ship(screen, ai)
    while True:
        gh.check_events(ship)
        ship.update()
        gh.update(ai, screen, ship)

if __name__ == '__main__':
    run()
