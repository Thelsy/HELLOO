#!/Users/lsy python
# coding:utf-8
# lsy
# 图像类
import pygame

class Ship():
    def __init__(self, screen):
        '''初始化飞船并设置初始问题'''
        self.screen = screen
        # 加载飞船图像
        self.image = pygame.image.load('Alienware/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个飞船位置置于屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving = 0
        self.up = 0
    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
    def update(self):
        if self.moving == 2:
            self.rect.centerx += 1
        elif self.moving == 1:
            self.rect.centerx -= 1
        if self.up == 2:
            self.rect.bottom += 1
        elif self.up == 1:
            self.rect.bottom -= 1
