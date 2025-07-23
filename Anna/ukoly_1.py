### 1. Logické operátory (AND, OR, NOT)
# 1️⃣ Napište podmínku, která vrátí `True`, pokud `x` je větší než 10 **a zároveň** menší než 50.
x = float(input("Zadej libovolné číslo:"))
if x > 10 and x < 50:
    print(True)
else:
    print(False)

# 2️⃣ Napište podmínku, která vrátí `True`, pokud `y` je menší než 5 **nebo** větší než 20.
y = float(input("Zadej libovolné číslo:"))
if y < 5 or y > 20:
    print(True)
else:
    print(False)

# 3️⃣ Napište podmínku, která vrátí `True`, pokud `z` **není** rovno nule.
z = float(input("Zadej libovolné číslo:"))

if z != 0:
    print(True)
else:
    print(False)

# nebo

if not z == 0:
    print(True)
else:
    print(False)

### 2. If - elif - else
# 4️⃣ Napište program, který na základě věku určí, zda je osoba dítě (do 12 let), teenager (13-17), dospělý (18-64) nebo senior (65+).
vek = int(input("Kolik je vám let?"))

if vek <= 12:
    print("Dítě")
elif vek <= 17:
    print("Teenager")
elif vek <= 64:
    print("Dospělý")
else:
    print("Senior")

# 5️⃣ Napište program, který přijme číslo od uživatele a určí, zda je kladné, záporné nebo nula.
cislo1 = float(input("Zadejte libovolné číslo"))

if cislo1 > 0:
    print("Kladné číslo.")
elif cislo1 < 0:
    print("Záporné číslo.")
else:
    print("Dzero")

### 3. While smyčka
# 6️⃣ Napište program, který bude **opakovaně** žádat uživatele o zadání čísla, dokud nezadá číslo větší než 100.
while True:
    zadej_cislo = float(input("Zdarec, zadej libovolné číslo!"))
    if zadej_cislo > 100:
        print("Pecka, zadal/a jsi číslo větší než 100.")
        break
    else:
        print("To nestačí, zkus to znovu!")

# 7️⃣ Napište program, který počítá **sčítání čísel od 1 do 10** pomocí `while` smyčky.
soucet = 0
cislo = 1

while cislo <= 10:
    soucet += cislo
    cislo += 1
print("Součet čísel od 1 do 10 je", soucet)

### 4. For smyčka
# 8️⃣ Napište `for` smyčku, která vypíše všechna sudá čísla od 1 do 20.
for number in range(2, 21, 2):
    print(number)

for number1 in range(1, 21):
    if number1 % 2 == 0:
        print(number1)

# 9️⃣ Vypište jednotlivé znaky ve slově `"Python"` pomocí `for` smyčky.
slovo = "Python"

for letter in slovo:
    print(letter)

### 5. Absolutní hodnota (abs)
# 🔟 Napište program, který přijme číslo od uživatele a vypíše jeho absolutní hodnotu.

cislo = float(input("Zadejte libovolné číslo."))

print("Jeho absolutní hodnota je: ", abs(cislo))

# 1️⃣1️⃣ Napište program, který porovná dvě čísla a zjistí jejich **vzdálenost na číselné ose**.
cislo1 = float(input("Zadejte první číslo."))
cislo2 = float(input("Zadejte druhé číslo."))

vzdalenost = abs(cislo1 - cislo1)

print("Vzdálenost mezi těmito dvěma čísly je: ", vzdalenost)

### 6. Seřazení seznamu (sort)
# 1️⃣2️⃣ Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
import random

nahodna_cisla = [random.randint(1, 100) for i in range(20)]

# pomocí sorted()
serazena_cisla = sorted(nahodna_cisla)
print(serazena_cisla)

# pomocí .sort
nahodna_cisla.sort()
print(nahodna_cisla)

# 1️⃣3️⃣ Napište program, který seřadí seznam slov podle abecedy.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
podle_abecedy = sorted(states_of_america)
print(podle_abecedy)
print(podle_abecedy[2])
print(podle_abecedy[-2])

### 7. Medián
# 1️⃣4️⃣ Napište program, který přijme seznam čísel od uživatele a najde jejich **medián**.
vstup = input("Ahojky, zadej čísla oddělená čárkou a já ti řeknu jejich medián (např: 10, 4, 6, 2).")
# Převod na seznam čísel (odstraní mezery a převede na float/int)
cisla2 = [float(x.strip()) for x in vstup.split(",")]

# Převod na seznam čísel (odstraní mezery a převede na float)
cisla2 = [float(x.strip()) for x in vstup.split(",")]

# Seřadíme seznam
cisla2.sort()

# Výpočet mediánu
n = len(cisla2)
if n % 2 == 1:
    median = cisla2[n // 2]  # prostřední prvek
else:
    median = (cisla2[n // 2 - 1] + cisla2[n // 2]) / 2  # průměr dvou prostředních

print("Medián zadaných čísel je:", median)

### 8. F-string (formátování textu)
# 1️⃣5️⃣ Napište program, který přijme jméno a věk uživatele a vypíše větu `"Ahoj, jmenuji se [jméno] a je mi [věk] let."` pomocí f-string.
name = input("Napiš své jméno:")
age = input("A kolik je ti let:")

print(f"Ahoj, jmenuji se {name} a je mi {age} let.")

### 9. Mapování hodnot (map)
# 1️⃣6️⃣ Napište program, který převede seznam číselných řetězců (např. `["1", "2", "3"]`) na čísla pomocí `map()`.
# 1️⃣7️⃣ Napište program, který převede seznam čísel na jejich druhé mocniny pomocí `map()`.

### 10. Zaokrouhlení čísel (round)
# 1️⃣8️⃣ Napište program, který přijme desetinné číslo od uživatele a zaokrouhlí ho na **2 desetinná místa**.
number3 = float(input("Napiš libovolné desetinné číslo, které má alespoň 4 čísla za desetinnou čárkou"))
zaokrouhlene = round(number3, 2)

# pokud chceš vždy výstup se 2 desetinnými čísly, i pro celá čísla, lze použít
number4 = 3
print(f"{number4:.2f}")

# 1️⃣9️⃣ Napište program, který vezme seznam desetinných čísel a zaokrouhlí každé číslo na **1 desetinné místo** pomocí `map()`.

### 11. Rozdělování textu (split)
# 2️⃣0️⃣ Napište program, který přijme větu od uživatele a rozdělí ji na jednotlivá slova pomocí `split()`.


###Bonusové kolo - nerozumim map() - beginner level

# 21 Převeď seznam textových čísel na celá čísla (např. ["1", "2", "3"] → [1, 2, 3])
text = ["1", "2", "3"]
cela_cisla = list(map(int, text))

print(cela_cisla)

# 22 Převeď seznam textových čísel na desetinná čísla

# desetinná textová na desetinná pomocí lambda - výsledek je list
textova_cisla = ["10.239", "25.786", "3.5", "8"]

desetinna_cisla = list(map(lambda x: f"{float(x):.2f}", textova_cisla))

print(desetinna_cisla)

# desetinná čísla a vypíšou se jako typ float, ale se 2 desetinnými čárkami
textova_cisla = ["10.239", "25.786", "3.5", "8"]

desetinna_cisla = list(map(lambda x: round(float(x), 2), textova_cisla))

for cislo in desetinna_cisla:
    print(f"{cislo:.2f}")

# celá čísla na desetinná


# 23 Zvětši každé číslo v seznamu o 10

# 24 Zdvojnásob každé číslo v seznamu

# 25 Zaokrouhli každé desetinné číslo na 2 desetinná místa

# 26 Převeď všechna slova v seznamu na VELKÁ písmena

# 27 Zkrať každé jméno na první 3 písmena

# 28 Spočítej délku každého slova v seznamu

# 29 Přidej 21% DPH ke každé ceně v seznamu

# 30 Zjisti, která čísla jsou větší než 100 (výsledkem bude True/False pro každé číslo)
