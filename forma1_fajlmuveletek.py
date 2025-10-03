import io
'''
fajl = open ("F1-2024dec.csv", encoding="utf-8")

fajl_tartalom = fajl.read()
fajl_tartalom1 = fajl.read(11)

print(fajl_tartalom)
print(f"\n\n{fajl_tartalom1}")

fajl_tartalom2 = []

fajl_tartalom2 = fajl.readlines()
print(len(fajl_tartalom2))

fajl.close()
'''
verseny_adatok = []
try:
    with open ("F1-2024dec.csv", encoding="utf-8") as fajl:    
        
        for sor in fajl:
            verseny_adatok.append(sor)
    
except IOError as ex:
    print(f"fáljmegnyítás hiba: {ex}")

print(verseny_adatok)



"""algoritmus fajták
1.Sorozatszámítás/összegzés
2.kiválasztás
3.megszámolás
4.eldöntés 1,2
5.maximum/minimum kiválasztás
6.keresés (lineáris)
7. Szétválogatás 
8.kiválogatás (külön,helyben)
9.unió
10.metszet
11.rendezés
    egyszerű csere
    buborékos
    minimumkiválasztásos
"""



#1.Sorozatszámítás/összegzés mennyi a pontszám átlag?
pontszam = 0
db = len(verseny_adatok) - 1

for i in range(1,len(verseny_adatok)):
    sor=verseny_adatok[i].split(",")
    pontszam = pontszam+int(sor[1])
atlag=pontszam/db
print(f"A pontszámok átlaga: {atlag}")



#2.Kiválasztás A kiválasztott versenyző adatai
pilota=input("Kérek adj meg egy pilótát:")
cikvalt=1
while verseny_adatok[cikvalt].split(",")[0]!= pilota:
    cikvalt+=1
print(verseny_adatok[cikvalt])
"""
Ciklusok


Előltesztelős:
-0-szor legrosszabb esetben
-I=1
ciklus amig I<=N
I=I+1
Hátultesztelős:
I=1
Ismételd:
I=I+1
amíg I<=N
-1-szer
Számlálos:
-N-szer fut le
1.ciklusváltozó (I)
-ciklus I = 1-től N-ig...
2.feltétel(kilépés,benmaradás)
3.lépésköz/léptetés
-1-sével lépked
"""