#!/usr/bin/python3
for idx in range(0, 9):
    for idx2 in range(idx + 1, 10): #se servir de l'index de la précédente boucle
        if idx == 8 and idx2 == 9:
            print(f'{idx}{idx2}'.format())
        else:
            print(f'{idx}{idx2}'.format(), end=", ")


