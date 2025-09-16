import random

szamok=[]

#lista feltoltese 100db random 2jegyu egesz szammal
for i in range (100):
    szam=random.randint(10,99)
    szamok.append(szam)
    
#ell
print(szamok) 

#EGYSZÁM JáTÉK
jatek_szam=0
nem_talalDB=0

kitalalando_szam=szamok[random.randint(0, len(szamok))]
jatszol=True
while (jatszol):
    tipp_sz=input("tipped?: ").strip()
    if (tipp_sz.isdecimal()):
        tipp=int(tipp_sz)
    else:
        print("egész számmal játsz")
        continue
    
    while (tipp!=kitalalando_szam):
        tipp_sz=input("tipped?: ").strip()
        if (tipp_sz.isdecimal()):
            tipp=int(tipp_sz)
        else:
            print("egész számmal játsz")
            continue
        
    print("eltaláltad")
    
    folytat=input("akarsz meg jatszani? [I/N]")
    if (folytat=="N"):
        jatszol=False