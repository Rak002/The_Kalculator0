from pygame import display,image,init
init()
screen = display.set_mode((307, 453))
display.set_caption("The Kalculator")

import pygame
from pygame import mixer
import math
import time

base=image.load(r'lib/img.png')
clck=image.load(r'lib/blank.png')
icon=image.load(r'lib/icon.png')
pygame.display.set_icon(icon)
screen.blit(base,(0,0))
pygame.display.update()

font = pygame.font.SysFont('Arial Bold', 40)
color=(0,0,0)
expressin=""
mn_expressin=""
result=""
f=False
operators=["+","-","*","/","(",")","sqrt","c","ac","="]

#_____________________________________________________________________________________________

def check_pos(x,y):
    pos=""
    if y>=130 and y<=202:
        if x>=17 and x<=73:
            pos="1"
        if x>=82 and x<=138:
            pos="2"
        if x>=143 and x<=199:
            pos="3"
    elif y>=210 and y<=281:
        if x>=17 and x<=73:
            pos="4"
        if x>=82 and x<=138:
            pos="5"
        if x>=143 and x<=199:
            pos="6"
    elif y>=292 and y<=363:
        if x>=17 and x<=73:
            pos="7"
        if x>=82 and x<=138:
            pos="8"
        if x>=143 and x<=199:
            pos="9"
    if y>=370 and y<=439 and x>=25 and x<=85:
        pos="0"
    if y>=370 and y<=439 and x>=145 and x<=210:
        pos="c"
    if y>=409 and y<=447 and x>=221 and x<=299:
        pos="ac"
    if y>=133 and y<=200:
        if x>=205 and x<=248:
            pos="+"
        if x>=253 and x<=297:
            pos="-"
    elif y>=212 and y<=279:
        if x>=205 and x<=248:
            pos="*"
        if x>=253 and x<=297:
            pos="/"
    if y>=368 and y<=402 and x>=221 and x<=292:
        pos="sqrt"
    if (34*x+43*y)<=20697 and x>=91 and y>=370:
        pos="("
    if (34*x+43*y)>=21471 and x<=139 and y<=427:
        pos=")"
    if y>=297 and y<=350 and x>=209 and x<=293:
        pos="="
        
    return pos

#__________________________________________________________________________________________________

def take_action(x):
    global expressin
    global mn_expressin
    global result
    global color
    global f
    
    if result!="" or expressin=="" or f==True:
        color=(0,0,0)
        expressin=""
        result=""
        f=False
    if x.isdigit():
        expressin+=x
    elif x in operators:
        if x=="sqrt":
            expressin+="sqrt("
        elif x=="ac":
            expressin=""
        elif x=="c":
            if expressin.endswith("sqrt("):
                expressin = expressin[:-5]
            else:
                expressin=expressin[:-1]     
        else:
            if x!="=":
                expressin+=x
    mn_expressin=expressin

#_________________________________________________________________________________________________

def set_expressin():
    global expressin
    global mn_expressin
    global operators
    lst=expressin.split("sqrt")
    mn_expressin=""
    for i in range(0,len(lst)):
        if i!=len(lst)-1:
            mn_expressin+=lst[i]+"math.sqrt"
        else:
            mn_expressin+=lst[i]
    print("mn_e",mn_expressin)

    if "(" in mn_expressin:
        lst2=mn_expressin.split("(")
        if lst2[-1]=="":
            lst2=lst2[:-1]
        x=""
        for i in range(0,len(lst2)):
            if (lst2[i].endswith("+") or lst2[i].endswith("-") or lst2[i].endswith("*") or lst2[i].endswith("/") or lst2[i].endswith("(") or lst2[i].endswith("sqrt") or lst2[i]=="") and i!=len(lst2)-1:
                x+=lst2[i]+"("
            else:
                if i!=len(lst2)-1:
                    x+=lst2[i]+"*("
                else:
                    x+=lst2[i]
        mn_expressin=x

    if ")" in mn_expressin:
        lst2=mn_expressin.split(")")
        x=""
        for i in range(0,len(lst2)-1):
            if (lst2[i+1].startswith("+") or lst2[i+1].startswith("-") or lst2[i+1].startswith("*") or lst2[i+1].startswith("/") or lst2[i+1].startswith("(") or lst2[i+1].startswith("sqrt") or lst2[i+1]=="") and i!=len(lst2)-1:
                x+=lst2[i]+")"
            else:
                x+=lst2[i]+")*"
        x+=lst2[-1]
        mn_expressin=x
    
    if "math.sqrt" in mn_expressin:
        lst3=mn_expressin.split("math.sqrt")
        if lst3[-1]=="":
            lst3=lst3[:-1]
        x=""
        for i in range(0,len(lst3)):
            if (lst3[i].endswith("+") or lst3[i].endswith("-") or lst3[i].endswith("*") or lst3[i].endswith("/") or lst3[i].endswith("(") or lst3[i].endswith(")") or lst3[i].endswith("sqrt(") or lst3[i]=="") and i!=len(lst3)-1:
                x+=lst3[i]+"math.sqrt"
            else:
                if i!=len(lst3)-1:
                    x+=lst3[i]+"*math.sqrt"
                else:
                    x+=lst3[i]
        mn_expressin=x


#___________________________________________________________________________________________________

running = True
while running:       
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
            pygame. quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            tp=pygame. mouse. get_pressed()
            if tp[0]==True:
                t1=pygame. mouse. get_pos()
                print("x=",t1[0])
                print("y=",t1[1])
                ps=check_pos(t1[0],t1[1])
                print("clicked on: ",ps)
                if len(expressin)<45 or (ps=="ac" or ps=="c"):
                    take_action(ps)
                if ps=="=":
                    color=(0,0,255)
                    set_expressin()
                    print("mn_expressin= ",mn_expressin)
                    
                    if mn_expressin!="":
                        try:
                            result=str(eval(mn_expressin))
                            mn_expressin=result
                            expressin=result
                        except:
                            result="ERROR!"
                            mn_expressin=""
                            expressin="ERROR!"
                screen.blit(base,(0,0))
                if ps!="*" and ps !="/" and ps!="":
                    clck=image.load('lib/clicks/'+ps+'.png')
                elif ps=="*":
                    clck=image.load('lib/clicks/x.png')
                elif ps=="/":
                    clck=image.load('lib/clicks/x2.png')
                elif ps=="":
                    clck=image.load(r'lib/blank.png')
                screen.blit(clck,(0,0))
                if ps !="":
                    try:
                        snd=pygame.mixer.Sound('lib/clicks/click_sound.wav')
                        snd.set_volume(0.09)
                        snd.play()
                    except:
                        pass
                if expressin=="ERROR!":
                    color=(255,0,0)
                if len(expressin)<15:
                    txt = font.render(expressin, True, color)
                    screen.blit(txt,(28,20))
                elif len(expressin)>=15 and len(expressin)<30:
                    txt1 = font.render(expressin[0:15], True, color)
                    txt2 = font.render(expressin[15:], True, color)
                    screen.blit(txt1,(28,20))
                    screen.blit(txt2,(28,45))
                elif len(expressin)>=30 and len(expressin)<45:
                    txt1 = font.render(expressin[0:15], True, color)
                    txt2 = font.render(expressin[15:30], True, color)
                    txt3 = font.render(expressin[30:45], True, color)
                    screen.blit(txt1,(28,20))
                    screen.blit(txt2,(28,45))
                    screen.blit(txt3,(28,70))
                elif len(expressin)>45:
                    txt = font.render("ERROR!", True, (255,0,0))
                    screen.blit(txt,(28,20))
                pygame.display.update()
                time.sleep(0.1)
                #blitting again to make the click
                screen.blit(base,(0,0))
                if len(expressin)<15:
                    txt = font.render(expressin, True, color)
                    screen.blit(txt,(28,20))
                elif len(expressin)>=15 and len(expressin)<30:
                    txt1 = font.render(expressin[0:15], True, color)
                    txt2 = font.render(expressin[15:], True, color)
                    screen.blit(txt1,(28,20))
                    screen.blit(txt2,(28,45))
                elif len(expressin)>=30 and len(expressin)<45:
                    txt1 = font.render(expressin[0:15], True, color)
                    txt2 = font.render(expressin[15:30], True, color)
                    txt3 = font.render(expressin[30:45], True, color)
                    screen.blit(txt1,(28,20))
                    screen.blit(txt2,(28,45))
                    screen.blit(txt3,(28,70))
                elif len(expressin)>44:
                    txt = font.render("OUT OF BOUNDS!", True, (255,0,0))
                    screen.blit(txt,(28,20))
                    f=True
                pygame.display.update()
                print('expressin= ',expressin)
                print('mn_expressin= ',mn_expressin)
                print("result :",result)
            

                    



    
