# 4. For smyčka
# Napište `for` smyčku, která vypíše všechna sudá čísla od 1 do 20.
# Vypište jednotlivé znaky ve slově `"Python"` pomocí `for` smyčky.

def smycky():

    print("Vítej v programu, který pomocí `for` smyčky vypíše všechna sudá čísla od 1 do 20")

    for i in range(1, 21):
        if i % 2 == 0:
            print(i)


    print("Vítej v programu, který vypíše jednotlivé znaky ve slově `Python` pomocí `for` smyčky")
    slovo = "Python"

    for i in range(len(slovo)):
        print(slovo[i])


if __name__ == '__main__':
    smycky()
