#!/usr/bin/python3
from plane_sprites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组
        self.__create_sprites()

        # 4.设置定时器事件 - 创建敌机(1000毫秒一个)
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        # 5.发射子弹事件
        pygame.time.set_timer(PLAYER_FIRE_EVENT, 500)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        # 两张背景实现无缝滚动
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建玩家的精灵和精灵组
        self.player = PlayerPlane()
        self.player_group = pygame.sprite.Group(self.player)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):

        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # 创建敌机精灵
                enemy = Enemy()

                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == PLAYER_FIRE_EVENT:
                self.player.fire()

        #  移动事件
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.player.speed = PLAYER_SPEED
        elif keys_pressed[pygame.K_LEFT]:
            self.player.speed = -PLAYER_SPEED
        elif keys_pressed[pygame.K_UP]:
            self.player.y_speed = -PLAYER_SPEED
        elif keys_pressed[pygame.K_DOWN]:
            self.player.y_speed = PLAYER_SPEED
        else:
            self.player.speed = 0
            self.player.y_speed = 0

    def __check_collide(self):

        # 1.子弹摧毁敌机
        enemy_down_dict = pygame.sprite.groupcollide(self.player.bullets, self.enemy_group, True, True)
        if enemy_down_dict:
            self.player.score += 1
            # 替换图片

        # 2.敌机撞毁玩家
        enemies = pygame.sprite.spritecollide(self.player, self.enemy_group, False)

        # 判断列表是否有内容
        if len(enemies) > 0:
            # 玩家牺牲
            self.player.kill()
            print("游戏分数为：%d" % self.player.score)
            # 结束游戏
            PlaneGame.__game_over()

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.player_group.update()
        self.player_group.draw(self.screen)

        self.player.bullets.update()
        self.player.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == '__main__':
    # 创建游戏对象
    game = PlaneGame()

    # 启动游戏
    game.start_game()
