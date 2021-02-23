import re, sys, hashlib, time
alphabet  = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','@','_','#','0','1','2','3','4','5','6','7','8','9']
max = 11
min = 5
string=""
size=0
sys.stdout = open('resultat.txt', 'w')
start_time = time.time()

def ecrire(result):
   print(result)

def forceur(string,size):
    # Si la taille du test ne dépasse pas le max
    if size <= max:
        for i in alphabet:
            testString = string+i
            testSize = size+1
            forceur(testString,testSize)

            # Si la taille du test n'est pas en dessous du minimum
            if min <= testSize:
                # On hash la chaine de test
                current_hash = hashlib.md5(testString.encode('utf')).hexdigest()
                # On la compare avec les mots de passes dans le tableau
                if current_hash in passwords.values():
                    # Si ça correspond on l'écrit avec le temps d'exécution
                    ecrire("Le mot de passe de \"{}\" est \"{}\"".format(','.join(i for i in passwords if passwords[i] == current_hash), testString))
                    ecrire("Temps pour le trouver : {} seconds".format(time.time() - start_time))
                    ecrire("------------------------")

# On ouvre le fichier shadow
with open('shadow', 'r') as f:
    lines = f.readlines()

# Création du tableau des résultats
passwords = {}

# Pour chaques lignes
for line in lines:
    try:
        # On sépare le login du mot de passe
        login, user_hash = re.findall('^([^:]+):\$1\$([^:]+):.+', line)[0]
    except IndexError:
        # si pas de hash on passe a la ligne suivante
        continue
    else:
        # Sinon on ajoute au tableau
        passwords[login] = user_hash

ecrire(str(len(passwords))+' Mot de passe chiffré sous MD5 trouvé, déchiffrage en cours entre '+str(min+1)+' et '+str(max+1)+' caractères...\n')
forceur(string,size)
