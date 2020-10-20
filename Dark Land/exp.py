import pygame as pg
pg.init()
print(pg.font.get_fonts())
screen = pg.display.set_mode((250,250))
font = pg.font.SysFont("brushscript", 20)


while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            quit()
    text = font.render("text, 123456890", True, (255, 255, 0))
    screen.blit(text, [5,100])
    pg.display.update()

