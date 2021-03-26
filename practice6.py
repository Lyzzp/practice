# coding=UTF-8
"""
@Time：2021/3/22 14:28
@Author：Administrator
@Project:pythonProject1
@Name:practice6 
"""
import pygame
import sys
import random
# from pygame.locals import *

# 初始化
pygame.init()  # 初始化pygame
pygame.mixer.init()  # 初始化混音器

# 制作窗口
playSurface = pygame.display.set_mode((800, 800))  # 定义窗口大小
pygame.display.set_caption("贪吃蛇")  # 定义标题

# 添加音乐
pygame.mixer.music.load("贪吃蛇背景音乐.mp3")
pygame.mixer.music.play(-1)


# 结束游戏
def gameover():
    pygame.quit()  # 退出pygame窗口
    sys.exit()  # 退出程序


# 颜色设置
snakeBody_color = pygame.Color(0, 255, 0)  # 绿色
food_color = pygame.Color(255, 0, 0)  # 红色


def main():
    time_clock = pygame.time.Clock()  # 定义一个变量来控制速度

    # 绘制蛇与果实
    snakePosition = [200, 200]  # 蛇头位置
    snakeBodys = [[200, 200], [180, 200], [160, 200]]  # 蛇身位置
    foodPosition = [500, 500]  # 果实位置
    foodTotal = 1  # 果实数量
    foodNumber = 1  # 用于增加速度的变量
    direction = 'right'  # 初始方向向右
    changeDirection = direction  # 定义一个改变方向的变量，按键

    speed = 4  # 定义初始速度

    while True:
        for event in pygame.event.get():  # 从队列中获取事件

            # 退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # 按键事件
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    changeDirection = 'right'

                if event.key == K_LEFT or event.key == K_a:
                    changeDirection = 'left'

                if event.key == K_UP or event.key == K_w:
                    changeDirection = 'up'

                if event.key == K_DOWN or event.key == K_s:
                    changeDirection = 'down'

                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))

        # 防止蛇反方向移动
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection

        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection

        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection

        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection

        # 根据方向移动蛇头
        if direction == 'right':
            snakePosition[0] += 20

        if direction == 'left':
            snakePosition[0] -= 20

        if direction == 'up':
            snakePosition[1] -= 20

        if direction == 'down':
            snakePosition[1] += 20

        snakeBodys.insert(0, list(snakePosition))  # 增加蛇的长度

        # 判断是否吃到食物
        if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
            foodTotal = 0
        else:
            snakeBodys.pop()  # 每次将最后一个单位的蛇身去除列表

        # 重新生成食物
        if foodTotal == 0:
            x = random.randrange(1, 40)
            y = random.randrange(1, 40)
            foodPosition = [int(x * 20), int(y * 20)]
            foodTotal = 1
            foodNumber += 1

            # 防止食物生成在蛇身上
        for body in snakeBodys[1:]:
            if foodPosition[0] == body[0] and foodPosition[1] == body[1]:
                foodTotal = 0
                foodNumber -= 1

        # 设置递增速度
        if foodNumber % 5 == 0:
            speed += 1
            foodNumber = 1

        # 绘制游戏背景
        background = pygame.image.load("河海大学校标.jpg")
        playSurface.blit(background, (0, 0))
        pygame.display.update()

        # 画出蛇与果实
        for position in snakeBodys:
            pygame.draw.rect(playSurface, snakeBody_color, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, food_color, Rect(foodPosition[0], foodPosition[1], 20, 20))

        pygame.display.flip()  # 更新显示到屏幕表面

        # 超出边框结束游戏
        if snakePosition[0] > 800 or snakePosition[0] < 0:
            gameover()

        elif snakePosition[1] > 800 or snakePosition[1] < 0:
            gameover()

        # 碰到身体结束游戏
        for body in snakeBodys[1:]:
            if snakePosition[0] == body[0] and snakePosition[1] == body[1]:
                gameover()

        # 控制游戏速度
        time_clock.tick(speed)


# 入口函数
if __name__ == "__main__":
    main()
