# 5. Absolutní hodnota (abs)
# Napište program, který přijme číslo od uživatele a vypíše jeho absolutní hodnotu.
# Napište program, který porovná dvě čísla a zjistí jejich vzdálenost na číselné ose.

def abs_hodnota():

    print("Vítej v programu, který přijme číslo od uživatele a vypíše jeho absolutní hodnotu")
    cislo = float(input("Zadej číslo: "))
    print(f"absolutní hodnota {cislo} je {abs(cislo):.2f}")


    print("Vítej v programu, který porovná dvě čísla a zjistí jejich vzdálenost na číselné ose")
    cislo_1 = float(input("Zadej první číslo: "))
    cislo_2 = float(input("Zadej druhé číslo: "))
    print(f"rozdíl mezi {cislo_1} a {cislo_2} je {abs(cislo_1 - cislo_2):.2f}")


if __name__ == '__main__':
    abs_hodnota()
