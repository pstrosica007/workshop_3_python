# 10. Vytvoř program, který zjistí, jestli je zadané číslo prvočíslo.

def je_prvocislo():
    try:
        cislo = int(input("Zadej celé číslo: "))
    except ValueError:
        print("To nebylo platné celé číslo.")
        return

    if cislo <= 1:
        print(f"{cislo} není prvočíslo.")
        return
    elif cislo in (2, 3):
        print(f"{cislo} je prvočíslo.")
        return

    for i in range(2, cislo):
        if cislo % i == 0:
            print(f"{cislo} není prvočíslo, protože je dělitelné {i}.")
            return

    print(f"{cislo} je prvočíslo.")


if __name__ == '__main__':
    je_prvocislo()
