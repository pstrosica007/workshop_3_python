# 7. Medián
# Napište program, který přijme seznam čísel od uživatele a najde jejich medián.

def najdi_median():
    print("Vítej v programu, který přijme seznam čísel od uživatele a najde jejich medián")

    try:
        # Načtení čísel od uživatele
        cisla = list(map(int, input("Zadej čísla pro hledání mediánu oddělená mezerou: ").split()))
        if not cisla:
            print("Nebyla zadána žádná čísla. Zkuste to znovu.")
            return

        # Seřazení čísel
        cisla.sort()
        n = len(cisla)
        stred = n // 2

        # Výpočet mediánu
        if n % 2 == 1:
            median = float(cisla[stred])  # Převod na float kvůli přesnosti výstupu
        else:
            median = (cisla[stred - 1] + cisla[stred]) / 2

        print(f"Medián je: {median:.2f}")

    except ValueError:
        print("Neplatný vstup! Zadejte pouze čísla oddělená mezerou.")


if __name__ == '__main__':
    najdi_median()
