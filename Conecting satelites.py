import pgzrun 
import random

WIDTH=600
HEIGHT=600

sats=[]


for i in range (10):
    satellite=Actor("satellite")
    satellite.x=random.randint(50,550)
    satellite.y=random.randint(50,550)
    sats.append(satellite)

def draw():
    na=1
    for i in sats:
        i.draw()
        screen.draw.text(str(na),(i.x,i.y+10))
        na=na+1



pgzrun.go()



