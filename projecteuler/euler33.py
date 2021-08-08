fracs = []

for nom in range(10,100):
    for denom in range(nom, 100):
        list_nom = [int(c) for c in str(nom)]
        list_denom = [int(c) for c in str(denom)]

        nom_0 = list_nom[0]
        nom_1 = list_nom[1]
        for nom_i in [nom_0, nom_1]:
            if nom_i in list_denom:
                list_nom_copy = list_nom.copy()
                list_nom_copy.remove(nom_i)
                list_denom_copy = list_denom.copy()
                list_denom_copy.remove(nom_i)

                new_nom = list_nom_copy[0]
                new_denom = list_denom_copy[0]
                try:
                    if nom/denom == new_nom / new_denom and nom_i != 0 and nom != denom:
                        print("Adding: ", nom, denom)
                        fracs.append([nom, denom])
                except:
                    pass

print(fracs)
bignom = 1
bigdenom = 1
for (nom, denom) in fracs:
    bignom *= nom
    bigdenom *= denom

print(bignom, bigdenom)
print(bignom / bigdenom)