print("We gaan de ruimte per plant berekenen.")

aantal_planten = int(input("Hoeveel planten heb je beschikbaar?"))
oppervlakte = float(input("Hoe groot is het stuk dat je wilt aanplanten in m2? Dit mag met decimalen."))

ruimte_per_plant = oppervlakte / aantal_planten

print(f"Je hebt gemiddeld {ruimte_per_plant:.2f} m2 per plant.")

if ruimte_per_plant < 5:
    print("De planten staan erg dicht op elkaar.")
elif ruimte_per_plant < 15:
    print("De plantafstand lijkt prima.")
else:
    print("Je hebt veel ruimte per plant beschikbaar.")
