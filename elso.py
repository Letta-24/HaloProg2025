import random

#Lista létrehozása
szamok = []
#A JÁTÉK -------------------------------
kitalalando_szam = 12

jatszol = True
while(jatszol):
    tipp_sz = input("Tipped? (egész szám):")
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue
    while(tipp != kitalalando_szam):
        tipp = int(input("Tipped? (egész szám):"))
        tipp_sz = input("Tipped? (egész szám):")
    if(tipp_sz.isdecimal()):
        tipp = int(tipp_sz)
    else:
        print("Egész számmal játsz!")
        continue
    print("Kitaláltad a számot!")
    
    folytatas = input("Akarsz-e még játszani [I/N]?")
    if folytatas == "N":
        jatszol = False