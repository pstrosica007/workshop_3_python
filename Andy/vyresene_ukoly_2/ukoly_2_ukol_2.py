# 2. Vypiš sudá čísla od 1 do 100 pomocí while smyčky.

def suda_cisla():
    print("Výpis sudých čísel od 1 do 100 pomocí cyklu while: ")
    x = 1
    while x <= 100:
        if x % 2 == 0:
            print(x)
        x += 1


if __name__ == '__main__':
    suda_cisla()
