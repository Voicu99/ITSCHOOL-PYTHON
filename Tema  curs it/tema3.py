def adunare(a, b):
    """Funcție pentru adunarea a două elemente"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return str(a) + str(b)

def scadere(a, b):
    """Funcție pentru scăderea a două numere"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    return "Scăderea se aplică doar numerelor!"

def inmultire(a, b):
    """Funcție pentru înmulțirea a două elemente"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a * b
    
    # Repetă primul element de atâtea ori cât indică al doilea
    if isinstance(b, int):
        return str(a) * b
    
    return "Înmulțirea se aplică doar numerelor sau repetării unui text!"

def impartire(a, b):
    """Funcție pentru împărțirea a două numere"""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if b == 0:
            return "Eroare: Împărțire la zero!"
        return a / b
    
    return "Împărțirea se aplică doar numerelor!"

def calculator():
    """Funcția principală pentru calculator"""
    print("Calculator Flexibil Python")
    print("Exemple de operații:")
    print("- Numere: '10 + 5', '20 * 3'")
    print("- Text: 'masina + 5', 'test * 3'")
    print("- Pentru ieșire, tastați 'exit'")

    while True:
        # Citește input-ul utilizatorului
        operatie = input("Introduceți operația: ")

        # Verifică comanda de ieșire
        if operatie.lower() == 'exit':
            print("Închidere calculator...")
            break

        try:
            # Desparte input-ul în componente
            componente = operatie.split()

            # Verifică dacă input-ul are 3 componente
            if len(componente) != 3:
                print("Format invalid! Folosiți formatul: 'x operator y'")
                continue

            # Încearcă să convertească numerele, dacă sunt numerice
            try:
                a = float(componente[0]) if '.' in componente[0] else int(componente[0]) if componente[0].isdigit() else componente[0]
            except ValueError:
                a = componente[0]

            operator = componente[1]

            try:
                b = float(componente[2]) if '.' in componente[2] else int(componente[2]) if componente[2].isdigit() else componente[2]
            except ValueError:
                b = componente[2]

            # Execută operația corespunzătoare
            if operator == '+':
                rezultat = adunare(a, b)
            elif operator == '-':
                rezultat = scadere(a, b)
            elif operator == '*':
                rezultat = inmultire(a, b)
            elif operator == '/':
                rezultat = impartire(a, b)
            else:
                print("Operator necunoscut! Folosiți +, -, *, /")
                continue

            # Afișează rezultatul
            print(f"Rezultat: {rezultat}")

        except Exception as e:
            print(f"A apărut o eroare: {e}")

# Pornește calculatorul
if __name__ == "__main__":
    calculator()