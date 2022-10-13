#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    # TODO completer la fonction ici
    b = ''
    mot = str(mot)
    for ma in mot:
        numero = int(ord(ma))
        if (numero>96 and numero<123):
            nouveau = str(chr(ord(ma) - (97-65)))
            b = b+nouveau
        else:
            b = b + ma

    return b


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
