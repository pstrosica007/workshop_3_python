# 8. Vytvoř seznam čísel a najdi největší a nejmenší hodnotu.

import random


def min_max_value():
    seznam_cisel = [random.randint(0, 39) for _ in range(10)]

    print(f"Seznam čísel je: {seznam_cisel}")
    print(f"Maximální hodnota ze seznamu je: {max(seznam_cisel)}")
    print(f"Minimální hodnota ze seznamu je: {min(seznam_cisel)}")


if __name__ == '__main__':
    min_max_value()
