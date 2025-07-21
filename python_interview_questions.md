# 💡 Kategorie otázek z pohovorů pro Python

Tento přehled shrnuje typické otázky a úkoly, které se objevují při technických pohovorech na Python roli – od juniorních až po seniorní pozice.

---

## 🧠 1. Teoretické otázky – Junior/Mid

Zaměřené na pochopení jazyka, datových typů, paměti atd.

- Jaký je rozdíl mezi `list`, `tuple`, `set` a `dict`?
- Co je to mutabilita? Které datové typy jsou mutable a které ne?
- Jak funguje `*args` a `**kwargs`?
- Jaký je rozdíl mezi `is` a `==`?
- Co je to list comprehension?
- Co dělá `@staticmethod` vs `@classmethod`?
- Co je to `__init__` a proč ho používáme?
- Co je PEP8?
- Jaký je rozdíl mezi Python 2 a Python 3 (high level)?
- Jak Python pracuje s pamětí a garbage collectorem?

---

## 🧪 2. Praktické úkoly (kódování během pohovoru) – Junior/Mid

Většinou formou: _"napiš funkci, která..."_

### ✅ Základy
- Spočítej počet výskytů každého znaku ve stringu.
- Najdi největší číslo v seznamu bez použití `max()`.
- Napiš funkci, která kontroluje, zda je slovo palindrom.
- Otoč seznam (nebo string) bez použití `reversed()` nebo `[::-1]`.
- Napiš funkci, která vypíše prvních `n` Fibonacciho čísel.

### 🧩 Mírně pokročilé
- Najdi druhé největší číslo v seznamu.
- Odstraň duplikáty ze seznamu.
- Vytvoř funkci, která vrátí anagramy ze seznamu slov.
- Vytvoř slovník ze seznamu klíčů a seznamu hodnot.
- Implementuj FizzBuzz do 100.

### 🔍 Logika + stringy
- Najdi první neopakující se znak ve stringu.
- Zapiš funkci pro kontrolu platnosti emailové adresy.
- Převod římských číslic na arabské a zpět.

---

## 📚 Struktura otázek pro pohovor – Mid/Senior

### ✅ Základy (kontrola porozumění jazyku)
- Jaký je rozdíl mezi `list`, `set`, `tuple`, `dict`?
- Co je `None`, jak se liší od `False`, `0`, `''`?
- Jaký je rozdíl mezi `is` a `==`?
- Co je to shallow copy vs deep copy?
- Co je `__name__ == "__main__"` a proč se používá?

### 🛠 Pokročilejší témata
- Vysvětli rozdíl mezi `mutable` a `immutable` typy a jak to ovlivňuje chování funkcí.
- Jak funguje `*args`, `**kwargs` a kdy je použít?
- Jak funguje paměťový model v Pythonu? (ref counting, GC)
- Jak se v Pythonu implementuje singleton?
- Rozdíl mezi `staticmethod`, `classmethod`, a `instancemethod`.

---

## 🧵 Paralelismus a výkonnost
- Rozdíl mezi `threading`, `multiprocessing`, a `asyncio`.
- Co je GIL (Global Interpreter Lock)?
- Kdy použít `async def` místo vláken?

---

## 💻 Testování a architektura
- Rozdíl mezi `unittest`, `pytest` a `doctest`.
- Jak testovat funkci, která zapisuje na disk nebo pracuje s API?
- Co je dependency injection a jak se řeší v Pythonu?
- Jaké znáš návrhové vzory a kdy bys je použila?

---

## ⚙️ Praktická znalost knihoven
- Kdy použít `collections.defaultdict` vs `dict.setdefault`?
- Rozdíl mezi `pandas` a `numpy`.
- K čemu slouží `functools.lru_cache`?

---

## 🧪 Praktické úkoly – Mid/Senior

### ✅ Jednodušší algoritmické úkoly
- Otočení stringu bez `[::-1]`.
- Histogram četnosti znaků.
- Fibonacciho posloupnost (iterativní i rekurzivní).
- Validátor závorek: `"{[()]}"` → `True`, `"{[(])}"` → `False`

### 🧩 Střední úroveň
- Zjisti, zda dvě slova jsou anagramy.
- Najdi první opakující se prvek v seznamu.
- Najdi všechny páry čísel ze seznamu, jejichž součet je `k`.

### 🔥 Pokročilé úlohy (senior)
- Implementuj LRU cache (bez knihovny).
- Dekorátor, který loguje čas běhu funkce.
- Mini-verze `grep` v Pythonu.
- Parser dotazu typu `name=Andy AND age>30 OR city=Prague`.
- REST API pomocí FastAPI, které přijímá JSON a vrací upravená data.

### ⚙️ Design/Architecture Tasks
- Aplikace, která parsuje e-maily a ukládá přílohy.
- Rate limiting systém (např. max 10 požadavků za 60 sekund).
- CLI nástroj pro mazání logů starších než X dní.

---
