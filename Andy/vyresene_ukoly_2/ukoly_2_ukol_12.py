# 12. Napiš program, který se zeptá na jméno a vypíše "Ahoj, [jméno]!" dokud nezadáš 'konec'.

def ahoj_user():
    while True:
        jmeno = input("Zadej prosím své jméno (nebo 'konec' pro ukončení): ")
        if jmeno.lower() == "konec":
            print("Program ukončen.")
            break
        print(f"Ahoj, {jmeno}!")


if __name__ == '__main__':
    ahoj_user()
