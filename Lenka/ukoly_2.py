# 1. Vypiš čísla od 1 do 10 pomocí cyklu for.

for i in range(1, 11):
    print(i)

# 2. Vypiš sudá čísla od 1 do 100 pomocí while smyčky.
i = 1
while i < 101:
    if i % 2 == 0:
        print(i)
    i += 1

# 3. Zeptej se uživatele na číslo a vypiš, zda je kladné, záporné nebo nula.

number = int(input("Please enter a number: "))

if number > 0:
    print("This number is a positive.")
elif number == 0:
    print("This number is zero.")
else:
    print("This number is a negative.")

# 4. Vytvoř seznam 5 jmen a vypiš je každé na nový řádek pomocí for smyčky.

#TODO

# 5. Vytvoř seznam čísel a spočítej jejich součet pomocí for smyčky.

#TODO

# 6. Vytvoř seznam čísel a vypiš pouze ta, která jsou větší než 10.

#TODO

# 7. Požádej uživatele, aby zadal 5 čísel. Ulož je do seznamu a vypiš průměr.

list = []
sum_n = 0
for i in range(5):
    number_list = int(input("Please enter a number: "))
    list.append(number_list)
    sum_n += number_list
    i += 1
print(sum_n)

length = len(list)
average = sum_n / length
print(average)

# 8. Vytvoř seznam čísel a najdi největší a nejmenší hodnotu.

#TODO

# 9. Napiš program, který se ptá na heslo, dokud uživatel nezadá správné (např. 'tajneheslo').

#TODO

# 10. Vytvoř program, který zjistí, jestli je zadané číslo prvočíslo.

#TODO

# 11. Měj seznam slov a vypiš pouze ta, která mají víc než 4 znaky.

#TODO

# 12. Napiš program, který se zeptá na jméno a vypíše "Ahoj, [jméno]!" dokud nezadáš 'konec'.

#TODO
