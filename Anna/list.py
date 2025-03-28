#1 Napište program, který vytvoří seznam náhodných čísel a seřadí ho vzestupně.
import random

nahodna_cisla = [random.randint(1, 100) for i in range(20)]

#pomocí sorted()
serazena_cisla = sorted(nahodna_cisla)
print(serazena_cisla)

#pomocí .sort
nahodna_cisla.sort()
print(nahodna_cisla)

#2 Napište program, který seřadí seznam slov podle abecedy.
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
podle_abecedy = sorted(states_of_america)
print(podle_abecedy)
print(podle_abecedy[2])
print(podle_abecedy[-2])