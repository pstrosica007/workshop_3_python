#1 Napište program, který na základě věku určí, zda je osoba dítě (do 12 let), teenager (13-17), dospělý (18-64) nebo senior (65+)
vek = int(input("Kolik je vám let?"))

if vek <= 12:
		print("Dítě")
elif vek <= 17:
		print("Teenager")
elif vek <= 64:
		print("Dospělý")
else:
		print("Senior")

#2 Napište program, který přijme číslo od uživatele a určí, zda je kladné, záporné nebo nula.
cislo = float(input("Zadejte libovolné číslo")

if cislo > 0:
		print("Kladné číslo.")
elif cislo < 0:
		print("Záporné číslo.")
else:
		print("Dzero")