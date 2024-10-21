def analyser_phrase():
    longueur_phrase = 0  # Compteur pour la longueur de la phrase
    nombre_mots = 0  # Compteur pour le nombre de mots
    nombre_voyelles = 0  # Compteur pour le nombre de voyelles
    voyelles = "aeiouAEIOU"  # Ensemble de voyelles

    # Initialisation pour le traitement des mots
    dans_un_mot = False

    print("Entrez une phrase (se termine par un point) :")

    while True:
        caractere = input()  # Lire un caractère à la fois

        if caractere == '.':
            # Si le caractère est un point, la phrase se termine
            if dans_un_mot:  # Vérification de la fin d'un mot
                nombre_mots += 1
            break  # Sortir de la boucle car la phrase est terminée

        # Incrémenter la longueur de la phrase pour chaque caractère lu
        longueur_phrase += 1

        # Vérification des voyelles
        if caractere in voyelles:
            nombre_voyelles += 1

        # Gestion des mots (supposant que les mots sont séparés par des espaces)
        if caractere != ' ':  # Si ce n'est pas un espace, on est dans un mot
            dans_un_mot = True
        else:
            if dans_un_mot:  # Si on sort d'un mot (après un espace)
                nombre_mots += 1
            dans_un_mot = False  # Réinitialisation pour le mot suivant

    # Résultats
    print("Longueur de la phrase :", longueur_phrase)
    print("Nombre de mots :", nombre_mots)
    print("Nombre de voyelles :", nombre_voyelles)

# Appel de la fonction
analyser_phrase()
