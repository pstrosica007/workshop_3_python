# 6. Seřazení seznamu (sort)
# Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
# Napište program, který seřadí seznam slov podle abecedy.

import random

def serad_cisla():
    """Vytvoří seznam náhodných čísel a seřadí ho vzestupně."""
    print("\nSeřazení náhodných čísel:")

    # Generování seznamu náhodných čísel
    nahodna_cisla = [random.randint(1, 100) for _ in range(10)]
    print(f"Původní seznam: {nahodna_cisla}")

    # Seřazení seznamu
    serazeny = sorted(nahodna_cisla)
    print(f"Seřazený seznam: {serazeny}")

def serad_slova():
    """Seřadí seznam slov podle abecedy."""
    print("\nSeřazení seznamu slov:")
    
    seznam_slov = ["Jahoda", "Jablko", "Citron", "Malina", "Kiwi"]
    print(f"Původní seznam: {seznam_slov}")

    # Seřazení slov bez ohledu na velká/malá písmena
    serazeny = sorted(seznam_slov, key=str.lower)
    print(f"Seřazený seznam: {serazeny}")

if __name__ == '__main__':
    serad_cisla()
    serad_slova()
