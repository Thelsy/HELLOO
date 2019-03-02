#!/Users/lsy python
# coding:utf-8
# lsy
# 图像类
import pygame
class Ship():
    def __init__(self, screen, ai_settings):
        '''初始化飞船并设置初始问题'''
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像
        self.image = pygame.image.load('Alienware/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每个飞船位置置于屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 控制飞船移动速度
        self.center = float(self.rect.centerx)
        self.bottomx = float(self.rect.bottom)
        # 控制飞船移动方向
        self.moving = 0
        self.up = 0
    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
    def update(self):
        # 向右移动
        if self.moving == 2:
            # 控制向右移动，不允许移动出窗口外
            if self.rect.right < self.screen_rect.right:
                # 移动速度
                self.center += self.ai_settings.ship_speed_factor
        elif self.moving == 1:
            # 控制向左移动，不允许移动出窗口外
            if self.moving and self.rect.left > 0:
                # 移动速度
                self.center -= self.ai_settings.ship_speed_factor
        if self.up == 2:
            # 控制向下移动，不允许移动出窗口外
            if self.up and self.rect.bottom < self.screen_rect.bottom:
                # 移动速度
                self.bottomx += self.ai_settings.ship_speed_factor
        elif self.up == 1:
            # 控制向上移动，不允许移动出窗口外
            if self.up and self.rect.top > self.screen_rect.top:
                # 移动速度
                self.bottomx -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        self.rect.bottom = self.bottomx
