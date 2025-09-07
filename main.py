import requests
import colorama
import argparse

parser = argparse.ArgumentParser(description="Scanner Prototype Pollution")

# Une seule URL
parser.add_argument("-u", "--url", type=str, help="URL unique à scanner")

# Plusieurs URLs via un fichier
parser.add_argument("-f", "--file", type=str, help="Fichier contenant les URLs")

# Payloads proto ou construc
parser.add_argument(
    "-p",
    "--payloads",
    type=str,
    default="payloads.json",
    help="Fichier JSON des payloads",
)

# Je voulais ajouter des gadgets a injecter mais le soucis c'est que chaque gadget va etre different en fonction de l'application donc c'est presque impossible a mettre en place

# Dans la version 2 il y aura des gadgets perso et de l'injection

args = parser.parse_args()

# Lecture des arguments URL

if args.url:
    urls = [arg.url]
    print("Voici l'URL a tester" + urls)

elif args.file:
    with open(arg.file, "r") as urlsfile:
        urls = [line.strip() for line in urlsfile.readlines()]
    print("Voici la liste d'URL a tester :" + urls)

if not args.url and not args.file:  # On sait jamais X)
    parser.print_help()
    exit()

# Lecture des gadgets et proto

if args.payload:
    with open(args.payload, "r") as payloadsfile:
        payloads = [line.strip() for line in payloadsfile.readlines()]
    print("Et ca c'est les payloads je suppose :" + payloads)

# if args.gadgets :
# 	with open(args.gadgets, "r") as gadgetsfile:
# 	       	gadgets = [line.strip() for line in gadgetsfile.readlines()]
# 	print("Et la c'est tes gadgets" + gadgets)

if not args.payloads:  # and not args.gadgets: La aussi on sait jamais hein ^^
    parser.print_help()
    exit()

# Les choses commencent ici !


class resultats:  # Creer un objet pour les URL
    def __init__(self, url):
        self.url = url
        self.vuln = False
        self.gadgets = []


all_results = []  # Creer une liste pour que chaque resultat d'objet qui va etre creer

for url in urls:

    res = Resultats(url)  # Creer un objet pour CHAQUE URL

    for payload in payloads:
        pollutedrequest = request.post(
            url, json=payload
        )  # Envoyer une requete post polluee pour CHAQUE URL

        if "polluted" in pollutedrequest.text:
            res.vuln = True
            print("Ca pue ici" + pollutedrequest.text)
        else:
            print("C'est pas pollue lol")

    all_results.append(res)  # Ajouter le resultat a la liste au dessus
