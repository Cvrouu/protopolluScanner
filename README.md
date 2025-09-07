# Prototype Pollution Scanner

This project is a Python script for testing **Prototype Pollution** vulnerabilities in web applications.  
It scans one or more URLs by dynamically injecting gadgets into JSON payloads to detect potential vulnerabilities.

---

## 🛠️ Usage

### Scanning a single URL

```bash
python scanner.py -u https://exemple.com
```

### Scan multiple URLs via a file

Create a text file (`urls.txt`) with one URL per line.

```bash
python scanner.py -f urls.txt
```

### Use a custom gadget file

Create a text file (`gadgets.txt`) with one gadget per line.

```bash
python scanner.py -u https://exemple.com -g gadgets.txt
```

---

## ⚙️ Features

- Scan one or more URLs
- Dynamic generation of payloads from known gadgets and pollution paths
- Automatic detection of prototype pollution
- Detailed results for each URL and gadget tested

---

## ⚠️ Limitations

- Results are not yet saved automatically
- Detection relies on the presence of the gadget in the response (to be adapted according to the target application)
- The script does not automatically guess the gadgets used by the application

---

## 📝 Example output

```
Here is the list of URLs to test: [‘https://exemple.com’]
Here are your gadgets: [‘isAdmin’, ‘toString’, ...]
Gadget ‘isAdmin’ via ‘__proto__’ seems to have an effect on https://exemple.com!
Gadget ‘toString’ via ‘constructor.prototype’ has no visible effect on https://exemple.com.
[Results(url=‘https://exemple.com’, vuln=True, gadgets=[‘isAdmin’])]
```

---

## 🤝 Contribution

- Contributions, tests, and feedback are welcome!
- Fork the repo and suggest your improvements via Pull Request.

---

## 📄 License

Personal project, no specific license