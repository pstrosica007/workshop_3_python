# 7. Požádej uživatele, aby zadal 5 čísel. Ulož je do seznamu a vypiš průměr.

def zadej_cislo():
    seznam_cisel = []
    for i in range(5):
        while True:
            try:
                cislo = int(input("Uživatel/ko prosím zadej číslo: "))
                seznam_cisel.append(cislo)
                break
            except ValueError:
                print("To nebylo číslo, zkus to prosím znovu.")

    prumer = sum(seznam_cisel) / len(seznam_cisel)
    print(f"Zadaná čísla: {seznam_cisel}")
    print(f"Průměr: {prumer:.2f}")


if __name__ == '__main__':
    zadej_cislo()
