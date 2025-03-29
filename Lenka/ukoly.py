import math
"""
ÚKOL: Logické operátory (AND, OR, NOT)
1 Napište podmínku, která vrátí `True`, pokud `x` je větší než 10 **a zároveň** menší než 50.
2 Napište podmínku, která vrátí `True`, pokud `y` je menší než 5 **nebo** větší než 20.
3 Napište podmínku, která vrátí `True`, pokud `z` **není** rovno nule.
"""
def logical_operators_1():
    x = int(input("Enter a number:"))
    if (x > 10) and (x < 50):
        print(True)
    else:
        print(False)
    
logical_operators_1()

def logical_operators_2():
    y = int(input("Enter a number:"))
    if (y < 5) or (y >= 20):
        print(True)
    else:
        print(False)
    
logical_operators_2()

def logical_operators_3():
    z = int(input("Enter a number:"))
    if z != 0:
        print(True)
    else:
        print(False)

logical_operators_3()

"""
ÚKOL: If - elif - else
Napište program, který na základě věku určí, zda je osoba dítě (do 12 let), teenager (13-17), dospělý (18-64) nebo senior (65+).
Napište program, který přijme číslo od uživatele a určí, zda je kladné, záporné nebo nula.
"""
age = int(input("What age are you?"))

def what_age():
    if age <= 12:
        print("You are a child.")
    elif 13 <= age <=17:
        print("You are a teenager.")
    elif 18 <= age <= 64:
        print("You are an adult.")
    else:
        print("You are an elder.")

what_age()

"""
ÚKOL: While smyčka
Napište program, který bude **opakovaně** žádat uživatele o zadání čísla, dokud nezadá číslo větší než 100.
Napište program, který počítá **sčítání čísel od 1 do 10** pomocí `while` smyčky.
"""
#TODO:

"""
ÚKOL: For smyčka
Napište `for` smyčku, která vypíše všechna sudá čísla od 1 do 20.
Vypište jednotlivé znaky ve slově `"Python"` pomocí `for` smyčky.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def loopy_loop():
    for n in numbers:
        if n%2 == 0:
            print(n)
        else:
            pass
loopy_loop()

word = "Python"

def word_loop():
    for w in word:
        print(w)
word_loop()

"""
ÚKOL: Absolutní hodnota (abs)
Napište program, který přijme číslo od uživatele a vypíše jeho absolutní hodnotu.
Napište program, který porovná dvě čísla a zjistí jejich **vzdálenost na číselné ose**.
"""

#TODO: dodělat


"""
ÚKOL: Seřazení seznamu (sort)
Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
Napište program, který seřadí seznam slov podle abecedy.
"""

#TODO: dodělat


"""
ÚKOL: Medián
Napište program, který přijme seznam čísel od uživatele a najde jejich **medián**.
"""
#TODO: dodělat


"""
ÚKOL: F-string (formátování textu)
Napište program, který přijme jméno a věk uživatele a vypíše větu `"Ahoj, jmenuji se [jméno] a je mi [věk] let."` pomocí f-string.
"""
def who_are_you():
    name = input("What is ypour name?")
    age = input("How old are you?")

    print(f"Hi, my name is {name} and I am {age} years old.")


"""
ÚKOL: Mapování hodnot (map)
Napište program, který převede seznam číselných řetězců (např. `["1", "2", "3"]`) na čísla pomocí `map()`.
Napište program, který převede seznam čísel na jejich druhé mocniny pomocí `map()`.
"""


#TODO: dodělat


"""
ÚKOL: Zaokrouhlení čísel (round)
1 Napište program, který přijme desetinné číslo od uživatele a zaokrouhlí ho na **2 desetinná místa**.
2 Napište program, který vezme seznam desetinných čísel a zaokrouhlí každé číslo na **1 desetinné místo** pomocí `map()`.
"""
number = float(input("Enter a float:"))

def rounding_one():
    if number:
        print(round(number, 2))
    else:
        "You did not enter a number. Try again."
rounding_one()

input = [1.00000, 25.6565989, 2.1, 6.2328, 9.2358, 12.347, 20.6453695]

#TODO: dodělat 2

"""
ÚKOL: Rozdělování textu (split)
Napište program, který přijme větu od uživatele a rozdělí ji na jednotlivá slova pomocí `split()`.
"""
def split_text():
    text = input("Enter a sentence, please.")
    transform = text.split(" ")
    print(transform)

split_text()