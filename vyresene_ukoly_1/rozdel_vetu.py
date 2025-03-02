# 11. Rozdělování textu (split)
# Napište program, který přijme větu od uživatele a rozdělí ji na jednotlivá slova pomocí `split()`.

def rozdel_vetu_verze_1():
    print("Vítej v programu, který:")
    print("- přijme větu od uživatele a rozdělí ji na jednotlivá slova pomocí `split()")

    # Input od uživatele - věta
    veta = input("Napiš větu prosím: ")
    slova = veta.split()
    print(slova)


def rozdel_vetu_verze_2():
    print("Vítej v programu, který:")
    print("- Přijme větu od uživatele a odstraní interpunkci.")

    veta = input("📝 Napiš větu prosím: ")

    # Definujeme znaky k odstranění
    znaky_k_odstraneni = str.maketrans('', '', '.,!?')
    veta_cista = veta.translate(znaky_k_odstraneni)

    # Rozdělení na slova
    slova = veta_cista.split()

    print("\n✅ Rozdělená slova:")
    for slovo in slova:
        print(f"- {slovo}")


if __name__ == '__main__':
    rozdel_vetu_verze_1()
    rozdel_vetu_verze_2()
