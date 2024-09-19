# In deze opdracht ga je een script schrijven waarbij de gebruikter een geheim getal moet raden.
#
# Stappenplan:
#
# 1. Maak een variabele "random_getal" en geef deze een willekeurige integer waarde tussen 1 en 10.
# 2. Vraag de gebruiker om het getal te raden
# 3. Gebruik een while-loop die blijft draaien zolang de gebruiker het verkeerde getal raadt.
# 4. Geef feedback of de ingevoerde waarde te hoog of te laag is.
# 5. Wanneer de gebruiker het juiste getal raadt, beëindig de loop en print een felicitatiebericht.
#
# BONUS: Gebruik `import random` en `random.randomInt(1, 10)` om je geheime getal mee te maken
# en deze zo ook voor jezelf geheim te houden.


correct_number = 8
user_guess = None

while user_guess != correct_number:
    user_guess = int(input("Raad het getal tussen 1 en 10: "))
    if user_guess < correct_number:
        print("Te laag!")
    elif user_guess > correct_number:
        print("Te hoog!")
    else:
        print("Gefeliciteerd, je hebt het geraden!")
