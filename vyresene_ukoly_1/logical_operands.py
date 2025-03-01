# 1. Logické operátory (AND, OR, NOT)
# Napište podmínku, která vrátí `True`, pokud `x` je větší než 10 a zároveň menší než 50.
# Napište podmínku, která vrátí `True`, pokud `y` je menší než 5 nebo větší než 20.
# Napište podmínku, která vrátí `True`, pokud `z` není rovno nule.


def logical_operands():
    x = int(input("Zadej prosím číslo: "))
    if x in range(10, 51):
        print(f'Zadal/a jsi číslo {x} v rozsahu 10 až 50 včetně.')
    else:
        print(f'Zadal/a jsi číslo {x} mimo rozsah 10 až 50 včetně.')

    y = int(input("Zadej prosím číslo: "))
    if y <= 5 or y >= 20:
        print(f'Zadal/a jsi číslo {y} , které je menší nebo rovno než 5 nebo větší nebo rovno než 20.')
    else:
        print(f'Zadal/a jsi číslo {y} mimo rozsah pod 5 nebo nad 20.')

    z = int(input("Zadej prosím číslo: "))
    if z != 0:
        print(f'Zadal/a jsi číslo {z} a není to 0.')
    else:
        print(f'Zadal/a jsi číslo {z} a je to 0.')


if __name__ == '__main__':
    logical_operands()
