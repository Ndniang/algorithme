# Phrased'entrée
phrase = "Bonjour je m'appelle ndeye fatou."

# Initialiser les compteurs
long_mot = 0
nbre_mots = 0
nombre_voyelles = 0

# Définir les voyelles
voyelles = "aeiouAEIOU"

# Parcourir chaque caractère de la phrase
for i in range(len(phrase) - 1):  # On ne compte pas le dernier point
    caractere = phrase[i]

    # Incrémenter le compteur de caractères
    long_mot += 1

    # Vérifier si le caractère est une voyelle
    if caractere in voyelles:
        nombre_voyelles += 1

    # Vérifier si le caractère est un espace 
    if caractere == ' ':
        nbre_mots += 1

# Ajouter un mot pour le dernier mot de la phrase (s'il y a des caractères)
if long_mot > 0:
    nbre_mots += 1

# Résultats
print("Longueur de la phrase (sans le point) :", long_mot)
print("Nombre de mots :", nbre_mots)
print("Nombre de voyelles :", nombre_voyelles)
