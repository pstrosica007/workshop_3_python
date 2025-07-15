# 9. Napiš program, který se ptá na heslo, dokud uživatel nezadá správné (např. 'tajneheslo').

def heslo():
    spravne_heslo = "tajneheslo"
    pokusy = 3

    while pokusy > 0:
        zadane_heslo = input("Zadej heslo: ")
        if zadane_heslo == spravne_heslo:
            print("Přístup povolen.")
            return
        else:
            pokusy -= 1
            print(f"Špatné heslo. Zbývá pokusů: {pokusy}")

    print("Přístup zamítnut.")


if __name__ == '__main__':
    heslo()
