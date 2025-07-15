# 5. Vytvoř seznam čísel a spočítej jejich součet pomocí for smyčky.

# from numpy import random

# def seznam_cisel():
#     x = random.randint(1000, size=(25))
#     print(x)
#     soucet = 0
#     for cislo in x:
#         soucet += cislo
#     print(soucet)

import random  # když nechci numpy


def seznam_cisel():
    x = [random.randint(0, 999) for _ in range(25)]
    soucet = 0
    for cislo in x:
        soucet += cislo
    print(f"Seznam čísel: {x}")
    print(f"Součet: {soucet}")


if __name__ == '__main__':
    seznam_cisel()
