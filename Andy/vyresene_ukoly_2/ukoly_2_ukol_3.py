# 3. Zeptej se uživatele na číslo a vypiš, zda je kladné, záporné nebo nula

def zadej_cislo():
    try:
        user_input = int(input("Zadej prosím kladné nebo záporné číslo, klidně i 0: "))
        if user_input < 0:
            print(f"Zadané číslo {user_input} je záporné.")
        elif user_input == 0:
            (
                print(f"Zadané číslo {user_input} je nula."))
        else:
            print(f"Zadané číslo {user_input} je kladné.")
    except ValueError:
        (
            print("Nezadal(a) jsi platné číslo. Zkus to prosím znovu."))


if __name__ == '__main__':
    zadej_cislo()
