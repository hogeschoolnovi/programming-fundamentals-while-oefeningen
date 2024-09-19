#
# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoevaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.

# De beschikbare muntwaarden
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1

# Vraag de gebruiker om een bedrag in centen
bedrag = int(input("Voer het bedrag in centen in: "))

# While-loop om het wisselgeld te berekenen
while bedrag > 0:
    if bedrag >= vijftig_cent:
        aantal_vijftig = bedrag // vijftig_cent
        bedrag -= aantal_vijftig * vijftig_cent
        print(f"{aantal_vijftig} x 50 cent munt")

    elif bedrag >= twintig_cent:
        aantal_twintig = bedrag // twintig_cent
        bedrag -= aantal_twintig * twintig_cent
        print(f"{aantal_twintig} x 20 cent munt")

    elif bedrag >= tien_cent:
        aantal_tien = bedrag // tien_cent
        bedrag -= aantal_tien * tien_cent
        print(f"{aantal_tien} x 10 cent munt")

    elif bedrag >= vijf_cent:
        aantal_vijf = bedrag // vijf_cent
        bedrag -= aantal_vijf * vijf_cent
        print(f"{aantal_vijf} x 5 cent munt")

    else:
        aantal_een = bedrag // een_cent
        bedrag -= aantal_een * een_cent
        print(f"{aantal_een} x 1 cent munt")