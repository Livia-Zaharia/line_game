import pygame

#se initializeaza
pygame.init()

#dimensiune ecran de lucru
windows_size=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()

#da numele ferestre de lucru deschise
pygame.display.set_caption("linii si iar linii")

#definim atribute
lines=[]
lines_inchidere=[]

draw=True
count=1

run=True


while run:
    clock.tick(5)
    #clock tick e cu ce rata ruleaza/secunda
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if draw:
                    lines.append([event.pos])
                    lines_inchidere.append([event.pos])
                    draw=not draw
                    count=count+1
                    middle=event.pos
            else:
                lines[-1].append(event.pos)
                if count==3:
                    lines_inchidere[-1].append(event.pos)
                    lines_inchidere[-1].append(middle)
                    #middle=lines[-1][-1]
                elif count>3:
                    lines_inchidere[-1].append(event.pos)
                    lines_inchidere[-1].append(middle)

                count=count+1
                #print(event.pos)
                print("-"*25)
                print(lines)
                #print("+"*25)
                #print(lines_inchidere)
            middle=lines[-1][-1]
    #print("????"*25)        
    windows_size.fill((255,255,255))
    for points in lines:
        print("++"*25)
        print(points)
        if len(points)>1:
            pygame.draw.lines(windows_size,(255,0,255),False,points,10)
            for points_2 in lines_inchidere:
                if len(points_2)>1:
                    pygame.draw.lines(windows_size, (0,255,0), False,points_2,10)
            for p in points:
                pygame. draw.circle(windows_size,(0,0,0),p,5)
                print("!!!"*25)
                print(p)
    pygame.display.flip()
pygame.quit()
exit()