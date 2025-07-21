### 🧱 Základy OOP v Pythonu – pro začátečníky

#### 1. Co je OOP (Object-Oriented Programming)?

OOP je programovací paradigma založené na objektech. Objekt je kombinace **dat** (atributů) a **chování** (metod).

Výhody:

* Lepší organizace kódu (modularita)
* Znovupoužitelnost pomocí dědičnosti (reuse)
* Snazší údržba a rozšiřování kódu (rozšiřitelnost)
* Možnost pracovat s reálnými entitami (např. uživatel, auto, účet)

---

#### 2. Třídy a instance

* **Třída** (class) je šablona, podle které se vytvářejí objekty.
* **Instance** je konkrétní objekt vytvořený z dané třídy.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} štěká")

my_dog = Dog("Azor")
my_dog.bark()  # Azor štěká
```

---

#### 3. Konstruktor `__init__`

* `__init__` je speciální metoda, která se automaticky zavolá při vytvoření nové instance.
* Slouží k nastavení výchozích hodnot (inicializace).

```python
class User:
    def __init__(self, username):
        self.username = username
```

---

#### 4. `self` – odkaz na instanci

* `self` se používá pro přístup k atributům a metodám konkrétní instance.
* Musí být vždy prvním parametrem metody v třídě.

```python
class Device:
    def show_info(self):
        print(f"Jsem objekt typu {type(self)}")
```

---

#### 5. Atributy a metody

* **Atributy**: data uložená v objektu (např. `jmeno`, `vek`)
* **Metody**: funkce definované v třídě, které manipulují s daty nebo poskytují chování

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def honk(self):
        print(f"{self.brand} říká: píp píp!")
```

---

#### 6. Dědičnost

* Pomocí dědičnosti lze vytvořit novou třídu, která přebírá chování a atributy jiné (rodičovské) třídy.

```python
class Animal:
    def speak(self):
        print("Zvuk")

class Cat(Animal):
    def speak(self):
        print("Mňau")

c = Cat()
c.speak()  # Mňau
```

---

#### 7. Přepisování metod (Overriding)

* Potomci mohou přepsat metody zděděné z rodičů vlastním chováním.

```python
class Parent:
    def greet(self):
        print("Ahoj")

class Child(Parent):
    def greet(self):
        print("Čau")
```

---

#### 8. `super()`

* `super()` umožňuje přístup k metodám rodičovské třídy. Používá se často při přepisování `__init__`.

```python
class Parent:
    def __init__(self):
        print("Init parent")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Init child")
```

---

#### 9. Zapouzdření (Encapsulation)

* Cílem je skrýt interní implementaci a vystavit jen to, co je potřeba.
* V Pythonu používáme konvenci `_protected` a `__private`.

```python
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
```

---

#### 10. Reprezentace objektu: `__str__()`

* Umožňuje definovat, jak má objekt vypadat při výpisu pomocí `print()`.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Jméno: {self.name}"

p = Person("Andy")
print(p)  # Jméno: Andy
```

---

#### 11. `@property` – elegantní přístup k atributům

* Umožňuje definovat atribut, který se chová jako metoda.
* Výhodné, když chceš zpětně zavést logiku bez změny API.

```python
class Square:
    def __init__(self, side):
        self._side = side

    @property
    def area(self):
        return self._side ** 2
```

---

#### 12. `@staticmethod` vs `@classmethod`

* `@staticmethod`: metoda nepracuje s třídou ani instancí – čistá funkce ve třídě.
* `@classmethod`: metoda pracuje s třídou jako celkem (`cls`) – typicky pro alternativní konstruktory.

```python
class Example:
    @staticmethod
    def add(x, y):
        return x + y

    @classmethod
    def from_string(cls, data):
        return cls(*data.split(","))
```

---

#### 13. `@dataclass`

* Zjednodušuje zápis tříd pro ukládání dat.
* Automaticky generuje `__init__`, `__repr__`, `__eq__` atd.

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(1, 2)
print(p)  # Point(x=1, y=2)
```

---

#### 14. Základní návrhové vzory (design patterns)

* **Singleton**: jen jedna instance (viz předchozí části)
* **Factory**: vytváří objekty podle vstupu
* **Strategy**: dynamická volba algoritmu
* **Observer**: reakce na změnu stavu (např. UI notifikace)

---

### 🧪 Praktický úkol pro OOP začátečníka

**Zadání:**
Navrhni třídy pro knihovní systém:

* `Book`: má název, autora, rok vydání a dostupnost
* `User`: má jméno a seznam vypůjčených knih
* `Library`: umí přidat knihu, půjčit knihu uživateli, zobrazit dostupné knihy

**Cíle:**

* Procvičit `__init__`, `__str__`, dědičnost (volitelně)
* Použít metody a atributy
* Zamyslet se nad zapouzdřením (`_books`, `__borrowed_books` apod.)

Můžeš později rozšířit o správu vrácení knihy, omezení výpůjček, nebo dědičnost (např. `Ebook`, `PrintedBook`).
