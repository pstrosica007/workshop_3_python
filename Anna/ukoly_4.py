# Cvičení: Debugging & Úfvod do OOP v Pythonu

# ==============================
# 🔧 1. DEBUGGING
# ==============================

# ❌ 1.1 Najdi a oprav chyby v následujících funkcí

# a) Typova chyba

def multiply(a, b):
    return a * b


# Test:
# multiply("3", 2)  # Očekávaný výsledek: TypeError nebo oprava logiky

# b) Chyba v podmínce

def is_even(n):
    if n % 2 = 0:
        return True
    else:
        return False


# c) Nekonečná rekurze

def broken_factorial(n):
    return n * broken_factorial(n - 1)


# d) Ladění pomocí print()

def debug_bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                print("Iterace:", data)
    return data

# ==============================
# 📃 2. OOP: Základy
# ==============================

# 🤖 2.1 Vytvoř třídu Dog, která bude mít:
# - atributy: name, age
# - metodu speak(), která vypíše "Woof, my name is ..."

# Test:
# dog1 = Dog("Rex", 5)
# dog1.speak()  # "Woof, my name is Rex"

# 📕 2.2 Vytvoř třídu Book s metodami:
# - __init__(title, author)
# - describe(), která vypíše např. "Kniha: 1984, autor: Orwell"

# 💪 2.3 Třída Player
# - atributy: name, score (zační na 0)
# - metoda add_score(points)
# - metoda show_score()

# Test:
# p = Player("Andy")
# p.add_score(50)
# p.show_score()  # "Andy has 50 points"

# ==============================
# 🌟 3. Bonus
# ==============================

# 📊 3.1 Vytvoř třídu FileAnalyzer:
# - metoda __init__(file_path)
# - metoda count_lines() → počítá řádky
# - metoda count_words() → počítá slova
# - metoda file_size() → velikost v bajtech

# Test:
# analyzer = FileAnalyzer("sample.txt")
# analyzer.count_lines()
# analyzer.count_words()
# analyzer.file_size()

# 📌 3.2 Třídící algoritmus jako třída (Sorter)
# Zopakuj příklad bubble sort/quick sort z minula, ale napiš novou třídu, která bude mít:
# - metody bubble_sort(), quick_sort()
# - uložený vstupní list v __init__
