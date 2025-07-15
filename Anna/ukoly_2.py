#1. Vypiš čísla od 1 do 10 pomocí cyklu for.
for i in range(1, 11):
    print(i)

#2. Vypiš sudá čísla od 1 do 100 pomocí while smyčky.
x = 0
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1

#3. Zeptej se uživatele na číslo a vypiš, zda je kladné, záporné nebo nula.
number = float(input(f"Napiš nějaké číslo!\n"))

if number > 0:
    print("Číslo které jsi napsal je kladné.")
elif number < 0:
    print("Číslo které jsi napsal je záporné.")
else:
    print("Jsi nula.")

#4. Vytvoř seznam 5 jmen a vypiš je každé na nový řádek pomocí for smyčky.
names = ["Bořek", "Božena", "Radoslav", "Ludmila", "Jarmila"]

for name in names:
    print(name)

#5. Vytvoř seznam čísel a spočítej jejich součet pomocí for smyčky.
numbers = [79, 32, 1, 22, 97, 32, 33, 43]
soucet = 0

for number in numbers:
    soucet += number

print("Soucet cisel je: ", soucet)

#6. Vytvoř seznam čísel a vypiš pouze ta, která jsou větší než 10.
numbers2 = [79, 32, 1, 22, 97, 32 ,2 ,32, 33, 8, 43]

for number2 in numbers2:
    if number2 > 10:
        print("Čísla větší než 10 jsou: ", number2)

#7. Požádej uživatele, aby zadal 5 čísel. Ulož je do seznamu a vypiš průměr.
tvoje_cisla = input("Zadej 5 čísel oddělených mezerou:\n")
cisla_list = tvoje_cisla.split()

if len(cisla_list) != 5:
    print("❗ Musíš zadat přesně 5 čísel, zkus to prosím znovu.")
else:
    cisla = [float(cislo) for cislo in cisla_list]
    soucet = sum(cisla)
    prumer = soucet / len(cisla)

    print("\nZadaná čísla jsou:", cisla)
    print("Jejich průměr je:", prumer)

#8. Vytvoř seznam čísel a najdi největší a nejmenší hodnotu.
import random
numbers3 = [random.randint(1, 100) for _ in range(10)]

nejvetsi = max(numbers3)
nejmensi = min(numbers3)

print("Seznam čísel je:", numbers3)
print("Největší číslo je:", nejvetsi)
print("Nejmenší číslo je:", nejmensi)

#9. Napiš program, který se ptá na heslo, dokud uživatel nezadá správné (např. 'tajneheslo').
spravne_heslo = "tajneheslo"
zadane_heslo = ""

while zadane_heslo != spravne_heslo:
    zadane_heslo = input("Zadej heslo:\n")
    if zadane_heslo != spravne_heslo:
        print("Špatné heslo, zkus to znovu.")

print("Přístup povolen.")

#10. Vytvoř program, který zjistí, jestli je zadané číslo prvočíslo.

def prvocislo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# získání vstupu od uživatele

number = int(input("Zadej libovolné číslo: "))

if prvocislo(number):
    print(f"{number} je prvočíslo.")
else:
    print(f"{number} není prvočíslo.")


#11. Měj seznam slov a vypiš pouze ta, která mají víc než 4 znaky.
seznam_slov = ["big", "smelly", "elephant", "had", "small", "pear", "on", "his", "trunk"]

for slovo in seznam_slov:
    if len(slovo) > 4:
        print(slovo)

#12. Napiš program, který se zeptá na jméno a vypíše "Ahoj, [jméno]!" dokud nezadáš 'konec'.

while True:
    name = input("Zadej své jméno (nebo napiš 'konec' pro ukončení): ")
    if name.lower() == "konec":
        print("Program ukončen, zdarec!")
        break
    print(f"Ahoj,{name}!")
