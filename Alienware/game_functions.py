#!/Users/lsy python
# coding:utf-8
# lsy
import sys
import pygame
def check_events(ship):
    '''响应用户操作'''
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_RIGHT:
                # 向右移动飞船
                ship.moving = 2
            elif events.key == pygame.K_LEFT:
                ship.moving = 1
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_UP:
                ship.up = 1
            elif events.key == pygame.K_DOWN:
                ship.up = 2
def update(ai_settings, screen, ship):
    '''更新位图操作'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()

