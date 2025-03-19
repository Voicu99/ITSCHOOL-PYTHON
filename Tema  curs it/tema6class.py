class Elev:
    def __init__(self, nume, prenume, nota_romana, nota_matematica, nota_engleza):
        self.nume = nume
        self.prenume = prenume
        self.nota_romana = nota_romana
        self.nota_matematica = nota_matematica
        self.nota_engleza = nota_engleza
        self.calculeaza_media()
    
    def calculeaza_media(self):
        self.media = round((self.nota_romana + self.nota_matematica + self.nota_engleza) / 3, 2)
    
    def afisare_info(self):
        return f"Nume: {self.nume}, Prenume: {self.prenume}, Romana: {self.nota_romana}, Matematica: {self.nota_matematica}, Engleza: {self.nota_engleza}, Media: {self.media}"

def adauga_elev(elevi):
    print("\n--- Adăugare elev nou ---")
    nume = input("Introduceți numele: ")
    prenume = input("Introduceți prenumele: ")
    
    while True:
        try:
            nota_romana = float(input("Introduceți nota la Română (1-10): "))
            if 1 <= nota_romana <= 10:
                break
            else:
                print("Nota trebuie să fie între 1 și 10!")
        except ValueError:
            print("Vă rugăm introduceți un număr valid!")
    
    while True:
        try:
            nota_matematica = float(input("Introduceți nota la Matematică (1-10): "))
            if 1 <= nota_matematica <= 10:
                break
            else:
                print("Nota trebuie să fie între 1 și 10!")
        except ValueError:
            print("Vă rugăm introduceți un număr valid!")
    
    while True:
        try:
            nota_engleza = float(input("Introduceți nota la Engleză (1-10): "))
            if 1 <= nota_engleza <= 10:
                break
            else:
                print("Nota trebuie să fie între 1 și 10!")
        except ValueError:
            print("Vă rugăm introduceți un număr valid!")
    
    elev_nou = Elev(nume, prenume, nota_romana, nota_matematica, nota_engleza)
    elevi.append(elev_nou)
    print(f"Elevul {nume} {prenume} a fost adăugat cu succes!")

def afisare_elevi(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
    
    print("\n--- Lista elevilor ---")
    for i, elev in enumerate(elevi, 1):
        print(f"{i}. {elev.afisare_info()}")

def modifica_elev(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
        
    afisare_elevi(elevi)
    try:
        index = int(input("\nIntroduceți numărul elevului pe care doriți să-l modificați: ")) - 1
        
        if index < 0 or index >= len(elevi):
            print("Număr invalid!")
            return
            
        elev = elevi[index]
        print(f"\nModificare date pentru elevul: {elev.nume} {elev.prenume}")
        
        nume_nou = input(f"Nume nou (enter pentru a păstra '{elev.nume}'): ")
        if nume_nou:
            elev.nume = nume_nou
            
        prenume_nou = input(f"Prenume nou (enter pentru a păstra '{elev.prenume}'): ")
        if prenume_nou:
            elev.prenume = prenume_nou
        
        nota_romana_noua = input(f"Nota nouă la Română (enter pentru a păstra '{elev. nota_romana}'): ")
        if nota_romana_noua:
            try:
                nota = float(nota_romana_noua)
                if 1 <= nota <= 10:
                    elev.nota_romana = nota
                else:
                    print("Nota trebuie să fie între 1 și 10! Nota la Română nu a fost modificată.")
            except ValueError:
                print("Valoare invalidă! Nota la Română nu a fost modificată.")
        
        nota_matematica_noua = input(f"Nota nouă la Matematică (enter pentru a păstra '{elev.nota_matematica}'): ")
        if nota_matematica_noua:
            try:
                nota = float(nota_matematica_noua)
                if 1 <= nota <= 10:
                    elev.nota_matematica = nota
                else:
                    print("Nota trebuie să fie între 1 și 10! Nota la Matematică nu a fost modificată.")
            except ValueError:
                print("Valoare invalidă! Nota la Matematică nu a fost modificată.")
        
        nota_engleza_noua = input(f"Nota nouă la Engleză (enter pentru a păstra '{elev.nota_engleza}'): ")
        if nota_engleza_noua:
            try:
                nota = float(nota_engleza_noua)
                if 1 <= nota <= 10:
                    elev.nota_engleza = nota
                else:
                    print("Nota trebuie să fie între 1 și 10! Nota la Engleză nu a fost modificată.")
            except ValueError:
                print("Valoare invalidă! Nota la Engleză nu a fost modificată.")
        
        elev.calculeaza_media()
        print("Datele elevului au fost actualizate cu succes!")
        
    except ValueError:
        print("Vă rugăm introduceți un număr valid!")

def sterge_elev(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
        
    afisare_elevi(elevi)
    try:
        index = int(input("\nIntroduceți numărul elevului pe care doriți să-l ștergeți: ")) - 1
        
        if index < 0 or index >= len(elevi):
            print("Număr invalid!")
            return
            
        elev = elevi[index]
        confirmare = input(f"Sigur doriți să ștergeți elevul {elev.nume} {elev.prenume}? (da/nu): ")
        
        if confirmare.lower() == "da":
            elevi.pop(index)
            print("Elevul a fost șters cu succes!")
        else:
            print("Operațiunea de ștergere a fost anulată.")
    
    except ValueError:
        print("Vă rugăm introduceți un număr valid!")

def cauta_elev(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
    
    nume = input("\nIntroduceți numele elevului: ")
    prenume = input("Introduceți prenumele elevului: ")
    
    rezultate = []
    for elev in elevi:
        if elev.nume.lower() == nume.lower() and elev.prenume.lower() == prenume.lower():
            rezultate.append(elev)
    
    if rezultate:
        print("\n--- Rezultate căutare ---")
        for i, elev in enumerate(rezultate, 1):
            print(f"{i}. {elev.afisare_info()}")
    else:
        print(f"\nNu a fost găsit niciun elev cu numele {nume} {prenume}!")

def afisare_dupa_medie(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
        
    elevi_sortati = sorted(elevi, key=lambda elev: elev.media, reverse=True)
    
    print("\n--- Elevi ordonați după medie (descrescător) ---")
    for i, elev in enumerate(elevi_sortati, 1):
        print(f"{i}. {elev.afisare_info()}")

def afisare_elevi_medie_peste_8(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
        
    elevi_filtrati = [elev for elev in elevi if elev.media > 8]
    
    if elevi_filtrati:
        print("\n--- Elevi cu media peste 8 ---")
        for i, elev in enumerate(elevi_filtrati, 1):
            print(f"{i}. {elev.afisare_info()}")
    else:
        print("\nNu există elevi cu media peste 8!")

def afisare_alfabetic(elevi):
    if not elevi:
        print("\nNu există elevi înregistrați!")
        return
        
    elevi_sortati = sorted(elevi, key=lambda elev: elev.nume)
    
    print("\n--- Elevi ordonați alfabetic după nume ---")
    for i, elev in enumerate(elevi_sortati, 1):
        print(f"{i}. {elev.afisare_info()}")

def meniu_principal():
    elevi = []
    
    while True:
        print("\n--- EVIDENȚA ELEVILOR ---")
        print("1. Adăugare elev")
        print("2. Afișarea elevilor existenți")
        print("3. Modificare informații elev existent")
        print("4. Ștergere elev")
        print("5. Căutare elev după nume și prenume")
        print("6. Afișare elevi în ordinea mediei")
        print("7. Afișare elevi cu media peste 8")
        print("8. Afișare elevi în ordine alfabetică (după Nume)")
        print("9. Ieșire din program")
        
        optiune = input("\nAlegeți o opțiune (1-9): ")
        
        if optiune == "1":
            adauga_elev(elevi)
        elif optiune == "2":
            afisare_elevi(elevi)
        elif optiune == "3":
            modifica_elev(elevi)
        elif optiune == "4":
            sterge_elev(elevi)
        elif optiune == "5":
            cauta_elev(elevi)
        elif optiune == "6":
            afisare_dupa_medie(elevi)
        elif optiune == "7":
            afisare_elevi_medie_peste_8(elevi)
        elif optiune == "8":
            afisare_alfabetic(elevi)
        elif optiune == "9":
            print("\nLa revedere!")
            break
        else:
            print("\nOpțiune invalidă! Vă rugăm alegeți o opțiune între 1 și 9.")

if __name__ == "__main__":
    meniu_principal()