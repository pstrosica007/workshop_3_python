# 8. F-string (formátování textu)
# Napište program, který přijme jméno a věk uživatele a vypíše větu `"Ahoj, jmenuji se [jméno] a je mi [věk] let."` pomocí f-string.


def vypis_jmeno():
    print("který přijme jméno a věk uživatele a vypíše větu `Ahoj, jmenuji se [jméno] a je mi [věk] let.` pomocí f-string")

    # Načtení jména a příjmění od uživatele
    jmeno = (input("Zadej své jméno: "))
    vek = int(input("Zadej svůj věk: "))
    print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")


if __name__ == '__main__':
    vypis_jmeno()
