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
