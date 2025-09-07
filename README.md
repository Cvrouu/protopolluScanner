Scanner Prototype Pollution

Ce projet est un petit script Python pour tester la vulnérabilité Prototype Pollution sur des applications web. L’idée, c’est de pouvoir scanner une URL ou plusieurs URLs avec des payloads JSON et voir si l’application est vulnérable.

Prérequis

Python 3.x

Modules Python : requests, colorama, argparse

Pour installer les modules :

pip install requests colorama

Utilisation
Scanner une seule URL
python scanner.py -u https://exemple.com

Scanner plusieurs URLs via un fichier

Créez un fichier texte (urls.txt) avec une URL par ligne.

python scanner.py -f urls.txt

Utiliser un fichier de payloads personnalisé

Par défaut, le script utilise payloads.json.

python scanner.py -u https://exemple.com -p mes_payloads.json

Fonctionnalités

Scanner une ou plusieurs URLs

Vérifier si elles sont vulnérables à Prototype Pollution avec les payloads fournis

Prévu dans une future version : test de gadgets personnalisés pour certaines applications

Limitations

Les gadgets personnalisés ne sont pas encore gérés.

Les résultats ne sont pas sauvegardés automatiquement (pas encore implémenté).

Exemple de sortie
Voici l'URL à tester : ['https://exemple.com']
Et ça c'est les payloads je suppose : ['payload1', 'payload2']

Contribution

C’est un projet perso donc pour l’instant contributions ouvertes juste pour test/feedback.

Fork le repo si tu veux jouer avec

Tu peux proposer des améliorations via Pull Request

Licence

Projet perso, pas de licence particulière pour le moment.
