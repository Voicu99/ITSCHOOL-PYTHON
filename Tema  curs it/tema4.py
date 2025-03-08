def exercitiul1():
    print("\n--- Exercițiul 1 ---")
    lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    nume_ionut = lista[1][1]
    print(f"Numele extras este: {nume_ionut}")

def exercitiul2():
    print("\n--- Exercițiul 2 ---")
    lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    litera_r = lista[1][2][2]
    print(f"Litera extrasă este: {litera_r}")

def exercitiul3():
    print("\n--- Exercițiul 3 ---")
    lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    numere_float = lista[2]
    print("Numerele de tip float din listă sunt:", numere_float)

def exercitiul4():
    print("\n--- Exercițiul 4 ---")
    lista = [[10, 5, 29], ["Marian", "Ionut", "Marcel"], [10.2, 7.5, 3.4]]
    nume = input("Introduceți un nume pentru a verifica dacă se află în listă: ")
    if nume in lista[1]:
        print(f"Numele '{nume}' se află în listă.")
    else:
        print(f"Numele '{nume}' nu se află în listă.")

def exercitiul5():
    print("\n--- Exercițiul 5 ---")
    lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    numere_pare = [numar for numar in lista if numar % 2 == 0]
    print("Numerele pare din listă sunt:", numere_pare)

def exercitiul6():
    print("\n--- Exercițiul 6 ---")
    lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    minim = min(lista)
    maxim = max(lista)
    print(f"Cel mai mic număr din listă este: {minim}")
    print(f"Cel mai mare număr din listă este: {maxim}")

def exercitiul7():
    print("\n--- Exercițiul 7 ---")
    lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def afiseaza_divizibile(lista, numar):
        divizibile = [x for x in lista if x % numar == 0]
        if divizibile:
            print(f"Numerele din listă divizibile cu {numar} sunt:", divizibile)
        else:
            print(f"Nu există numere în listă divizibile cu {numar}")
    
    numar = int(input("Introduceți un număr pentru a verifica divizibilitatea: "))
    afiseaza_divizibile(lista, numar)

def exercitiul8():
    print("\n--- Exercițiul 8 ---")
    lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def suma_impare(lista):
        suma = sum([numar for numar in lista if numar % 2 != 0])
        return suma
    
    print(f"Suma numerelor impare din listă este: {suma_impare(lista)}")

def exercitiul9():
    print("\n--- Exercițiul 9 ---")
    lista = [5, 17, 15, 12, 19, 31, 27, 55, 102, 33, 97]
    
    def gaseste_index(lista, numar):
        if numar in lista:
            return lista.index(numar)
        else:
            return "Not Found"
    
    numar = int(input("Introduceți un număr pentru a căuta indexul său în listă: "))
    rezultat = gaseste_index(lista, numar)
    print(f"Indexul numărului {numar} în listă este: {rezultat}")

def main():
    print("Program pentru rezolvarea exercițiilor cu liste în Python")
    
    exercitiul1()
    exercitiul2()
    exercitiul3()
    exercitiul4()
    exercitiul5()
    exercitiul6()
    exercitiul7()
    exercitiul8()
    exercitiul9()

if __name__ == "__main__":
    main()