import random

def main():
    print("Program care rezolvă exercițiile 21-31")
    print("=" * 50)
    
    # Exercițiul 21: Numărarea aparițiilor unei litere într-un cuvânt
    print("\n21) Numărarea aparițiilor unei litere într-un cuvânt:")
    cuvant = input("Introduceți un cuvânt: ")
    litera = input("Introduceți o literă: ")
    
    # Folosind for
    count_for = 0
    for char in cuvant:
        if char.lower() == litera.lower():
            count_for += 1
            
    # Folosind while
    count_while = 0
    i = 0
    while i < len(cuvant):
        if cuvant[i].lower() == litera.lower():
            count_while += 1
        i += 1
        
    print(f"Folosind for: Litera '{litera}' apare de {count_for} ori în cuvântul '{cuvant}'")
    print(f"Folosind while: Litera '{litera}' apare de {count_while} ori în cuvântul '{cuvant}'")
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 22: Afișarea numerelor pare până la 100
    print("\n22) Numerele pare până la 100:")
    for num in range(0, 101, 2):
        print(num, end=" ")
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 23: Afișarea numerelor impare până la 50
    print("\n23) Numerele impare până la 50:")
    for num in range(1, 51, 2):
        print(num, end=" ")
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 24: Afișarea puterilor lui 2 mai mici decât 150
    print("\n24) Puterile lui 2 mai mici decât 150:")
    power = 1
    while power < 150:
        print(power, end=" ")
        power *= 2
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 25: Afișarea puterilor lui 3 cuprinse între 200 și 300
    print("\n25) Puterile lui 3 cuprinse între 200 și 300:")
    power = 1
    while power <= 300:
        power *= 3
        if 200 <= power <= 300:
            print(power, end=" ")
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 26: Calcularea sumei de la 1 la un număr dat
    print("\n26) Calcularea sumei de la 1 la n:")
    n = int(input("Introduceți un număr pentru calculul sumei: "))
    
    # Folosind for
    suma_for = 0
    for i in range(1, n + 1):
        suma_for += i
        
    # Folosind while
    suma_while = 0
    i = 1
    while i <= n:
        suma_while += i
        i += 1
        
    print(f"Suma numerelor de la 1 la {n} folosind for: {suma_for}")
    print(f"Suma numerelor de la 1 la {n} folosind while: {suma_while}")
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 27: Calcularea produsului de la 1 la un număr dat
    print("\n27) Calcularea produsului de la 1 la n:")
    n = int(input("Introduceți un număr pentru calculul produsului: "))
    
    # Folosind for
    produs_for = 1
    for i in range(1, n + 1):
        produs_for *= i
        
    # Folosind while
    produs_while = 1
    i = 1
    while i <= n:
        produs_while *= i
        i += 1
        
    print(f"Produsul numerelor de la 1 la {n} folosind for: {produs_for}")
    print(f"Produsul numerelor de la 1 la {n} folosind while: {produs_while}")
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 28: Numărătoare inversă
    print("\n28) Numărătoare inversă:")
    n = int(input("Introduceți un număr pentru numărătoarea inversă: "))
    print(f"Numărătoare inversă de la {n} la 0:")
    for i in range(n, -1, -1):
        print(i, end=" ")
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 29: Afișarea divizorilor unui număr
    print("\n29) Afișarea divizorilor unui număr:")
    n = int(input("Introduceți un număr pentru a afișa divizorii: "))
    print(f"Divizorii numărului {n} sunt:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 30: Afișarea pe rând a cifrelor unui număr
    print("\n30) Afișarea cifrelor unui număr:")
    n = int(input("Introduceți un număr pentru a afișa cifrele: "))
    print(f"Cifrele numărului {n} sunt:")
    
    # Folosind for și string
    for cifra in str(n):
        print(cifra, end=" ")
    print()
    
    # Folosind while (afișează cifrele în ordine inversă)
    print("Cifrele folosind while (în ordine inversă):")
    temp = n
    while temp > 0:
        cifra = temp % 10
        print(cifra, end=" ")
        temp //= 10
    print()
    
    input("\nApăsați Enter pentru a continua...")
    
    # Exercițiul 31: Joc de ghicit numărul
    print("\n31) Joc de ghicit numărul:")
    print("Am generat un număr între 1 și 100. Încearcă să-l ghicești!")
    
    # Generarea numărului aleator între 1 și 100
    numar_secret = random.randint(1, 100)
    incercari = 0
    ghicit = False
    
    while not ghicit:
        try:
            incercari += 1
            ghicire = int(input("Introduceți un număr: "))
            
            if ghicire < numar_secret:
                print("Numărul secret este mai mare. Încearcă din nou!")
            elif ghicire > numar_secret:
                print("Numărul secret este mai mic. Încearcă din nou!")
            else:
                ghicit = True
                print(f"Felicitări! Ai ghicit numărul {numar_secret} din {incercari} încercări!")
        except ValueError:
            print("Te rog să introduci un număr valid!")
    
    print("\nProgram finalizat! Toate exercițiile au fost rezolvate.")
if __name__ == "__main__":
    main()