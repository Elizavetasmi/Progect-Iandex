import pygame, sys, random
from pygame.locals import *


#задаём необходимые параметры
#размера окна
BW = 4
BH = 4
TS = 80
WW = 640
WH = 480
#скорость
FPS = 31
BLANK = None
#цвета 1
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
BB =    (  0,  50, 255)
DT = (  3,  54,  73)
GREEN =         (255,   0,   0)
#цвета 2
BG = DT
TC = GREEN
TR = WHITE
BR = BB
BE = 20
BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK
MR = WHITE
XN = int((WW - (TS * BW + (BW - 1))) / 2)
YN = int((WH - (TS * BH + (BH - 1))) / 2)
#вверх
UP = 'up'
#вниз
DOWN = 'down'
#влево
LEFT = 'left'
#вправо
RIGHT = 'right'


def main():
    #глобальные переменные
    global FK, DF, BT, RF, RT, NF, NT, SF, ST
    pygame.init()
    FK = pygame.time.Clock()
    DF = pygame.display.set_mode((WW, WH))
    # текст 1
    pygame.display.set_caption('Слайд-головоломка')
    BT = pygame.font.Font('freesansbold.ttf', BE)
    RF, RT = fff('Сброс',    TR, TC, WW - 120, WH - 90)
    NF, NT = fff('Новая игра', TR, TC, WW - 120, WH - 60)
    SF, ST = fff('Решение',    TR, TC, WW - 120, WH - 30)
    md, sq = gle(80)
    SD = www()
    al = []
    while True:
        sl = None
        #текст 2
        msg = 'Нажмите клавиши со стрелками или плитку, чтобы сдвинуть.'
        if md == SD:
            msg = 'Решено!'
        dvb(md, msg)
        aaa()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                sx, sy = nnn(md, event.pos[0], event.pos[1])
                if (sx, sy) == (None, None):
                    if RT.collidepoint(event.pos):
                        ron(md, al)
                        al = []
                    elif NT.collidepoint(event.pos):
                        md, sq = gle(80)
                        al = []
                    elif ST.collidepoint(event.pos):
                        ron(md, sq + al)
                        al = []
                else:
                    bx, by = vvv(md)
                    if sx == bx + 1 and sy == by:
                        sl = LEFT
                    elif sx == bx - 1 and sy == by:
                        sl = RIGHT
                    elif sx == bx and sy == by + 1:
                        sl = UP
                    elif sx == bx and sy == by - 1:
                        sl = DOWN

            elif event.type == KEYUP:
                if event.key in (K_LEFT, K_a) and\
                        iii(md, LEFT):
                    sl = LEFT
                elif event.key in (K_RIGHT, K_d) and\
                        iii(md, RIGHT):
                    sl = RIGHT
                elif event.key in (K_UP, K_w) and\
                        iii(md, UP):
                    sl = UP
                elif event.key in (K_DOWN, K_s) and\
                        iii(md, DOWN):
                    sl = DOWN
        if sl:
            # текст 3
            slp(md, sl, 'Нажмите клавиши со стрелками или плитку, чтобы сдвинуть.', 8)
            mmm(md, sl)
            al.append(sl)
        pygame.display.update()
        FK.tick(FPS)


def qqq():
    pygame.quit()
    sys.exit()


def aaa():
    for event in pygame.event.get(QUIT):
        qqq()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            qqq()
        pygame.event.post(event)


def www():
    ee = 1
    rr = []
    for x in range(BW):
        dd = []
        for y in range(BH):
            dd.append(ee)
            ee += BW
        rr.append(dd)
        ee -= BW * (BH - 1) + BW - 1
    rr[BW - 1][BH - 1] = BLANK
    return rr


def vvv(tt):
    for x in range(BW):
        for y in range(BH):
            if tt[x][y] == BLANK:
                return (x, y)


def mmm(p, k):
    x, y = vvv(p)
    if k == UP:
        p[x][y], p[x][y + 1] =\
            p[x][y + 1], p[x][y]
    elif k == DOWN:
        p[x][y], p[x][y - 1] =\
            p[x][y - 1], p[x][y]
    elif k == LEFT:
        p[x][y], p[x + 1][y] =\
            p[x + 1][y], p[x][y]
    elif k == RIGHT:
        p[x][y], p[x - 1][y] =\
            p[x - 1][y], p[x][y]


def iii(d, m):
    x, y = vvv(d)
    return (m == UP and y != len(d[0]) - 1) or \
           (m == DOWN and y != 0) or \
           (m == LEFT and x != len(d) - 1) or \
           (m == RIGHT and x != 0)


def kkk(t, lastMove=None):
    validMoves = [UP, DOWN, LEFT, RIGHT]
    if lastMove == UP or not iii(t, DOWN):
        validMoves.remove(DOWN)
    if lastMove == DOWN or not iii(t, UP):
        validMoves.remove(UP)
    if lastMove == LEFT or not iii(t, RIGHT):
        validMoves.remove(RIGHT)
    if lastMove == RIGHT or not iii(t, LEFT):
        validMoves.remove(LEFT)
    return random.choice(validMoves)


def jjj(X, Y):
    left = XN + (X * TS) + (X - 1)
    top = YN + (Y * TS) + (Y - 1)
    return (left, top)


def nnn(board, x, y):
    for tileX in range(len(board)):
        for tileY in range(len(board[0])):
            left, top = jjj(tileX, tileY)
            uu = pygame.Rect(left, top, TS, TS)
            if uu.collidepoint(x, y):
                return (tileX, tileY)
    return (None, None)


def zzz(x, y, c, adjx=0, adjy=0):
    left, top = jjj(x, y)
    pygame.draw.rect(DF, TC, (left + adjx,\
                              top + adjy, TS, TS))
    h = BT.render(str(c), True, TR)
    kl = h.get_rect()
    kl.center = left + int(TS / 2) + adjx,\
                top + int(TS / 2) + adjy
    DF.blit(h, kl)


def fff(t, c, m, n, b):
    zx = BT.render(t, True, c, m)
    xc = zx.get_rect()
    xc.topleft = (n, b)
    return (zx, xc)


def dvb(r, lp):
    DF.fill(BG)
    if lp:
        textSurf, textRect = fff(lp, MR, BG, 5, 5)
        DF.blit(textSurf, textRect)
    for x in range(len(r)):
        for y in range(len(r[0])):
            if r[x][y]:
                zzz(x, y, r[x][y])
    left, top = jjj(0, 0)
    w = BW * TS
    h = BH * TS
    pygame.draw.rect(DF, BR, (left - 5, top - 5, w + 11, h + 11), 4)
    DF.blit(RF, RT)
    DF.blit(NF, NT)
    DF.blit(SF, ST)


def slp(b, d, m, animationSpeed):
    x, y = vvv(b)
    if d == UP:
        mx = x
        my = y + 1
    elif d == DOWN:
        mx = x
        my = y - 1
    elif d == LEFT:
        mx = x + 1
        my = y
    elif d == RIGHT:
        mx = x - 1
        my = y
    dvb(b, m)
    bf = DF.copy()
    mt, mp = jjj(mx, my)
    pygame.draw.rect(bf, BG, (mt, mp, TS, TS))
    for i in range(0, TS, animationSpeed):
        aaa()
        DF.blit(bf, (0, 0))
        if d == UP:
            zzz(mx, my, b[mx][my], 0, -i)
        if d == DOWN:
            zzz(mx, my, b[mx][my], 0, i)
        if d == LEFT:
            zzz(mx, my, b[mx][my], -i, 0)
        if d == RIGHT:
            zzz(mx, my, b[mx][my], i, 0)
        pygame.display.update()
        FK.tick(FPS)


#создание комбинаций
def gle(ns):
    s = []
    b = www()
    dvb(b, '')
    pygame.display.update()
    pygame.time.wait(500)
    lve = None
    for i in range(ns):
        m = kkk(b, lve)
        slp(b, m, 'Создание новой головоломки...', animationSpeed=int(TS / 3))
        mmm(b, m)
        s.append(m)
        lve = m
    return (b, s)


def ron(b, als):
    res = als[:]
    res.reverse()
    for i in res:
        if i == UP:
            oppositeMove = DOWN
        elif i == DOWN:
            oppositeMove = UP
        elif i == RIGHT:
            oppositeMove = LEFT
        elif i == LEFT:
            oppositeMove = RIGHT
        slp(b, oppositeMove, '', animationSpeed=int(TS / 2))
        mmm(b, oppositeMove)


if __name__ == '__main__':
    main()