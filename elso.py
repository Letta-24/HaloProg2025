import random

szamok=[]

#lista feltoltese 40db random nem ismétlödő 2jegyu egesz szammal
while len(szamok) != 40:
    szam=random.randint(10,99)
    if szam not in szamok:
        szamok.append(szam)
    
#ell
print(szamok) 

#Változok létrehozzása
jatek_szam=0
nem_talalDB=0
#A kitalálandó szám kiválasztása a listából
kitalalando_szam=szamok[random.randint(0, len(szamok))]

kitalalando_szam = 12

jatszol=True
while (jatszol):
    jatek_szam +=1
    tipp_sz=input("tipped? (egész szám): ").strip()
    if (tipp_sz.isdecimal()):
        tipp=int(tipp_sz)
    else:
        print("egész számmal játsz")
        continue
    
    while (tipp!=kitalalando_szam):
        if (tipp < kitalalando_szam):
            print("A kitalálandó szám nagyobb!")
        else:
            print("A kitalálandó szám kisebb!")
        tipp_sz=input("tipped? (egész szám)\n[kilépés\'X\' karakterrel]: ").strip()
        if (tipp_sz.isdecimal()):
            tipp=int(tipp_sz)
        elif tipp_sz == 'X':
            exit()
        else:
            print("egész számmal játsz")
            continue
        
    print("eltaláltad")
    
    folytat=input("akarsz meg jatszani? [I/N]")
    if (folytat=="N"):
        jatszol=False