# Un dictionnaire en python est une sorte de liste mais au lieu d'utiliser des index , on utilise des clés alphanumériques

person = {"fristname": "Mahamadou", "name": "Diaby", "mail": "kherabadiaby328@gmail.com"}

# obtenir une valeur dans un dictionnaire
print("you are: {} {}".format(person.get("fristname"), person.get("name")))

print("--------------------------")

# Comment supprimer une entrée dans un dictionnaire python?
del person["mail"]
print(person)

# Comment récupérer les clés d'un dictionnaire python par une boucle?

for key in person.keys(): 
    print(key)

print("--------------------------")
# Comment récupérer les valeurs d'un dictionnaire python par une boucle?
for value in person.values(): 
    print(value)

print("--------------------------")
# Comment récupérer les clés et les valeurs d'un dictionnaire python par une boucle?
for key, value in person.items(): 
    print(key,":", value)

print("--------------------------")
# Comment créer une copie indépendante d'un dictionnaire python?
person1 = person.copy()

print(person1)

print("--------------------------")
# Comment fusionner des dictionnaires python?

inforperson = {"sexe": "Male", "age": 22}
person.update(inforperson)
print(person)
