import pygame as pg
import time
import sys
from math import ceil
from math import sqrt
from random import randint
import string
import random

pg.init()

pg.display.set_caption('Решётка Кардано')

phrase_input = 'Спасибо Глебу Дудорову за помощь'
phrase_input = phrase_input.replace(' ', '')
dlinna_phrasi = len(phrase_input)
dlinna_tablici = ceil(sqrt(dlinna_phrasi))
if dlinna_tablici % 2 != 0:
    dlinna_tablici += 1

clock = pg.time.Clock()
pivot = [1300 // 2, 800 // 2]
offset = pg.math.Vector2()
angle = 0

Moi_Font = pg.font.Font(None, 40)
screen = pg.display.set_mode((1300, 800))
screen.fill('black')

table = [[0] * dlinna_tablici for _ in range(dlinna_tablici)]
letter_table = [['0'] * dlinna_tablici for q in range(dlinna_tablici)]

yellow_image_orig = pg.Surface((dlinna_tablici * 50, dlinna_tablici * 50))
yellow_image_orig.set_colorkey('black')
yellow_image_orig.fill('yellow')
yellow_image_copy = yellow_image_orig.copy()
yellow_image_orig.set_colorkey('black')
yellow_rect = yellow_image_orig.get_rect()
yellow_image_copy_rect = yellow_image_copy.get_rect()
yellow_rect.center = (1300 // 2, 800 // 2)
yellow_image_copy_rect.center = (1300 // 2, 800 // 2)
yellow_rect_center = yellow_rect.center
left_up_ugolY = yellow_rect_center[1] - (dlinna_tablici * 50) // 2
left_up_ugolX = yellow_rect_center[0] - (dlinna_tablici * 50) // 2

for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if n * dlinna_tablici + m < len(phrase_input):
            letter_table[n][m] = phrase_input[n * dlinna_tablici + m]
        else:
            letter_table[n][m] = random.choice(string.ascii_letters)
        Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
        time.sleep(0.1)
        screen.blit(Moi_text, (m * 50 + left_up_ugolX + 10, n * 50 + left_up_ugolY + 10))
        pg.display.flip()
        print(letter_table[n][m], end=' ')
    print()

time.sleep(2)
screen.blit(yellow_image_orig, yellow_rect)
pg.display.update()


def rotate(surface, angle, pivot, offset):
    rotated_image = pg.transform.rotate(surface, -angle)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    return rotated_image, rect


time.sleep(2)

k_1 = 1
COL = int((dlinna_tablici * dlinna_tablici) / 4)
proverka_1 = 0
first_pos = []
while proverka_1 < COL:
    i = randint(0, dlinna_tablici - 1)
    j = randint(0, dlinna_tablici - 1)
    if table[i][j] == 0:
        table[i][j] = 1
        table[j][dlinna_tablici - 1 - i] = 2
        table[dlinna_tablici - 1 - i][dlinna_tablici - 1 - j] = 3
        table[dlinna_tablici - 1 - j][dlinna_tablici - 1 - (dlinna_tablici - 1 - i)] = 4

        time.sleep(0.5)
        pg.draw.rect(yellow_image_orig, 'black', (j * 50 + 5, i * 50 + 5, 40, 40))
        pg.draw.rect(screen, 'black', (j * 50 + 5 + left_up_ugolX, i * 50 + 5 + left_up_ugolY, 40, 40))
        for n in range(dlinna_tablici):
            for m in range(dlinna_tablici):
                if table[n][m] == 1:
                    Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
                    screen.blit(Moi_text, (m * 50 + left_up_ugolX + 10, n * 50 + left_up_ugolY + 10))

        pg.display.update()
        proverka_1 += 1


second_pos = []
time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 1:
            k_1 += 1
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            for i in range(1, 32):
                x_1 = m * 50 + left_up_ugolX + 10
                y_1 = n * 50 + left_up_ugolY + 10
                x_2 = 35 * (k_1 - 1) + 10
                y_2 = 800 - 100





                screen.fill('black')
                screen.blit(yellow_image_orig, yellow_rect)
                screen.blit(Moi_text, (x_1 + ((x_2 - x_1) / 30) * (i - 1), y_1 + ((y_2 - y_1) / 30) * (i - 1)))

                for w in range(len(second_pos)):
                    screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

                clock.tick(30)
                pg.display.update()
            second_pos.append((x_2, y_2, Moi_text))

time.sleep(2)
while angle < 90:
    angle += 1
    rotated_image, rect = rotate(yellow_image_orig, angle, pivot, offset)
    screen.fill('black')
    screen.blit(rotated_image, rect)

    for w in range(len(second_pos)):
        screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

    pg.display.flip()
    clock.tick(30)

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 2:
            time.sleep(0.5)
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            screen.blit(Moi_text, (m * 50 + left_up_ugolX + 10, n * 50 + left_up_ugolY + 10))
            pg.display.update()

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 2:
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            k_1 += 1
            for i in range(1, 32):
                x_1 = m * 50 + left_up_ugolX + 10
                y_1 = n * 50 + left_up_ugolY + 10
                x_2 = 35 * (k_1 - 1) + 5
                y_2 = 800 - 100
                screen.fill('black')
                screen.blit(rotated_image, rect)
                screen.blit(Moi_text, (x_1 + ((x_2 - x_1) / 30) * (i - 1), y_1 + ((y_2 - y_1) / 30) * (i - 1)))
                for w in range(len(second_pos)):
                    screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

                clock.tick(30)
                pg.display.update()
            second_pos.append((x_2, y_2, Moi_text))



time.sleep(3)
while angle < 180:
    angle += 1
    rotated_image, rect = rotate(yellow_image_orig, angle, pivot, offset)
    screen.fill('black')
    screen.blit(rotated_image, rect)

    for w in range(len(second_pos)):
        screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

    pg.display.update()
    clock.tick(30)

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 3:
            time.sleep(0.5)
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            screen.blit(Moi_text, (m * 50 + left_up_ugolX + 10, n * 50 + left_up_ugolY + 10))
            pg.display.update()

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 3:
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            k_1 += 1
            for i in range(1, 32):
                x_1 = m * 50 + left_up_ugolX + 10
                y_1 = n * 50 + left_up_ugolY + 10
                x_2 = 35 * (k_1 - 1) + 5
                y_2 = 800 - 100
                screen.fill('black')
                screen.blit(rotated_image, rect)
                screen.blit(Moi_text, (x_1 + ((x_2 - x_1) / 30) * (i - 1), y_1 + ((y_2 - y_1) / 30) * (i - 1)))

                for w in range(len(second_pos)):
                    screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

                clock.tick(30)
                pg.display.update()
            second_pos.append((x_2, y_2, Moi_text))

time.sleep(3)
while angle < 270:
    angle += 1
    rotated_image, rect = rotate(yellow_image_orig, angle, pivot, offset)
    screen.fill('black')
    screen.blit(rotated_image, rect)
    for w in range(len(second_pos)):
        screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))
    pg.display.flip()
    clock.tick(30)

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 4:
            time.sleep(0.5)
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            screen.blit(Moi_text, (m * 50 + left_up_ugolX + 10, n * 50 + left_up_ugolY + 10))
            pg.display.update()

time.sleep(1)
for n in range(dlinna_tablici):
    for m in range(dlinna_tablici):
        if table[n][m] == 4:
            Moi_text = Moi_Font.render(letter_table[n][m], 0, 'white')
            k_1 += 1
            for i in range(1, 32):
                x_1 = m * 50 + left_up_ugolX + 10
                y_1 = n * 50 + left_up_ugolY + 10
                x_2 = 35 * (k_1 - 1) + 5
                y_2 = 800 - 100
                screen.fill('black')
                screen.blit(rotated_image, rect)
                screen.blit(Moi_text, (x_1 + ((x_2 - x_1) / 30) * (i - 1), y_1 + ((y_2 - y_1) / 30) * (i - 1)))
                for w in range(len(second_pos)):
                    screen.blit(second_pos[w][2], (second_pos[w][0], second_pos[w][1]))

                clock.tick(30)
                pg.display.update()
            second_pos.append((x_2, y_2, Moi_text))

print()

for i in range(len(table)):
    for j in range(len(table)):
        print(table[i][j], end=' ')
    print()

print()

for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 1:
            a = letter_table[i][j]
            print(a, end='')

for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 2:
            b = letter_table[i][j]
            print(b, end='')

for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 3:
            c = letter_table[i][j]
            print(c, end='')

for i in range(len(table)):
    for j in range(len(table)):
        if table[i][j] == 4:
            d = letter_table[i][j]
            print(d, end='')


pg.display.update()
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()