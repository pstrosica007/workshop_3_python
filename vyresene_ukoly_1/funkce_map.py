# 9. Mapování hodnot (map)
# Napište program, který převede seznam číselných řetězců (např. ["1", "2", "3"]) na čísla pomocí map().
# Napište program, který převede seznam čísel na jejich druhé mocniny pomocí map().

def hraj_si_s_map():
    print("Vítej v programu, který:")
    print("- Převede seznam číselných řetězců na čísla pomocí `map()`.")
    print("- Převede seznam čísel na jejich druhé mocniny pomocí `map()`.")

    # Seznam čísel jako řetězce
    cisla = ['1', '2', '3', '4']

    # Převod řetězců na čísla, rovnou na list abychom se vyhnuli opětovnému iterování
    seznam_cisel = list(map(int, cisla))
    print(f"Převedený seznam na čísla: {seznam_cisel}")

    # Výpočet druhé mocniny každého čísla
    seznam_cisel_mocniny = list(map(lambda x: x**2, seznam_cisel))
    print(f"Druhé mocniny čísel: {seznam_cisel_mocniny}")


if __name__ == '__main__':
    hraj_si_s_map()
