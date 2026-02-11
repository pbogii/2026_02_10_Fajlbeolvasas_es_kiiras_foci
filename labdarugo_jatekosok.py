"""
Olvasd be a labdarugok.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány játékos szerepel a fájlban?
2. Melyik játékos szerezte a legkevesebb gólt?
3. Melyik játékos szerzett a legtöbb gólt?
4. Ki játszott a legtöbb mérkőzést?
5. Átlagosan hány gólt szerzett egy játékos?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerzett a legtöbb gólt? (feltételezve, hogy egy játékos csak egy csapatban játszott)


A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

labda_rugok = []
with open('beolvasando_adatok/labdarugok.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        csapat= adatok[1]
        golszam = int(adatok[2])
        merkozesekszama = int(adatok[3])
      
        labdarugo = {'nev': nev,
                'csapat': csapat,
                'golszam': golszam,
                'merkozesekszama': merkozesekszama}
        labda_rugok.append(labdarugo)

print(f'{labda_rugok=}')


#1
print(f"A beolvasott fájlban összesen {len(labda_rugok)} játékos szerepel.")


#2
legkevesebb_gol = labda_rugok[0]["golszam"]
legkevesebb = labda_rugok[0]["nev"]

for labdarugo in labda_rugok:
    if labdarugo["golszam"] < legkevesebb_gol:
        legkevesebb_gol = labdarugo["golszam"]
        legkevesebb = labdarugo["nev"]

print(f"A legkevesebb gólt szerző játékos: {legkevesebb} ")


#3
legtobb_gol = labda_rugok[0]["golszam"]
legtobb = labda_rugok[0]["nev"]

for labdarugo in labda_rugok:
    if labdarugo["golszam"] > legtobb_gol:
        legtobb_gol = labdarugo["golszam"]
        legtobb = labdarugo["nev"]

print(f"A legtöbb gólt szerző játékos: {legtobb}")


#4
legtobb_mer = labda_rugok[0]["merkozesekszama"]
legtobb_m = labda_rugok[0]["nev"]

for labdarugo in labda_rugok:
    if labdarugo["merkozesekszama"] > legtobb_mer:
        legtobb_mer = labdarugo["merkozesekszama"]
        legtobb_m = labdarugo["nev"]

print(f"A legtöbb mérkőzést játszó játékos: {legtobb_m}")

#5
golaszamok = []
for labdarugo in labda_rugok:
    golaszamok.append(golszam)
atlag = sum(golaszamok) / len(golaszamok)

print(f"Az átlagos gólszám: {atlag}")

#6
print("***A legtöbb gólt szerző csapat: ____")
