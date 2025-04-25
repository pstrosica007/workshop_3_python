import math
import random

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
4 Napište program, který na základě věku určí, zda je osoba dítě (do 12 let), teenager (13-17), dospělý (18-64) nebo senior (65+).
5 Napište program, který přijme číslo od uživatele a určí, zda je kladné, záporné nebo nula.
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
6 Napište program, který bude **opakovaně** žádat uživatele o zadání čísla, dokud nezadá číslo větší než 100.
7 Napište program, který počítá **sčítání čísel od 1 do 10** pomocí `while` smyčky.
"""
def asking_numbers():
    question = int(input("Please enter a number: "))
    answer = question

    while answer < 101:
        next_question = int(input("Please enter another number: "))
        answer = next_question
    else:
        print("You passed the limit of 100.")
asking_numbers()

def counting_numbers():
    i = 0
    j = 0

    while i < 11:
        j += i
        i += 1
    print(j)
counting_numbers()

"""
ÚKOL: For smyčka
8 Napište `for` smyčku, která vypíše všechna sudá čísla od 1 do 20.
9 Vypište jednotlivé znaky ve slově `"Python"` pomocí `for` smyčky.
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
10 Napište program, který přijme číslo od uživatele a vypíše jeho absolutní hodnotu.
11 Napište program, který porovná dvě čísla a zjistí jejich **vzdálenost na číselné ose**.
"""

def finding_abs():
    number = float(input("Please enter a number: "))
    abs_number = abs(number)
    print(f"Absolute number for your choice is: {abs_number}")
finding_abs()

"""
ÚKOL: Seřazení seznamu (sort)
12 Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
13 Napište program, který seřadí seznam slov podle abecedy.
"""
def sorting_random_numbers():
    list_of_numbers = []
    for i in range(10):
        i = random.randint(0, 100)
        list_of_numbers.append(i)
    list_of_numbers.sort()
    print(list_of_numbers)

sorting_random_numbers()

def sorting_words():
    list_of_words = ["banana", "lemon", "apple", "melon", "cherry", "plum", "avocado"]
    list_of_words.sort()
    print(list_of_words)

sorting_words()

"""
ÚKOL: Medián
14 Napište program, který přijme seznam čísel od uživatele a najde jejich **medián**.
"""
def median_calculation():
    user_numbers = []
    for i in range(10):
        i = float(input("Add a number into the list: "))
        user_numbers.append(i)
    user_numbers.sort()
    length = len(user_numbers)
    center = length // 2
    if length % 2 == 1:
        print(user_numbers[center])
    else:
        print((user_numbers[center - 1] + user_numbers[center]) / 2)
median_calculation()

"""
ÚKOL: F-string (formátování textu)
15 Napište program, který přijme jméno a věk uživatele a vypíše větu `"Ahoj, jmenuji se [jméno] a je mi [věk] let."` pomocí f-string.
"""
def who_are_you():
    name = input("What is ypour name?")
    age = input("How old are you?")

    print(f"Hi, my name is {name} and I am {age} years old.")


"""
ÚKOL: Mapování hodnot (map)
16 Napište program, který převede seznam číselných řetězců (např. `["1", "2", "3"]`) na čísla pomocí `map()`.
17 Napište program, který převede seznam čísel na jejich druhé mocniny pomocí `map()`.
"""


#TODO: dodělat


"""
ÚKOL: Zaokrouhlení čísel (round)
18 Napište program, který přijme desetinné číslo od uživatele a zaokrouhlí ho na **2 desetinná místa**.
19 Napište program, který vezme seznam desetinných čísel a zaokrouhlí každé číslo na **1 desetinné místo** pomocí `map()`.
"""
number = float(input("Enter a float:"))

def rounding_one():
    if number:
        print(round(number, 2))
    else:
        print("You did not enter a number. Try again.")
rounding_one()

numbers = [1.00000, 25.6565989, 2.1, 6.2328, 9.2358, 12.347, 20.6453695]

#TODO: dodělat 2

"""
ÚKOL: Rozdělování textu (split)
20 Napište program, který přijme větu od uživatele a rozdělí ji na jednotlivá slova pomocí `split()`.
"""
def split_text():
    text = input("Enter a sentence, please.")
    transform = text.split(" ")
    print(transform)

split_text()