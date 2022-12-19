import numpy as np
import time
import random
import pygame
import pygame.freetype  

class Mappa:

    def __init__(self,riga,colonna):
        self.riga=riga
        self.colonna=colonna
        self.crea_mappa()
        #self.stampa_mappa()

        
    def crea_mappa(self):
        self.mappa=np.zeros((self.riga,self.colonna), dtype=int)
        self.mappa[0,0]=1
        self.mappa[self.riga-1,self.colonna-1]=3
        
    def stampa_mappa(self):
        print("\n\n"+str(self.mappa)+"\n\n")
    

    def aggiungi_ostacolo(self,ostacoli):
        for ostacolo in ostacoli:
            if(ostacolo[0]!=0 or ostacolo[1]!=0):
                self.mappa[ostacolo[0],ostacolo[1]]=2

    def get_cella(self,riga,colonna):
        if(riga>=self.riga or riga<0 or colonna>=self.colonna or colonna<0):
            return 2
        return self.mappa[riga][colonna]

    def genera_mappa_casuale(self):
        for i in range(1,self.riga):
            for j in range(1,self.colonna):
                if i!=self.riga-1 or j!=self.colonna-1:
                    self.mappa[i][j]=random.randrange(0,3,2)
        return str(self.mappa)


    def trova_percorso(self):
        cammino=[(0,0)]
        posX=0;
        posY=0
        tmp=(-1,-1)

        
        while  not (self.riga-1,self.colonna-1) in cammino:

            griglia()
            aggiornaSchermo()
            #print(cammino)
            #self.stampa_mappa()

            if(self.get_cella(posX+1,posY)==2 and  self.get_cella(posX-1,posY)==2 and self.get_cella(posX,posY+1)==2 and self.get_cella(posX,posY-1)==2):
                return -1
            
            
            if posX+1<self.colonna and self.get_cella((cammino[-1][0])+1,cammino[-1][1])!=2 and (posX+1,posY) not in cammino and tmp!=(posX+1,posY):#basso
                
                posX+=1
                cammino.append((posX,posY))
                self.mappa[posX,posY]=-1
 
            
            elif posY+1<self.riga and self.get_cella(cammino[-1][0],(cammino[-1][1])+1)!=2 and (posX,posY+1) not in cammino and tmp!=(posX,posY+1): #destra
                
                posY+=1
                cammino.append((posX,posY))
                self.mappa[posX,posY]=-1


            elif posX-1>-1 and self.get_cella((cammino[-1][0])-1,cammino[-1][1])!=2 and(posX-1,posY) not in cammino and tmp!=(posX-1,posY): #alto
            
                posX-=1
                cammino.append((posX,posY))
                self.mappa[posX,posY]=-1


            elif posY-1>-1 and self.get_cella((cammino[-1][0]),(cammino[-1][1])-1)!=2 and (posX,posY-1) not in cammino and tmp!=(posX,posY-1): #sinistra
                
                posY-=1
                cammino.append((posX,posY))
                self.mappa[posX,posY]=-1
                
            

            else:
                
                self.mappa[posX,posY]=2
                tmp=cammino[-1]

                if(len(cammino)!=1):
                    cammino.pop()
                
                posX=cammino[-1][0]
                posY=cammino[-1][1]

            
        return cammino
            
                
    def traccia_percorso(self,cammino):
        cammino.pop()
        for c in cammino:
            self.mappa[c[0]][c[1]]=4;
        self.mappa[0][0]=1
        self.mappa[self.riga-1][self.colonna-1]=3

            

def scrivi():
    global esclusi,text,screen,colore
    img = text.render("Mappe generate: "+str(esclusi), True, colore)
    pygame.transform.scale(img, (310, 0))
    screen.blit(img, (200, 25))



def aggiornaSchermo():
    global FPS
    pygame.display.update() #aggiorno il display
    pygame.time.Clock().tick(FPS) #frame di aggiornamento


def griglia():
    global width, heigth,mappa,dim
    if dim==5:
        blockSize = 100
    elif dim==25:
        blockSize=20
    else:
        blockSize=50

    scrivi()
    nero=(0, 0, 0)
    green=(0,254,0)
    blue=(0,0,254)
    red=(254,0,0)
    yellow=(254,254,0)
    conto1=0
    conto2=-1
    for x in range(100,width-100, blockSize):
        conto1=0
        conto2+=1
        for y in range(100, heigth-100, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)

            if(mappa.get_cella(conto1,conto2)==0):
                pygame.draw.rect(screen, nero, rect, 1)

            elif mappa.get_cella(conto1,conto2)==1:
                pygame.draw.rect(screen, yellow, rect)

            elif mappa.get_cella(conto1,conto2)==3:
                pygame.draw.rect(screen, blue, rect)

            elif mappa.get_cella(conto1,conto2)==2:
                pygame.draw.rect(screen, nero, rect)

            elif mappa.get_cella(conto1,conto2)==-1:
                pygame.draw.rect(screen, red, rect)
            elif mappa.get_cella(conto1,conto2)==4:
                pygame.draw.rect(screen, green, rect)   

            conto1+=1
            

    
    


pygame.init() #inizializzo pygame e i suoi metodi

width=700 #larghezza schermo
heigth=700 #altezza schermo

screen = pygame.display.set_mode((width, heigth))#dimensione finestra
pygame.display.set_caption("Maze solver") #titolo della finestra

text = pygame.font.SysFont(None, 48)



colore =(0, 120, 252)
dim=25
FPS=60 #frame di aggioramento



cammino=-1
esclusi=0
while cammino==-1:
    
    esclusi+=1
    mappa=Mappa(dim,dim)
    mappa.genera_mappa_casuale()
    white=(254,254,254)
    screen.fill(white)
    griglia()
    aggiornaSchermo()
    time.sleep(2)
    cammino=mappa.trova_percorso()
    

colore=(0,254,0)
mappa.traccia_percorso(cammino)
griglia()
aggiornaSchermo()
time.sleep(5)
pygame.quit() # chiudo tutto






    
