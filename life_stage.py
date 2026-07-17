print("We gaan je volwassenheid bepalen o.b.v. je leeftijd.")

leeftijd = int(input("Wat is je leeftijd?"))

# Werkt prima, maar bevat overbodige controles.
if leeftijd < 13:
    print("Je bent een kind.")
elif leeftijd >= 13 and leeftijd <= 17:
    print("Je bent een tiener.")
elif leeftijd >= 18 and leeftijd <= 66:
    print("Je bent volwassen.")
else:
    print("Je bent met pensioen.")

# Pythonic: gebruik de volgorde van if/elif.
# Zodra een voorwaarde waar is, worden de volgende voorwaarden niet meer gecontroleerd.
if leeftijd < 13:
    print("Je bent een kind.")
elif leeftijd <= 17:
    print("Je bent een tiener.")
elif leeftijd <= 66:
    print("Je bent volwassen.")
else:
    print("Je bent met pensioen.")

# Python ondersteunt ook chained comparisons.
# Dit is gelijkwaardig aan:
# leeftijd >= 13 and leeftijd <= 17
if leeftijd < 13:
    print("Je bent een kind.")
elif 13 <= leeftijd <= 17:
    print("Je bent een tiener.")
elif 18 <= leeftijd <= 66:
    print("Je bent volwassen.")
else:
    print("Je bent met pensioen.")
