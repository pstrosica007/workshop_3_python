# 4. Vytvoř seznam 5 jmen a vypiš je každé na nový řádek pomocí for smyčky.

# def seznam_jmen():
#     seznam_jmen = ("Jana Nováková", "Bohuš Hustý", "Petr Rychlý", "Alena Malá", "Vlasta Dostál")
#     for jmeno in seznam_jmen:
#         print(f"{jmeno}")

def seznam_jmen():
    seznam_jmen = ["Jana Nováková", "Bohuš Hustý", "Petr Rychlý", "Alena Malá", "Vlasta Dostál"]
    for i, jmeno in enumerate(seznam_jmen, start=1):
        print(f"{i}. {jmeno}")


if __name__ == '__main__':
    seznam_jmen()
