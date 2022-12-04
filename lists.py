## Créer une liste en python ##
listesEleve = []

## Ajouter une valeur à une liste python ##
listesEleve = ['Mahamadou', 'Omar', 'Michiel']

## Ou les ajouter après la création de la liste avec la méthode append (qui signifie "ajouter" en anglais): ##
listesEleve.append('Fatima') 
listesEleve.append(22) 
listesEleve.append('Awa') 
listesEleve.append('15') 
print(listesEleve)  # ['Mahamadou', 'Omar', 'Michiel', 'Fatima', 22, 'Awa', '15']

## Afficher un item d'une liste ##
listesEleve[3] = "Aminata"
print(listesEleve[3]) # Aminata 

## Supprimer une entrée avec un index ##
del listesEleve[4] 
del listesEleve[3] 
print(listesEleve)  # ['Mahamadou', 'Omar', 'Michiel', 'Awa', '15']

## Supprimer une entrée avec sa valeur ##
listesEleve.remove("Mahamadou")
listesEleve

## Inverser les valeurs d'une liste ##
listesEleve.reverse()
print(listesEleve) # ['15', 'Awa', 'Michiel', 'Omar', 'Mahamadou']


## Compter le nombre d'occurences d'une valeur ##
listesEleve.append('Mahamadou') # ajout Mahamadou
listesEleve.append('Mahamadou') # ajout Mahamadou
listesEleve.append('Mahamadou') # ajout Mahamadou
listesEleve.append('Mahamadou') # ajout Mahamadou

countIndex = listesEleve.count('Mahamadou')

print(countIndex) # 5

## Compter le nombre d'items d'une liste ##
print(listesEleve.__len__()) # 9

# Manipuler une liste
listeNombre = [1, 10, 100, 250, 500]
print(listeNombre[0]) # affiche 1
print(listeNombre[-1]) # affiche 500
print(listeNombre[-4]) # affiche 10
print(listeNombre[:]) # Affiche toutes les occurences
