import random

szamok=[]

#lista feltoltese 40db random nem ismétlödő 2jegyu egesz szammal
while len(szamok) != 40:
    szam=random.randint(10,99)
    if szam not in szamok:
        szamok.append(szam)
    
#ell
print(szamok) 

#Változok létrehozzása a statisztikához
jatek_szam=1
nem_talalDB=0
#A kitalálandó szám kiválasztása a listából
kitalalando_szam=szamok[random.randint(0, len(szamok))]

jatszol=True
while (jatszol):
    tipp_sz=input("\ntipped?: ").strip()
    if (tipp_sz.isdecimal()):
        tipp=int(tipp_sz)
    else:
        print("egész számmal játsz")
        continue
    
    while (tipp!=kitalalando_szam):
        nem_talaltDB +=1 
        
        if (tipp == 123):
            pass
        elif (tipp < kitalalando_szam):
            print("kitalálandó szám nagyobb")
        elif (tipp > kitalalando_szam):
            print("kitalálandó szám kisebb")
            
        tipp_sz=input("\ntipped? (egész szám)[Kilépés \'X\' karakterrel]: ").strip()

        if (tipp_sz.isdecimal()):
            tipp=int(tipp_sz)
        elif tipp_sz == 'X':
            print(f"\n{jatek_szam} db szám kitalálásához {nem_talaltDB}-szer próbálkozott rosszul")
            exit()
        else:
            print("egész számmal játsz")
            tipp=123
            continue
        
    print("eltaláltad")
    
    folytat=input("akarsz meg jatszani? [I/N]")
    
    if (folytat=="N"):
        jatszol=False
        print(f"\n{jatek_szam} db szám kitalálásához {nem_talaltDB}-szer próbálkozott rosszul")
    elif (folytat=="I"):
        jatek_szam += 1