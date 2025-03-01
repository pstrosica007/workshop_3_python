# 6. Seřazení seznamu (sort)
# Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
# Napište program, který seřadí seznam slov podle abecedy.

import random
def serazeni_seznamu():

    print("Vítej v programu, který vytvoří seznam náhodných čísel a seřadí ho vzestupně")

    # Vytvoření seznamu s 10 náhodnými čísly mezi 1 a 100
    nahodna_cisla = [random.randint(1, 100) for _ in range(10)]

    print("Původní seznam:", nahodna_cisla)  # Výpis před seřazením

    nahodna_cisla.sort()  # Seřazení vzestupně

    print("Seřazený seznam:", nahodna_cisla)  # Výpis po seřazení



    print("Vítej v programu, který seřadí seznam slov podle abecedy")
    seznam_slov = ["Jahoda", "Jablko", "Citron", "Malina", "Kiwi"]

    # Seřazení seznamu abecedně
    seznam_slov.sort()

    # Výpis seřazeného seznamu
    print("Seřazený seznam slov:")
    for slovo in seznam_slov:
        print(slovo)


if __name__ == '__main__':
    serazeni_seznamu()
