import pyautogui,pygame,sys,time
from pygame.locals import *

MainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("Müqqemmmlee efsane makro BY @Yazlimchi")

monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
screen_size = [800,600]

scene = "menu"

screen = pygame.display.set_mode(screen_size,pygame.RESIZABLE)

#ith open("Data.txt", "r", encoding="utf-8")as file:
#   Data_t = file.readlines()
#   scale = int(Data_t[4])
#   lvl = int(Data_t[3])
#   screen_size[0] = int(Data_t[0])
#   screen_size[1] = int(Data_t[1])
#
#f int(Data_t[2]) == 1:
#   
#   ex = (screen_size[0]) /2
#   ey = (screen_size[1]) /2
#lse:
#   screen = pygame.display.set_mode(monitor_size,pygame.FULLSCREEN)
#   ex = (monitor_size[0]) /2
#   ey = (monitor_size[1]) /2

mx, my = pygame.mouse.get_pos()

kapak = pygame.image.load("kapak.png")
pygame.display.set_icon(kapak)

font = pygame.font.SysFont("None", 32)


run = pygame.image.load("run.png")
run = pygame.transform.scale(run,(32,32))
runr = run.get_rect()
runr.x,runr.y = 2,2

stop = pygame.image.load("stop.png")
stop = pygame.transform.scale(stop,(32,32))
stopr = stop.get_rect()
stopr.x,stopr.y = 36,2

save = pygame.image.load("save.png")
save = pygame.transform.scale(save,(32,32))
saver = save.get_rect()
saver.x,saver.y = 72,2

ayar = pygame.image.load("ayar.png")
ayar = pygame.transform.scale(ayar,(32,32))
ayarr = ayar.get_rect()
ayarr.x,ayarr.y = screen_size[0]-200,8+(((my-8)//32)*32)

cop = pygame.image.load("cop.png")
cop = pygame.transform.scale(cop,(32,32))
copr = cop.get_rect()
copr.x,copr.y = screen_size[0]-164,8+(((my-8)//32)*32)

i = pygame.image.load("i.png")
i = pygame.transform.scale(i,(32,32))
ir = i.get_rect()
ir.x,ir.y = screen_size[0]-236,8+(((my-8)//32)*32)

click = pygame.image.load("clck.png")
clickr = click.get_rect()
clickr.x,clickr.y = screen_size[0]-130,36*1+2

mdown = pygame.image.load("mdown.png")
mdownr = mdown.get_rect()
mdownr.x,mdownr.y = screen_size[0]-130,36*2+2

mup = pygame.image.load("mup.png")
mupr = mup.get_rect()
mupr.x,mupr.y = screen_size[0]-130,36*3+2

move = pygame.image.load("move.png")
mover = move.get_rect()
mover.x,mover.y = screen_size[0]-130,36*4+2

moverl = pygame.image.load("moverl.png")
moverlr = moverl.get_rect()
moverlr.x,moverlr.y = screen_size[0]-130,36*5+2

write = pygame.image.load("write.png")
writer = write.get_rect()
writer.x,writer.y = screen_size[0]-130,36*6+2

press = pygame.image.load("press.png")
pressr = press.get_rect()
pressr.x,pressr.y =screen_size[0]-130,36*7+2

down = pygame.image.load("down.png")
downr = down.get_rect()
downr.x,downr.y =screen_size[0]-130,36*8+2

up = pygame.image.load("up.png")
upr = up.get_rect()
upr.x,upr.y =screen_size[0]-130,36*9+2

hotkey = pygame.image.load("hotkey.png")
hotkeyr = hotkey.get_rect()
hotkeyr.x,hotkeyr.y =screen_size[0]-130,36*10+2

ss = pygame.image.load("ss.png")
ssr = ss.get_rect()
ssr.x,ssr.y =screen_size[0]-130,36*11+2

slep = pygame.image.load("slep.png")
slepr = slep.get_rect()
slepr.x,slepr.y =screen_size[0]-130,36*12+2


msira = []


mrect = pygame.Rect(1,1,1,1)

def makro():
    global msira
    global sira
    sira = 0
    while sira<len(msira):
        if msira[sira][0] == 0:
            pyautogui.click(button=msira[sira][1])
        elif msira[sira][0] == 1:
            pyautogui.mouseDown(button=msira[sira][1])
        elif msira[sira][0] == 2:
            pyautogui.mouseUp(button=msira[sira][1])
        elif msira[sira][0] == 3:
            pyautogui.moveTo(msira[sira][1],msira[sira][2])
        elif msira[sira][0] == 4:
            pyautogui.moveRel((msira[sira][1],msira[sira][2]))
        elif msira[sira][0] == 5:
            pyautogui.typewrite(msira[sira][1])
        elif msira[sira][0] == 6:
            pyautogui.press(msira[sira][1])
        elif msira[sira][0] == 7:
            pyautogui.keyDown(msira[sira][1])
        elif msira[sira][0] == 8:
            pyautogui.keyUp(msira[sira][1])
        #elif msira[sira][0] == 9:
        #    pyautogui.hotkey(pyautogui.hotkey(msira[sira][1]))
        elif msira[sira][0] == 10:
            pyautogui.screenshot(msira[sira][1])
        elif msira[sira][0] == 11:
            time.sleep(msira[sira][1])
        sira += 1
bs = 0
ma = 0

while True:
    screen.fill((30,30,30))
    pygame.draw.rect(screen,(20,20,20),(0,36,screen_size[0]-134,screen_size[1]))
    #pygame.draw.rect(screen,(0,0,0),(screen_size[0]-146,36,12,screen_size[1]))
    key = pygame.key.get_pressed()
    mx, my = pygame.mouse.get_pos()
    mrect.x,mrect.y = mx, my

    pygame.draw.rect(screen,(50,50,50),(0,8+(((my-8)//32)*32),screen_size[0]-134,32))
    ma = (my-8-bs)//32
    copr.y = ((my-8)//32)*32+8
    screen.blit(cop,copr)
    ayarr.y = ((my-8)//32)*32+8
    screen.blit(ayar,ayarr)
    ir.y = ((my-8)//32)*32+8
    screen.blit(i,ir)
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            screen_size = [screen.get_width(),screen.get_height()]
            clickr.x,clickr.y = screen_size[0]-130,2+36
            mdownr.x,mdownr.y = screen_size[0]-130,36*2+2
            mupr.x,mupr.y = screen_size[0]-130,36*3+2
            mover.x,mover.y = screen_size[0]-130,36*4+2
            moverlr.x,moverlr.y = screen_size[0]-130,36*5+2
            writer.x,writer.y = screen_size[0]-130,36*6+2
            pressr.x,pressr.y =screen_size[0]-130,36*7+2
            downr.x,downr.y =screen_size[0]-130,36*8+2
            upr.x,upr.y =screen_size[0]-130,36*9+2
            hotkeyr.x,hotkeyr.y =screen_size[0]-130,36*10+2
            ssr.x,ssr.y =screen_size[0]-130,36*11+2
            slepr.x,slepr.y =screen_size[0]-130,36*12+2
            copr.x,copr.y = screen_size[0]-164,8+(((my-8)//32)*32)
            ir.x,ir.y = screen_size[0]-236,8+(((my-8)//32)*32)
            ayarr.x,ayarr.y = screen_size[0]-200,8+(((my-8)//32)*32)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            pass
        if event.type == MOUSEBUTTONDOWN:
            if event.button== 1:
                if mrect.colliderect(clickr):
                    msira.append([0,"left"])
                if mrect.colliderect(mdownr):
                    msira.append([1,"left"])
                if mrect.colliderect(mupr):
                    msira.append([2,"left"])
                if mrect.colliderect(mover):
                    msira.append([3,0,0])
                if mrect.colliderect(moverlr):
                    msira.append([4,0,0])
                if mrect.colliderect(writer):
                    msira.append([5,""])
                if mrect.colliderect(pressr):
                    msira.append([6,""])
                if mrect.colliderect(downr):
                    msira.append([7,""])
                if mrect.colliderect(upr):
                    msira.append([8,""])
                #if mrect.colliderect(hotkeyr):
                #    msira.append([9,["ctrl","v"]])
                if mrect.colliderect(ssr):
                    msira.append([10,"screenshot.png"])
                if mrect.colliderect(slepr):
                    msira.append([11,1])
                if mrect.colliderect(copr):
                    if ma >-1 and len(msira)>0:
                        msira.pop(ma-1)
                if mrect.colliderect(ayarr):
                    if ma >-1 and len(msira)>0:
                        if msira[ma-1][0]==0:
                            msira[ma-1][1]=pyautogui.prompt(text='Mause Butonu (left,right) :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]="left"
                        elif msira[ma-1][0]==1:
                            msira[ma-1][1]=pyautogui.prompt(text='Mause Butonu (left,right) :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]="left"
                        elif msira[ma-1][0]==2:
                            msira[ma-1][1]=pyautogui.prompt(text='Mause Butonu (left,right) :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]="left"
                        elif msira[ma-1][0]==3:
                            q = msira[ma-1][1]
                            msira[ma-1][1]=int(pyautogui.prompt(text='gidilecek x konumu', title='Ayar'))
                            if msira[ma-1][1]==None:
                                msira[ma-1][1]=q
                            q = msira[ma-1][2]
                            msira[ma-1][2]=int(pyautogui.prompt(text='gidilecek y konumu', title='Ayar'))
                            if msira[ma-1][2]==None:
                                msira[ma-1][2]=q
                        elif msira[ma-1][0]==4:
                            q = msira[ma-1][1]
                            msira[ma-1][1]=int(pyautogui.prompt(text='arttırılacak x konumu', title='Ayar'))
                            if msira[ma-1][1]==None:
                                msira[ma-1][1]=q
                            q = msira[ma-1][2]
                            msira[ma-1][2]=int(pyautogui.prompt(text='arttırılacak y konumu', title='Ayar'))
                            if msira[ma-1][2]==None:
                                msira[ma-1][2]=q
                        elif msira[ma-1][0]==5:
                            msira[ma-1][1]=pyautogui.prompt(text='Yazılacak Yazı :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]=""
                        elif msira[ma-1][0]==6:
                            msira[ma-1][1]=pyautogui.prompt(text='Basılacak tuş :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]=""
                        elif msira[ma-1][0]==7:
                            msira[ma-1][1]=pyautogui.prompt(text='Basılı tutulacak tuş :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]=""
                        elif msira[ma-1][0]==8:
                            msira[ma-1][1]=pyautogui.prompt(text='çekilen tuş :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]=""
                        elif msira[ma-1][0]==10:
                            msira[ma-1][1]=pyautogui.prompt(text='Dosya Adı :', title='Ayar')
                            if msira[ma-1][1]== None:
                                msira[ma-1][1]="screenshot.png"
                        #elif msira[ma-1][0]==9:
                        #    msira[ma-1][1][0]=pyautogui.prompt(text='1. tuş :', title='Ayar')
                        #    if msira[ma-1][1][0]== None:
                        #        msira[ma-1][1][0]=""
                        elif msira[ma-1][0]==11:
                            q = pyautogui.prompt(text='Bekleme Süresi :', title='Ayar')
                            if q== None:
                                msira[ma-1][1]=1
                            else:
                                msira[ma-1][1]=float(q)
                if mrect.colliderect(runr):
                    screen.fill((0,0,0))
                    yazi = font.render("Makro Çalışırken Bu Pencereye Tıklamayın",True,(255,255,255))
                    screen.blit(yazi,((screen_size[0]//2)-(yazi.get_width()//2),(screen_size[1]//2)-(yazi.get_height()//2)))
                    MainClock.tick(60)
                    pygame.display.update()
                    makro()
                if mrect.colliderect(stopr):
                    pyautogui.alert(text="UYGULAMA HENÜZ TAMAMLANMADI TAMAMLANINCA DİSCORD'DAN HABER VERİRİM", title='BU BUTON AKTİF DEĞİL', button='OK')
                if mrect.colliderect(saver):
                    pyautogui.alert(text="UYGULAMA HENÜZ TAMAMLANMADI TAMAMLANINCA DİSCORD'DAN HABER VERİRİM", title='BU BUTON AKTİF DEĞİL', button='OK')
                if mrect.colliderect(ir):
                    pyautogui.alert(text="UYGULAMA HENÜZ TAMAMLANMADI TAMAMLANINCA DİSCORD'DAN HABER VERİRİM", title='BU BUTON AKTİF DEĞİL', button='OK')
                if mrect.colliderect(hotkeyr):
                    pyautogui.alert(text="UYGULAMA HENÜZ TAMAMLANMADI TAMAMLANINCA DİSCORD'DAN HABER VERİRİM", title='BU BUTON AKTİF DEĞİL', button='OK')
            if event.button == 4:
                bs+= 32
            if event.button == 5:
                bs-= 32

    screen.blit(click,clickr)
    screen.blit(mdown,mdownr)
    screen.blit(mup,mupr)
    screen.blit(move,mover)
    screen.blit(moverl,moverlr)
    screen.blit(write,writer)
    screen.blit(press,pressr)
    screen.blit(down,downr)
    screen.blit(up,upr)
    screen.blit(hotkey,hotkeyr)
    screen.blit(ss,ssr)
    screen.blit(slep,slepr)


    sira = len(msira)-1
    while sira>-1:
        if msira[sira][0] == 0:
            screen.blit(click,(4,sira*32+40+bs))
            yazi = font.render("Mouse Tuşu : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 1:
            screen.blit(mdown,(4,sira*32+40+bs))
            yazi = font.render("Mouse Tuşu : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 2:
            screen.blit(mup,(4,sira*32+40+bs))
            yazi = font.render("Mouse Tuşu : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 3:
            screen.blit(move,(4,sira*32+40+bs))
            yazi = font.render("X : "+str(msira[sira][1])+" | Y : "+str(msira[sira][2]),True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 4:
            screen.blit(moverl,(4,sira*32+40+bs))
            yazi = font.render("+X : "+str(msira[sira][1])+" | +Y : "+str(msira[sira][2]),True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 5:
            screen.blit(write,(4,sira*32+40+bs))
            yazi = font.render("Yazı : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 6:
            screen.blit(press,(4,sira*32+40+bs))
            yazi = font.render("Tuş : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 7:
            screen.blit(down,(4,sira*32+40+bs))
            yazi = font.render("Tuş : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 8:
            screen.blit(up,(4,sira*32+40+bs))
            yazi = font.render("Tuş : "+msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        #elif msira[sira][0] == 9:
        #    screen.blit(hotkey,(4,sira*32+40+bs))
        #    if len(msira[sira][1]) == 2:
        #        yazi = font.render("Tuşlar : "+msira[sira][1][0]+","+msira[sira][1][1],True,(255,255,255))
        #        screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 10:
            screen.blit(ss,(4,sira*32+40+bs))
            yazi = font.render(msira[sira][1],True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        elif msira[sira][0] == 11:
            screen.blit(slep,(4,sira*32+40+bs))
            yazi = font.render("Süre : "+str(msira[sira][1])+"sn",True,(255,255,255))
            screen.blit(yazi,(136,sira*32+40+bs+4))
        sira -= 1
    pygame.draw.rect(screen,(10,10,10),(0,0,screen_size[0],36))
    screen.blit(run,runr)
    screen.blit(stop,stopr)
    screen.blit(save,saver)
    MainClock.tick(60)
    pygame.display.update()