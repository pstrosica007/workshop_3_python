#1 sečti čísla od 1 do 10
from xml.etree.ElementPath import prepare_self

soucet = 0
for cislo in range(1, 11):
    soucet += cislo
print("Součet čísel od 1 do 10 je:", soucet)

#2 vytiskni všechna čísla v seznamu
cisla = [3, 5, 7, 10, 12]
for cislo in cisla:
    print(cislo)

#3 Zkontroluj, jestli jsou všechna čísla dělitelná 2
cisla2 = [4, 15, 6, 7, 8, 9]
for cislo2 in cisla2:
    if cislo2 % 2 == 0:
        print(cislo2)

#4 Vytiskni všechna písmena ve slově
slovo = "prdel"
for znak in slovo:
    print(znak)

#5 pyramidový tvar z hvězdiček
for i in range(1, 6):
    print('*' * i)
    