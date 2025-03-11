# Program pentru evidența elevilor din școală
# Acest program gestionează o listă de elevi și permite diverse operații asupra acesteia

# Vom folosi un dicționar pentru a reprezenta fiecare elev
# și o listă pentru a stoca toți elevii

def calculeaza_medie(note):
    # Funcție care calculează media unui elev
    # Primește un dicționar cu notele și returnează media aritmetică
    return (note["romana"] + note["matematica"] + note["engleza"]) / 3  # Calculează media aritmetică a celor trei note

def adauga_elev(lista_elevi):
    # Funcție pentru adăugarea unui nou elev în lista
    # Primește lista de elevi și o modifică adăugând un nou element
    
    print("\n--- Adăugare elev nou ---")  # Afișează un titlu pentru operația curentă
    nume = input("Introduceți numele: ")  # Solicită și salvează numele elevului
    prenume = input("Introduceți prenumele: ")  # Solicită și salvează prenumele elevului
    
    while True:  # Începe o buclă infinită pentru validarea notei la română
        try:  # Începe un bloc try pentru a gestiona posibilele erori
            nota_romana = float(input("Introduceți nota la Romana (0-10): "))  # Solicită nota la română și o convertește la float
            if 0 <= nota_romana <= 10:  # Verifică dacă nota este în intervalul valid
                break  # Dacă nota este validă, iese din buclă
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10!")  # Afișează un mesaj de eroare
        except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
            print("Introduceți o valoare numerică validă!")  # Afișează un mesaj de eroare
    
    while True:  # Începe o buclă infinită pentru validarea notei la matematică
        try:  # Începe un bloc try pentru a gestiona posibilele erori
            nota_matematica = float(input("Introduceți nota la Matematica (0-10): "))  # Solicită nota la matematică și o convertește la float
            if 0 <= nota_matematica <= 10:  # Verifică dacă nota este în intervalul valid
                break  # Dacă nota este validă, iese din buclă
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10!")  # Afișează un mesaj de eroare
        except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
            print("Introduceți o valoare numerică validă!")  # Afișează un mesaj de eroare
    
    while True:  # Începe o buclă infinită pentru validarea notei la engleză
        try:  # Începe un bloc try pentru a gestiona posibilele erori
            nota_engleza = float(input("Introduceți nota la Engleza (0-10): "))  # Solicită nota la engleză și o convertește la float
            if 0 <= nota_engleza <= 10:  # Verifică dacă nota este în intervalul valid
                break  # Dacă nota este validă, iese din buclă
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10!")  # Afișează un mesaj de eroare
        except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
            print("Introduceți o valoare numerică validă!")  # Afișează un mesaj de eroare
    
    elev_nou = {  # Creează un dicționar pentru noul elev
        "nume": nume,  # Salvează numele în dicționar
        "prenume": prenume,  # Salvează prenumele în dicționar
        "romana": nota_romana,  # Salvează nota la română în dicționar
        "matematica": nota_matematica,  # Salvează nota la matematică în dicționar
        "engleza": nota_engleza  # Salvează nota la engleză în dicționar
    }
    
    # Calculăm și adăugăm media
    elev_nou["medie"] = calculeaza_medie(elev_nou)  # Calculează media și o adaugă în dicționar
    
    lista_elevi.append(elev_nou)  # Adaugă noul elev în lista de elevi
    print(f"Elevul {nume} {prenume} a fost adăugat cu succes!")  # Afișează un mesaj de confirmare

def afiseaza_elevi(lista_elevi):
    # Funcție pentru afișarea tuturor elevilor din listă
    # Primește lista de elevi și afișează informațiile despre fiecare
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    print("\n--- Lista elevilor ---")  # Afișează un titlu pentru lista de elevi
    for i, elev in enumerate(lista_elevi, 1):  # Parcurge lista de elevi cu indici începând de la 1
        print(f"{i}. {elev['nume']} {elev['prenume']}: Romana: {elev['romana']}, "  # Afișează numărul și numele elevului
              f"Matematica: {elev['matematica']}, Engleza: {elev['engleza']}, "  # Afișează notele la matematică și engleză
              f"Media: {elev['medie']:.2f}")  # Afișează media cu două zecimale

def modifica_elev(lista_elevi):
    # Funcție pentru modificarea informațiilor unui elev existent
    # Primește lista de elevi și permite modificarea unui element selectat
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    afiseaza_elevi(lista_elevi)  # Afișează lista de elevi pentru a permite selecția
    while True:  # Începe o buclă infinită pentru validarea indexului elevului
        try:  # Începe un bloc try pentru a gestiona posibilele erori
            index = int(input("\nIntroduceți numărul elevului pe care doriți să îl modificați: ")) - 1  # Solicită indexul elevului și îl ajustează (scade 1 pentru că afișarea începe de la 1)
            if 0 <= index < len(lista_elevi):  # Verifică dacă indexul este valid
                break  # Dacă indexul este valid, iese din buclă
            else:  # Dacă indexul nu este valid
                print("Numărul introdus nu este valid!")  # Afișează un mesaj de eroare
        except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la int
            print("Introduceți un număr valid!")  # Afișează un mesaj de eroare
    
    elev = lista_elevi[index]  # Obține referința la elevul selectat
    print(f"\nModificare date pentru elevul: {elev['nume']} {elev['prenume']}")  # Afișează un mesaj cu elevul selectat
    
    nume_nou = input(f"Nume nou (sau Enter pentru a păstra '{elev['nume']}'): ")  # Solicită noul nume sau permite păstrarea celui existent
    if nume_nou:  # Verifică dacă s-a introdus un nume nou
        elev['nume'] = nume_nou  # Actualizează numele elevului
    
    prenume_nou = input(f"Prenume nou (sau Enter pentru a păstra '{elev['prenume']}'): ")  # Solicită noul prenume sau permite păstrarea celui existent
    if prenume_nou:  # Verifică dacă s-a introdus un prenume nou
        elev['prenume'] = prenume_nou  # Actualizează prenumele elevului
    
    try:  # Începe un bloc try pentru a gestiona posibilele erori
        nota_romana_str = input(f"Nota nouă la Romana (sau Enter pentru a păstra '{elev['romana']}'): ")  # Solicită noua notă la română sau permite păstrarea celei existente
        if nota_romana_str:  # Verifică dacă s-a introdus o notă nouă
            nota_romana = float(nota_romana_str)  # Convertește nota la float
            if 0 <= nota_romana <= 10:  # Verifică dacă nota este în intervalul valid
                elev['romana'] = nota_romana  # Actualizează nota la română
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
        print("Valoare invalidă! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    
    try:  # Începe un bloc try pentru a gestiona posibilele erori
        nota_matematica_str = input(f"Nota nouă la Matematica (sau Enter pentru a păstra '{elev['matematica']}'): ")  # Solicită noua notă la matematică sau permite păstrarea celei existente
        if nota_matematica_str:  # Verifică dacă s-a introdus o notă nouă
            nota_matematica = float(nota_matematica_str)  # Convertește nota la float
            if 0 <= nota_matematica <= 10:  # Verifică dacă nota este în intervalul valid
                elev['matematica'] = nota_matematica  # Actualizează nota la matematică
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
        print("Valoare invalidă! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    
    try:  # Începe un bloc try pentru a gestiona posibilele erori
        nota_engleza_str = input(f"Nota nouă la Engleza (sau Enter pentru a păstra '{elev['engleza']}'): ")  # Solicită noua notă la engleză sau permite păstrarea celei existente
        if nota_engleza_str:  # Verifică dacă s-a introdus o notă nouă
            nota_engleza = float(nota_engleza_str)  # Convertește nota la float
            if 0 <= nota_engleza <= 10:  # Verifică dacă nota este în intervalul valid
                elev['engleza'] = nota_engleza  # Actualizează nota la engleză
            else:  # Dacă nota nu este în intervalul valid
                print("Nota trebuie să fie între 0 și 10! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la float
        print("Valoare invalidă! Nota nu a fost modificată.")  # Afișează un mesaj de eroare
    
    # Recalculează media după modificări
    elev['medie'] = calculeaza_medie(elev)  # Recalculează și actualizează media elevului
    print("Datele elevului au fost actualizate cu succes!")  # Afișează un mesaj de confirmare

def sterge_elev(lista_elevi):
    # Funcție pentru ștergerea unui elev din listă
    # Primește lista de elevi și elimină un element selectat
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    afiseaza_elevi(lista_elevi)  # Afișează lista de elevi pentru a permite selecția
    while True:  # Începe o buclă infinită pentru validarea indexului elevului
        try:  # Începe un bloc try pentru a gestiona posibilele erori
            index = int(input("\nIntroduceți numărul elevului pe care doriți să îl ștergeți: ")) - 1  # Solicită indexul elevului și îl ajustează (scade 1 pentru că afișarea începe de la 1)
            if 0 <= index < len(lista_elevi):  # Verifică dacă indexul este valid
                break  # Dacă indexul este valid, iese din buclă
            else:  # Dacă indexul nu este valid
                print("Numărul introdus nu este valid!")  # Afișează un mesaj de eroare
        except ValueError:  # Prinde eroarea generată când input-ul nu poate fi convertit la int
            print("Introduceți un număr valid!")  # Afișează un mesaj de eroare
    
    elev = lista_elevi[index]  # Obține referința la elevul selectat
    confirmare = input(f"Sigur doriți să ștergeți elevul {elev['nume']} {elev['prenume']}? (da/nu): ")  # Solicită confirmarea ștergerii
    
    if confirmare.lower() == "da":  # Verifică dacă utilizatorul a confirmat ștergerea
        lista_elevi.pop(index)  # Elimină elevul din listă
        print("Elevul a fost șters cu succes!")  # Afișează un mesaj de confirmare
    else:  # Dacă utilizatorul nu a confirmat ștergerea
        print("Operațiunea de ștergere a fost anulată.")  # Afișează un mesaj de anulare

def cauta_elev(lista_elevi):
    # Funcție pentru căutarea unui elev după nume și prenume
    # Primește lista de elevi și afișează informații despre elevii găsiți
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    print("\n--- Căutare elev ---")  # Afișează un titlu pentru operația curentă
    nume = input("Introduceți numele: ")  # Solicită numele pentru căutare
    prenume = input("Introduceți prenumele: ")  # Solicită prenumele pentru căutare
    
    gasit = False  # Inițializează variabila care indică dacă s-a găsit vreun elev
    for elev in lista_elevi:  # Parcurge lista de elevi
        if elev['nume'].lower() == nume.lower() and elev['prenume'].lower() == prenume.lower():  # Verifică dacă numele și prenumele corespund (ignorând diferențele de capitalizare)
            print(f"\nElev găsit: {elev['nume']} {elev['prenume']}: "  # Afișează numele elevului găsit
                  f"Romana: {elev['romana']}, Matematica: {elev['matematica']}, "  # Afișează notele la română și matematică
                  f"Engleza: {elev['engleza']}, Media: {elev['medie']:.2f}")  # Afișează nota la engleză și media
            gasit = True  # Actualizează variabila pentru a indica că s-a găsit un elev
    
    if not gasit:  # Verifică dacă nu s-a găsit niciun elev
        print(f"Nu s-a găsit niciun elev cu numele {nume} {prenume}.")  # Afișează un mesaj de notificare

def afisare_dupa_medie(lista_elevi):
    # Funcție pentru afișarea elevilor în ordinea descrescătoare a mediei
    # Primește lista de elevi și afișează o versiune sortată a acesteia
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    print("\n--- Elevii în ordinea mediei (descrescător) ---")  # Afișează un titlu pentru lista sortată
    elevi_sortati = sorted(lista_elevi, key=lambda elev: elev['medie'], reverse=True)  # Sortează lista de elevi după medie în ordine descrescătoare
    
    for i, elev in enumerate(elevi_sortati, 1):  # Parcurge lista sortată cu indici începând de la 1
        print(f"{i}. {elev['nume']} {elev['prenume']}: "  # Afișează numărul și numele elevului
              f"Romana: {elev['romana']}, Matematica: {elev['matematica']}, "  # Afișează notele la română și matematică
              f"Engleza: {elev['engleza']}, Media: {elev['medie']:.2f}")  # Afișează nota la engleză și media

def afisare_peste_medie(lista_elevi):
    # Funcție pentru afișarea elevilor cu media peste 8
    # Primește lista de elevi și afișează doar pe cei care îndeplinesc condiția
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    print("\n--- Elevii cu media peste 8 ---")  # Afișează un titlu pentru lista filtrată
    elevi_filtrati = [elev for elev in lista_elevi if elev['medie'] > 8]  # Filtrează lista pentru a include doar elevii cu media peste 8
    
    if not elevi_filtrati:  # Verifică dacă lista filtrată este goală
        print("Nu există elevi cu media peste 8.")  # Afișează un mesaj dacă nu există elevi care să îndeplinească condiția
        return  # Încheie funcția
    
    for i, elev in enumerate(elevi_filtrati, 1):  # Parcurge lista filtrată cu indici începând de la 1
        print(f"{i}. {elev['nume']} {elev['prenume']}: "  # Afișează numărul și numele elevului
              f"Romana: {elev['romana']}, Matematica: {elev['matematica']}, "  # Afișează notele la română și matematică
              f"Engleza: {elev['engleza']}, Media: {elev['medie']:.2f}")  # Afișează nota la engleză și media

def afisare_alfabetica(lista_elevi):
    # Funcție pentru afișarea elevilor în ordine alfabetică după nume
    # Primește lista de elevi și afișează o versiune sortată a acesteia
    
    if not lista_elevi:  # Verifică dacă lista de elevi este goală
        print("\nNu există elevi înregistrați!")  # Afișează un mesaj dacă lista este goală
        return  # Încheie funcția
    
    print("\n--- Elevii în ordine alfabetică după nume ---")  # Afișează un titlu pentru lista sortată
    elevi_sortati = sorted(lista_elevi, key=lambda elev: elev['nume'].lower())  # Sortează lista de elevi după nume în ordine alfabetică (ignorând diferențele de capitalizare)
    
    for i, elev in enumerate(elevi_sortati, 1):  # Parcurge lista sortată cu indici începând de la 1
        print(f"{i}. {elev['nume']} {elev['prenume']}: "  # Afișează numărul și numele elevului
              f"Romana: {elev['romana']}, Matematica: {elev['matematica']}, "  # Afișează notele la română și matematică
              f"Engleza: {elev['engleza']}, Media: {elev['medie']:.2f}")  # Afișează nota la engleză și media

def meniu_principal():
    # Funcția principală care afișează meniul și gestionează opțiunile utilizatorului
    
    lista_elevi = []  # Inițializează lista goală de elevi
    
    while True:  # Începe o buclă infinită pentru meniul principal
        print("\n===== EVIDENȚA ELEVILOR =====")  # Afișează titlul meniului
        print("1. Adăugare elev")  # Afișează opțiunea 1
        print("2. Afișarea elevilor existenți")  # Afișează opțiunea 2
        print("3. Modificare informații elev existent")  # Afișează opțiunea 3
        print("4. Ștergere elev")  # Afișează opțiunea 4
        print("5. Căutare elev după nume și prenume")  # Afișează opțiunea 5
        print("6. Afișare elevi în ordinea mediei")  # Afișează opțiunea 6
        print("7. Afișare elevi cu media peste 8")  # Afișează opțiunea 7
        print("8. Afișare elevi în ordine alfabetică (după Nume)")  # Afișează opțiunea 8
        print("9. Ieșire din program")  # Afișează opțiunea 9
        
        optiune = input("\nIntroduceți opțiunea dorită: ")  # Solicită opțiunea utilizatorului
        
        if optiune == '1':  # Verifică dacă opțiunea este 1
            adauga_elev(lista_elevi)  # Apelează funcția pentru adăugarea unui elev
        elif optiune == '2':  # Verifică dacă opțiunea este 2
            afiseaza_elevi(lista_elevi)  # Apelează funcția pentru afișarea elevilor
        elif optiune == '3':  # Verifică dacă opțiunea este 3
            modifica_elev(lista_elevi)  # Apelează funcția pentru modificarea unui elev
        elif optiune == '4':  # Verifică dacă opțiunea este 4
            sterge_elev(lista_elevi)  # Apelează funcția pentru ștergerea unui elev
        elif optiune == '5':  # Verifică dacă opțiunea este 5
            cauta_elev(lista_elevi)  # Apelează funcția pentru căutarea unui elev
        elif optiune == '6':  # Verifică dacă opțiunea este 6
            afisare_dupa_medie(lista_elevi)  # Apelează funcția pentru afișarea elevilor după medie
        elif optiune == '7':  # Verifică dacă opțiunea este 7
            afisare_peste_medie(lista_elevi)  # Apelează funcția pentru afișarea elevilor cu media peste 8
        elif optiune == '8':  # Verifică dacă opțiunea este 8
            afisare_alfabetica(lista_elevi)  # Apelează funcția pentru afișarea elevilor în ordine alfabetică
        elif optiune == '9':  # Verifică dacă opțiunea este 9
            print("\nProgramul s-a încheiat. La revedere!")  # Afișează un mesaj de încheiere
            break  # Iese din bucla while și încheie programul
        else:  # Dacă opțiunea nu este niciuna dintre cele de mai sus
            print("Opțiune invalidă! Vă rugăm să introduceți un număr între 1 și 9.")  # Afișează un mesaj de eroare

if __name__ == "__main__":  # Verifică dacă scriptul este rulat direct (nu importat ca modul)
    meniu_principal()  # Apelează funcția principală pentru a porni programul