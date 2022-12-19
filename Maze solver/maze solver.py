import numpy as np
import random
import time

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

            #griglia()
            #aggiornaSchermo()
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
        for c in cammino:
            self.mappa[c[0]][c[1]]=1;
        self.mappa[0][0]=1
        self.mappa[self.riga-1][self.colonna-1]=3

            
start_time = time.time()



cammino=-1
dim=50
conto=0
while cammino==-1:
    mappa=Mappa(dim,dim)

    #ostacoli=[(0,4),(1,0),(1,1),(2,3),(3,2),(3,4),(8,8),(3,7),(5,6),(7,9),(9,1),(9,5),(1,3),(1,6),(2,5),(3,1)]
    #mappa.aggiungi_ostacolo(ostacoli)
    print("generazione "+str(conto+1)+"\n")
    mappy=mappa.genera_mappa_casuale()

    cammino=mappa.trova_percorso()
    conto+=1



if cammino!=-1:
    print("\n\n\nmappa analizzata\n\n\n"+mappy)
    print("\n\n\n\npercorso trovato!\n\n-> "+str(cammino)+"\n\n\n")
    mappa.traccia_percorso(cammino);
    mappa.stampa_mappa()
    print("\n\n\nmappe senza soluzione generate: "+str(conto))

else:
    print("\n\n\nnon esiste un percorso dalla radice alla destinazione!\n\n")

print("--- %s seconds ---" % (time.time() - start_time))

