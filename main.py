import pygame as pgm
import sys
import traceback
import scripts.enemy as enmy
from scripts.myplane import MyPlane

pgm.init()
pgm.mixer.init()

bg_size = width, height = 480, 700
screen = pgm.display.set_mode(bg_size)
pgm.display.set_caption("Plane Fight My Version")

background = pgm.image.load("images/background.png").convert()

# 载入音乐
pgm.mixer.music.load("sound/game_music.ogg")
pgm.mixer.music.set_volume(0.2)
bullet_sound = pgm.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pgm.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
supply_sound = pgm.mixer.Sound("sound/supply.wav")
supply_sound.set_volume(0.2)
get_bomb_sound = pgm.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pgm.mixer.Sound("sound/get_bullet.wav")
get_bullet_sound.set_volume(0.2)
upgrade_sound = pgm.mixer.Sound("sound/upgrade.wav")
upgrade_sound.set_volume(0.2)
enemy3_fly_sound = pgm.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
enemy1_down_sound = pgm.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pgm.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pgm.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.5)
me_down_sound = pgm.mixer.Sound("sound/me_down.wav")
me_down_sound.set_volume(0.2)


def add_small_enemies(group1: pgm.sprite.Group, group2: pgm.sprite.Group, num):
    for _ in range(num):
        e1 = enmy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1: pgm.sprite.Group, group2: pgm.sprite.Group, num):
    for _ in range(num):
        e2 = enmy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1: pgm.sprite.Group, group2: pgm.sprite.Group, num):
    for _ in range(num):
        e3 = enmy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    pgm.mixer.music.play(-1)

    # 实例化本机
    me = MyPlane(bg_size)

    # 实例化敌机
    enemies = pgm.sprite.Group()
    small_enemies: pgm.sprite.Group[enmy.SmallEnemy] = pgm.sprite.Group()
    add_small_enemies(small_enemies, enemies, 15)
    mid_enemies: pgm.sprite.Group[enmy.MidEnemy] = pgm.sprite.Group()
    add_mid_enemies(mid_enemies, enemies, 5)
    big_enemies: pgm.sprite.Group[enmy.BigEnemy] = pgm.sprite.Group()
    add_big_enemies(big_enemies, enemies, 5)

    # 用于切换图片
    switch_image = True

    # 用于延迟切换
    delay = 100

    # 游戏时钟
    clock = pgm.time.Clock()

    running = True
    while running:
        for event in pgm.event.get():
            if event.type == pgm.QUIT:
                pgm.quit()
                sys.exit()

        # 获取键盘输入 & 控制本机
        key_pressed = pgm.key.get_pressed()
        if key_pressed[pgm.K_w] or key_pressed[pgm.K_UP]:
            me.moveUp()
        if key_pressed[pgm.K_s] or key_pressed[pgm.K_DOWN]:
            me.moveDown()
        if key_pressed[pgm.K_a] or key_pressed[pgm.K_LEFT]:
            me.moveLeft()
        if key_pressed[pgm.K_d] or key_pressed[pgm.K_RIGHT]:
            me.moveRight()

        screen.blit(background, (0, 0))

        # 渲染大型机
        for each in big_enemies:
            each.move()
            if switch_image:
                screen.blit(each.image1, each.rect)
            else:
                screen.blit(each.image2, each.rect)
            if each.rect.bottom > -50:
                enemy3_fly_sound.play()

        for each in mid_enemies:
            each.move()
            screen.blit(each.image, each.rect)

        for each in small_enemies:
            each.move()
            screen.blit(each.image, each.rect)

        # 渲染本机
        if switch_image:
            screen.blit(me.image1, me.rect)
        else:
            screen.blit(me.image2, me.rect)
        if not (delay % 5):
            switch_image = not switch_image
        delay = delay - 1 if delay > 0 else 100

        pgm.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except BaseException:
        traceback.print_exc()
        pgm.quit()
        input()
