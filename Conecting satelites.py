import pgzrun 
import random
from time import time

WIDTH=600
HEIGHT=600

sats=[]
sat_num=0
line=[]
start=time()
total=0
#tns=

#creation of sats
for i in range (10):
    satellite=Actor("satellite")
    satellite.x=random.randint(50,550)
    satellite.y=random.randint(50,550)
    sats.append(satellite)

#on click lines

def on_mouse_down(pos):
    global sat_num,sats,line
    if sats[sat_num].collidepoint(pos):
        if sat_num >0:
            line.append((sats[sat_num-1].pos,sats[sat_num].pos))
            print(line)
        sat_num+=1
    else:
        line=[]
        sat_num=0











def draw():
    global total
    screen.blit("sat_background",(0,0))
    na=1
    for sat in sats:
        sat.draw()
        screen.draw.text(str(na),(sat.x,sat.y+15))
        na=na+1

    for l in line:
        screen.draw.line(l[0],l[1],"white")
    
    if sat_num<10:
        total=time()-start
        
        screen.draw.text(str(round(total,2)),(50,550))  
    else:
        screen.draw.text(str(round(total,2)),(50,550))   


def update():
    pass


pgzrun.go()



