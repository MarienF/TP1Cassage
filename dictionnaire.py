import re, hashlib, sys, time

sys.stdout = open('resultat.txt', 'w')
start_time = time.time()

def ecrire(result):
    print(result)

with open('shadow', 'r') as f:
   lines = f.readlines()

passwords = {}
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

# On ouvre le dictionnaire en lecture
with open('dico_mini_fr', 'r') as f:
   lines = f.readlines()

# Pour chaque lignes on test
for line in lines:
    # On enleve les caractères invisibles
    testString = line.strip()
    # On hash le test
    current_hash = hashlib.md5(testString.encode('utf')).hexdigest()
    # On la compare avec les mots de passes dans le tableau
    if current_hash in passwords.values():
        # Si ça correspond on l'écrit avec le temps d'exécution
        ecrire("Le mot de passe de \"{}\" est \"{}\"".format(','.join(i for i in passwords if passwords[i] == current_hash), testString))
        ecrire("Temps pour le trouver : {} seconds".format(time.time() - start_time))
        ecrire("------------------------")