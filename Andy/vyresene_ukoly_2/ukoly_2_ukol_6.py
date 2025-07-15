# 6. Vytvoř seznam čísel a vypiš pouze ta, která jsou větší než 10.

import random


def seznam_cisel():
    x = [random.randint(0, 39) for _ in range(10)]
    filtr = [cislo for cislo in x if cislo > 10]

    print(f"Originální seznam čísel je: {x}")
    print(f"Čísla větší než 10 jsou: {filtr}")


if __name__ == '__main__':
    seznam_cisel()
