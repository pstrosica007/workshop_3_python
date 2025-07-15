# 1. Vytvoř tuple se třemi prvky (čísla nebo řetězce)
# tuple(1,2,3)
moje_tuple = ("hovno", "letí", "oknem")

# 2. Přístup na 2. prvek v tuplu
druhy_prvek = moje_tuple[2]
print(druhy_prvek)

# 3. Jak vytvoříš tuple s jedním prvkem?
inferno = (666,)  # aby to byl tuple, musí za tim být čárka, jinak to bude int neasi
print(type(inferno))

# 4. Může tuple obsahovat jiný tuple? Vyzkoušej
tuple_trouble = (666, "duch_svatý", 333)
print(tuple_trouble)

# --- List ---
# 5. Vytvoř list jmen a přidej nové jméno na konec
seznam_jmen = ["Bára", "Petra", "Martin", "Dobromysla"]
seznam_jmen.append("Monika")

print(seznam_jmen)

# 6. Seřaď list čísel
list_cisel = [1, 44, 5.6, 66, 743, 24, 66, 11, -5, 98, 33.8, 25, 6]
list_cisel.sort()

print(list_cisel)

# 7. Vyfiltruj z listu jen sudá čísla pomocí list comprehension
# tohle je bez list comprehension
# suda_cisla = []

# for x in list_cisel:
#    if x % 2 == 0:
#        suda_cisla.append(x)

suda_cisla = [x for x in list_cisel if x % 2 == 0]
print(suda_cisla)

# print(suda_cisla)


# 8. Změň druhý prvek listu na jiné jméno
seznam_jmen2 = ["Bára", "Petra", "Martin", "Dobromysla"]
seznam_jmen2[1] = "Romulus"
print(seznam_jmen2)

# --- Set ---
# 9. Vytvoř set s čísly, zkus přidat duplikát – co se stane?
set_cisel = {1, 2, 3}
set_cisel.add(2)
print(set_cisel)
# stane se to, že se nestane nic - jelikož je číslo stejné, python ho nepřidá

# 10. Vyzkoušej průnik dvou setů
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
prunik = set1 & set2
print(prunik)

# 11. Přidej více prvků do setu pomocí update()
novy_set = {3, 5, 7, 8, 44}
novy_set.update([23, 2, 19])
print(novy_set)

# 12. Zjisti, zda určitá hodnota je v setu
tvoje_cislo = input("Zadej libovolné číslo a zjisti zda je v setu.")
if tvoje_cislo in novy_set:
    print("Zadené číslo je v setu.")
else:
    print("Zadané číslo v setu není :(.")
# --- Dict ---
# 13. Vytvoř dict s klíči "name", "age" a "city"
dict = {
    "name": "Anna",
    "age": 30,
    "city": "Prague"
}

print(dict)

# 14. Přidej nový klíč "email"
dict.update({"email": "anna@gmail.com"})
print(dict)

# 15. Vyhledej hodnotu podle klíče "name"
print(dict["name"])

# 16. Iteruj přes všechny klíče a hodnoty
# tomuhle asi uplně nerozumim - jakože projít všechny klíče a jejich hodnoty? ale jinak než pomocí print

# --- Bubble Sort ---
# 17. Použij metodu bubble_sort na list čísel [4, 2, 7, 1]
list_cisel = [4, 2, 7, 1]

# --- Quick Sort ---
# 18. Použij metodu quick_sort na list čísel [9, 5, 2, 8, 1]

# --- Rekurze ---
# 19. Spočítej faktoriál čísla 5 pomocí factorial_recursive
# 20. Spočítej Fibonacciho číslo na pozici 7 pomocí fibonacci()
# 21. Co se stane, když zavoláš factorial_recursive(-1)? Proč?

# 🔁 BONUS
# 22. Napiš funkci, která najde nejhlubší složku v zadané cestě rekurzivně
# 23. Vytvoř funkci, která spočítá počet všech souborů v adresáři (včetně podsložek)
