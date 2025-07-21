### 1. Jaký je rozdíl mezi `list`, `tuple`, `set` a `dict`?

| Typ   | Seřazený | Unikátní prvky | Mutable | Inicializace | Přidání     | Odebrání    |
| ----- | -------- | -------------- | ------- | ------------ | ----------- | ----------- |
| list  | ✅        | ❌           | ✅      | `[1, 2, 3]`  | `.append()` | `.remove()` |
| tuple | ✅        | ❌           | ❌      | `(1, 2, 3)`  | nelze       | nelze       |
| set   | ❌        | ✅           | ✅      | `{1, 2, 3}`  | `.add()`    | `.remove()` |
| dict  | ❌        | ✅ (klíče)   | ✅      | `{"a": 1}`   | `d[k] = v`  | `del d[k]`  |

**Ukázka kódu:**

```python
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}
```

**Kdy co použít?**

* `list`: když potřebuješ zachovat pořadí a často měníš data.
* `tuple`: pro konstantní sekvence, např. souřadnice nebo návrat více hodnot.
* `set`: když tě zajímají pouze unikátní hodnoty.
* `dict`: když chceš ukládat páry klíč-hodnota.

---

### 2. Co je to mutabilita? Které datové typy jsou mutable a které ne?

**Mutabilita** znamená schopnost objektu měnit svůj obsah bez změny jeho identity.

| Datový typ     | Mutable |
| -------------- | ------- |
| `int`, `float` | ❌      |
| `str`          | ❌      |
| `tuple`        | ❌      |
| `list`         | ✅      |
| `dict`         | ✅      |
| `set`          | ✅      |

---

### 3. Jak funguje `*args` a `**kwargs`?

* `*args` sbírá všechny poziční argumenty do `tuple`
* `**kwargs` sbírá všechny pojmenované argumenty do `dict`

**Ukázka:**

```python
def my_func(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

my_func(1, 2, 3, a=10, b=20)
# args: (1, 2, 3)
# kwargs: {'a': 10, 'b': 20}
```

---

### 4. Jaký je rozdíl mezi `is` a `==`?

* `==` porovnává hodnotu objektů
* `is` porovnává identitu objektů (jestli ukazují na stejný objekt v paměti)

**Ukázka:**

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == c)  # True
print(a is c)  # False
print(a is b)  # True
```

---

### 5. Co je to list comprehension?

Zkrácený zápis pro tvorbu seznamů z iterovatelných objektů.

**Ukázka:**

```python
numbers = [1, 2, 3, 4]
squares = [n**2 for n in numbers]  # [1, 4, 9, 16]
```

Výhoda: přehledný a efektivní zápis bez nutnosti vytvářet nový prázdný seznam a cyklus `for`.

---

### 6. Co dělá `@staticmethod` vs `@classmethod`?

* `@staticmethod`: metoda, která nevyužívá instanci ani třídu – chová se jako běžná funkce, ale je součástí třídy kvůli logickému uspořádání.
* `@classmethod`: metoda, která má přístup k samotné třídě (`cls`) – používá se např. pro alternativní konstruktory.

**Příklad:**

```python
class Example:
    @staticmethod
    def static_hello():
        return "Hello from static!"

    @classmethod
    def class_hello(cls):
        return f"Hello from {cls.__name__}"
```

---

### 7. Co je to `__init__` a proč ho používáme?

Je to konstruktor třídy – spustí se při vytvoření instance a inicializuje její vlastnosti.

**Ukázka:**

python
class Device:
    def __init__(self, name, status):
        self.name = name
        self.status = status

printer = Device("HP LaserJet", "online")
print(printer.name)  # HP LaserJet


---

### 8. Co je PEP8?

PEP8 je oficiální dokument, který definuje doporučení pro styl psaní Python kódu.

**Top 10 pravidel:**

1. Používej odsazení 4 mezery.
2. Maximální délka řádku je 79 znaků.
3. Používej smysluplné názvy proměnných.
4. Funkce a proměnné píš `lower_case_with_underscores`.
5. Třídy píš `CamelCase`.
6. Importy piš na začátku souboru ve třech blocích: standardní knihovna, 3rd party, vlastní moduly.
7. Mezera kolem operátorů: `a = b + c`, ne `a=b+c`.
8. Prázdný řádek mezi funkcemi a metodami.
9. Komentuj jen to, co není zřejmé z kódu.
10. Používej `docstring` pro dokumentaci funkcí a tříd.

---

### 9. Jaký je rozdíl mezi Python 2 a Python 3 (high level)?

* **Python 2** je zastaralá verze (podpora skončila v roce 2020), zatímco **Python 3** je současný standard.
* Hlavní rozdíly:

  * `print` je funkce v Pythonu 3: `print("ahoj")`, v Python 2 byl příkaz: `print "ahoj"`
  * V Pythonu 3 je výchozí `str` typ Unicode.
  * Dělení `/` v Python 3 vždy vrací float, zatímco v Python 2 celé číslo, pokud jsou oba operandy `int`.
  * Mnoho funkcí jako `range`, `zip`, `map` vrací iterátory místo seznamů.

```python
# Python 2
print "hello"

# Python 3
print("hello")
```

---

### 10. Jak Python pracuje s pamětí a garbage collectorem?

* Python používá **referenční počítání** – každý objekt má čítač, kolikrát je na něj odkazováno.
* Když čítač dosáhne nuly, objekt se odstraní.
* Pro odstranění **cyklických referencí** (např. objekt odkazuje sám na sebe) Python používá **garbage collector** (`gc` modul).

```python
import gc
print(gc.get_threshold())  # aktuální nastavení GC
```

---

### 11. Co je `None`, jak se liší od `False`, `0`, `''`?

* `None` je speciální objekt značící „nic“, nebo „žádná hodnota“.
* `0`, `''` a `False` jsou konkrétní hodnoty, které se v logickém kontextu vyhodnocují jako `False`.
* `None` není totéž co `False` – neprováděj `if x == False` pro testování na `None`, použij `if x is None`.

```python
x = None
print(bool(x))      # False
print(x == False)   # False
print(x is None)    # True
```

Použití: např. když funkce nic nevrací, automaticky vrátí `None`.

---

### 12. Co je to `shallow copy` vs `deep copy`?

* `Shallow copy` vytvoří novou strukturu, ale vnitřní objekty zůstávají odkazy na původní.
* `Deep copy` rekurzivně zkopíruje vše, včetně vnořených objektů.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999
print(shallow)  # [[999, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]
```

---

### 13. Co je to `__name__ == "__main__"` a proč se používá?

* Konstrukce slouží k určení, zda je skript spouštěn přímo nebo importován jako modul.
* Umožňuje mít v souboru jak kód pro import, tak i pro přímé spuštění.

```python
def pozdrav():
    print("Ahoj")

if __name__ == "__main__":
    pozdrav()
```

Když tento soubor spustíš přímo: spustí se `pozdrav()`.
Když ho importuješ jako modul: nespustí se nic.

---

### 9. Jaký je rozdíl mezi Python 2 a Python 3 (high level)?

* **Python 2** je zastaralá verze (podpora skončila v roce 2020), zatímco **Python 3** je současný standard.
* Hlavní rozdíly:

  * `print` je funkce v Pythonu 3: `print("ahoj")`, v Python 2 byl příkaz: `print "ahoj"`
  * V Pythonu 3 je výchozí `str` typ Unicode.
  * Dělení `/` v Python 3 vždy vrací float, zatímco v Python 2 celé číslo, pokud jsou oba operandy `int`.
  * Mnoho funkcí jako `range`, `zip`, `map` vrací iterátory místo seznamů.

```python
# Python 2
print "hello"

# Python 3
print("hello")
```

---

### 10. Jak Python pracuje s pamětí a garbage collectorem?

* Python používá **referenční počítání** – každý objekt má čítač, kolikrát je na něj odkazováno.
* Když čítač dosáhne nuly, objekt se odstraní.
* Pro odstranění **cyklických referencí** (např. objekt odkazuje sám na sebe) Python používá **garbage collector** (`gc` modul).

```python
import gc
print(gc.get_threshold())  # aktuální nastavení GC
```

---

### 11. Co je `None`, jak se liší od `False`, `0`, `''`?

* `None` je speciální objekt značící „nic“, nebo „žádná hodnota“.
* `0`, `''` a `False` jsou konkrétní hodnoty, které se v logickém kontextu vyhodnocují jako `False`.
* `None` není totéž co `False` – neprováděj `if x == False` pro testování na `None`, použij `if x is None`.

```python
x = None
print(bool(x))      # False
print(x == False)   # False
print(x is None)    # True
```

Použití: např. když funkce nic nevrací, automaticky vrátí `None`.

---

### 12. Co je to `shallow copy` vs `deep copy`?

* `Shallow copy` vytvoří novou strukturu, ale vnitřní objekty zůstávají odkazy na původní.
* `Deep copy` rekurzivně zkopíruje vše, včetně vnořených objektů.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999
print(shallow)  # [[999, 2], [3, 4]]
print(deep)     # [[1, 2], [3, 4]]
```

---

### 13. Co je to `__name__ == "__main__"` a proč se používá?

* Konstrukce slouží k určení, zda je skript spouštěn přímo nebo importován jako modul.
* Umožňuje mít v souboru jak kód pro import, tak i pro přímé spuštění.

```python
def pozdrav():
    print("Ahoj")

if __name__ == "__main__":
    pozdrav()
```

Když tento soubor spustíš přímo: spustí se `pozdrav()`.
Když ho importuješ jako modul: nespustí se nic.

---

### 14. Vysvětli rozdíl mezi mutable a immutable typy a jak to ovlivňuje chování funkcí

* **Mutable** objekty (např. `list`, `dict`) lze měnit bez vytvoření nové instance.
* **Immutable** objekty (např. `int`, `str`, `tuple`) po změně vytváří novou instanci.
* Funkce, která mění `mutable` typ, změní i původní objekt mimo funkci.

```python
def modify_list(lst):
    lst.append(99)

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 99]

# Immutable typy
x = "hello"
def to_upper(s):
    s = s.upper()
    return s

print(to_upper(x))  # "HELLO"
print(x)            # "hello" (původní zůstává)
```

---

### 15. Jak se v Pythonu implementuje singleton?

Singleton zajistí, že ze třídy vznikne pouze jedna instance.

**Příklad pomocí `__new__`:**

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True
```

---

### 16. Jaký je rozdíl mezi `staticmethod`, `classmethod`, a běžnou metodou (instancemethod)?

| Dekorátor       | Přístup k instanci | Přístup ke třídě | Kdy použít                                |
| --------------- | ------------------ | ---------------- | ----------------------------------------- |
| žádný (metoda)  | ✅ (`self`)         | ❌                | Práce s daty konkrétní instance           |
| `@classmethod`  | ❌                  | ✅ (`cls`)        | Např. alternativní konstruktory           |
| `@staticmethod` | ❌                  | ❌                | Pomocné funkce, které nepotřebují kontext |

---

### 17. Jak funguje paměťový model v Pythonu? (ref counting, GC)

* Každý objekt má **referenční čítač**, který se zvyšuje/snižuje při přiřazení/odstranění odkazu.
* Když čítač klesne na 0, objekt se smaže.
* Modul `gc` detekuje a odstraní cyklické reference.

```python
import sys
x = []
print(sys.getrefcount(x))  # výchozí počet referencí
```

---

### 18. Jak funguje `*args`, `**kwargs` a kdy je použít?

* `*args` – pro proměnný počet **pozičních argumentů**
* `**kwargs` – pro proměnný počet **pojmenovaných argumentů**
* Použijeme je, pokud předem nevíme, kolik argumentů funkce přijme, nebo pokud chceme předávat argumenty dál (např. při dědění).

```python
def log_event(event, *args, **kwargs):
    print("Event:", event)
    print("Args:", args)
    print("Kwargs:", kwargs)

log_event("start", 10, 20, user="andy", debug=True)
```

---



