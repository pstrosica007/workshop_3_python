# 10. Zaokrouhlení čísel (round)
# Napište program, který přijme desetinné číslo od uživatele a zaokrouhlí ho na **2 desetinná místa**.
# Napište program, který vezme seznam desetinných čísel a zaokrouhlí každé číslo na 1 desetinné místo pomocí `map()`.

def hraj_si_s_round():
    print("Vítej v programu, který:")
    print("- Přijme desetinné číslo od uživatele a zaokrouhlí ho na 2 desetinná místa")

    # Input od uživatele zaokrouhlený na 2 desetinná místa
    cislo = round(float(input("Zadej prosím desetinné číslo: ")), 2)
    print(f"Číslo zaokrouhlené na 2 des. místa: {cislo}")

def hraj_si_s_map():
    print("\nVítej v programu, který:")
    print("- Vezme seznam desetinných čísel a zaokrouhlí každé číslo na 1 desetinné místo pomocí `map()`")

    # Převod řetězců na desetinná čísla
    seznam_cisel = list(map(float, input("Zadej desetinná čísla oddělená mezerou: ").split()))

    # Použití map() pro zaokrouhlení každého čísla na 1 desetinné místo
    novy_seznam_cisel = list(map(lambda x: round(x, 1), seznam_cisel))

    print(f"Seznam desetinných čísel zaokrouhlených na 1 des. místo: {novy_seznam_cisel}")


if __name__ == '__main__':
    hraj_si_s_round()
    hraj_si_s_map()
