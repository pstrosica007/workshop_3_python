# 2. If - elif - else
# Napište program, který na základě věku určí, zda je osoba dítě (do 12 let), teenager (13-17), dospělý (18-64) nebo senior (65+).
# Napište program, který přijme číslo od uživatele a určí, zda je kladné, záporné nebo nula.

def ukol2():
    x = int(input("Kolik ti je let? : "))
    if x in range(0, 13):
        print(f'{x} je věk dítětě.')
    elif x in range(13, 18):
        print(f'{x} je věk teenagera.')
    elif x in range(18, 65):
        print(f'{x} je věk dospěláka.')
    else:
        print(f'{x} je věk seniora.')


if __name__ == '__main__':
    ukol2()
