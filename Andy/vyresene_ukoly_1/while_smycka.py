# 3. While smyčka
# Napište program, který bude opakovaně žádat uživatele o zadání čísla, dokud nezadá číslo větší než 100.
# Napište program, který počítá sčítání čísel od 1 do 10 pomocí `while` smyčky.

def smycky():

    print("Vítej v programu, který opakovaně žádá uživatele o zadání čísla, dokud nezadá číslo větší než 100")
    cislo = 1

    while cislo <= 100:
        cislo = int(input("Zadej prosím celé číslo: "))


    print("Vítej v programu, který počítá sčítání čísel od 1 do 10 pomocí `while` smyčky")
    x = 0
    soucet = 0

    while x <= 10:
        soucet += x
        x += 1

    print(f"Soucet cisel od 1 do 10 je {soucet}")


if __name__ == '__main__':
    smycky()
