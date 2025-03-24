import re
from typing import List, Optional

class Angajat:
    def __init__(self, cnp: str, nume: str, prenume: str, varsta: int, 
                 salar: float, departament: str, senioritate: str):
        """
        Constructor pentru clasa Angajat
        
        Args:
            cnp (str): Cod Numeric Personal 
            nume (str): Numele angajatului
            prenume (str): Prenumele angajatului
            varsta (int): Vârsta angajatului
            salar (float): Salariul brut
            departament (str): Departamentul angajatului
            senioritate (str): Nivelul de senioritate
        """
        self.cnp = cnp
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
        self.salar = salar
        self.departament = departament
        self.senioritate = senioritate

class SistemManagementAngajati:
    def __init__(self):
        """
        Inițializare sistem de management cu lista de angajați
        """
        self.angajati: List[Angajat] = []

    def validare_cnp(self, cnp: str) -> bool:
        """
        Validează CNP-ul introdus
        
        Args:
            cnp (str): CNP de verificat
        
        Returns:
            bool: True dacă CNP-ul este valid, False altfel
        """
        # Verifică lungimea și să conțină doar cifre
        return len(cnp) == 13 and cnp.isdigit()

    def validare_varsta(self, varsta: int) -> bool:
        """
        Validează vârsta angajatului
        
        Args:
            varsta (int): Vârsta de verificat
        
        Returns:
            bool: True dacă vârsta este validă, False altfel
        """
        return 18 <= varsta <= 65

    def validare_salar(self, salar: float) -> bool:
        """
        Validează salariul angajatului
        
        Args:
            salar (float): Salariul de verificat
        
        Returns:
            bool: True dacă salariul este valid, False altfel
        """
        return salar >= 4050

    def adaugare_angajat(self):
        """
        Adaugă un nou angajat în sistem
        """
        print("\n--- Adăugare Angajat Nou ---")
        
        # Validare CNP
        while True:
            cnp = input("Introduceți CNP (13 cifre): ")
            if self.validare_cnp(cnp):
                # Verifică unicitate CNP
                if not any(ang.cnp == cnp for ang in self.angajati):
                    break
                else:
                    print("CNP deja exist în sistem!")
            else:
                print("CNP invalid! Trebuie să fie 13 cifre.")
        
        # Validare nume și prenume
        while True:
            nume = input("Introduceți numele: ").strip().capitalize()
            prenume = input("Introduceți prenumele: ").strip().capitalize()
            if len(nume) > 1 and len(prenume) > 1:
                break
            else:
                print("Numele și prenumele trebuie să aibă minim 2 caractere!")
        
        # Validare vârstă
        while True:
            try:
                varsta = int(input("Introduceți vârsta: "))
                if self.validare_varsta(varsta):
                    break
                else:
                    print("Vârsta trebuie să fie între 18 și 65 de ani!")
            except ValueError:
                print("Vârsta trebuie să fie un număr întreg!")
        
        # Validare salar
        while True:
            try:
                salar = float(input("Introduceți salariul brut: "))
                if self.validare_salar(salar):
                    break
                else:
                    print(f"Salariul trebuie să fie minim {4050} RON!")
            except ValueError:
                print("Salariul trebuie să fie un număr!")
        
        # Validare departament
        departamente = ["IT", "Vânzări", "HR", "Marketing", "Financiar"]
        while True:
            print("Departamente disponibile:", ', '.join(departamente))
            departament = input("Introduceți departamentul: ").capitalize()
            if departament in departamente:
                break
            else:
                print("Departament invalid!")
        
        # Validare senioritate
        senioritati = ["Junior", "Mid", "Senior"]
        while True:
            print("Nivele de senioritate:", ', '.join(senioritati))
            senioritate = input("Introduceți senioritatea: ").capitalize()
            if senioritate in senioritati:
                break
            else:
                print("Nivel de senioritate invalid!")
        
        # Creare angajat nou
        angajat_nou = Angajat(cnp, nume, prenume, varsta, salar, departament, senioritate)
        self.angajati.append(angajat_nou)
        print("Angajat adăugat cu succes!")

    def cautare_angajat(self) -> Optional[Angajat]:
        """
        Caută un angajat după CNP
        
        Returns:
            Optional[Angajat]: Angajatul găsit sau None
        """
        cnp = input("Introduceți CNP-ul angajatului: ")
        for angajat in self.angajati:
            if angajat.cnp == cnp:
                return angajat
        print("Angajat nefăcut!")
        return None

    def modificare_angajat(self):
        """
        Modifică datele unui angajat
        """
        angajat = self.cautare_angajat()
        if angajat:
            print("\n--- Modificare Angajat ---")
            print("Lăsați câmpul necompletat pentru a păstra datele curente.")
            
            # Similar cu adăugare, dar opțional
            nou_salar = input(f"Salar curent {angajat.salar} RON. Nou salar: ")
            if nou_salar:
                try:
                    nou_salar = float(nou_salar)
                    if self.validare_salar(nou_salar):
                        angajat.salar = nou_salar
                    else:
                        print("Salar invalid!")
                except ValueError:
                    print("Salar invalid!")
            
            print("Modificare realizată cu succes!")

    def stergere_angajat(self):
        """
        Șterge un angajat din sistem
        """
        cnp = input("Introduceți CNP-ul angajatului de șters: ")
        for angajat in self.angajati:
            if angajat.cnp == cnp:
                self.angajati.remove(angajat)
                print("Angajat șters cu succes!")
                return
        print("Angajat nefăcut!")

    def afisare_angajati(self):
        """
        Afișează toți angajații
        """
        if not self.angajati:
            print("Nu există angajați!")
            return
        
        for angajat in self.angajati:
            print(f"CNP: {angajat.cnp}, Nume: {angajat.nume} {angajat.prenume}, "
                  f"Departament: {angajat.departament}, Senioritate: {angajat.senioritate}")

    def calcul_total_salarii(self):
        """
        Calculează costul total al salariilor
        """
        total = sum(angajat.salar for angajat in self.angajati)
        print(f"Cost total salarii: {total:.2f} RON")

    def calcul_salarii_departament(self):
        """
        Calculează costul total al salariilor pentru un departament
        """
        departament = input("Introduceți departamentul: ").capitalize()
        total = sum(angajat.salar for angajat in self.angajati if angajat.departament == departament)
        print(f"Cost total salarii departament {departament}: {total:.2f} RON")

    def calcul_fluturas_salar(self):
        """
        Calculează fluturașul de salar pentru un angajat
        """
        angajat = self.cautare_angajat()
        if angajat:
            brut = angajat.salar
            cas = brut * 0.10
            cass = brut * 0.25
            impozabil = brut - cas - cass
            impozit = impozabil * 0.10
            net = impozabil - impozit

            print("\n--- Fluturaș Salar ---")
            print(f"Salar Brut: {brut:.2f} RON")
            print(f"CAS (10%): {cas:.2f} RON")
            print(f"CASS (25%): {cass:.2f} RON")
            print(f"Salar Impozabil: {impozabil:.2f} RON")
            print(f"Impozit (10%): {impozit:.2f} RON")
            print(f"Salar Net: {net:.2f} RON")

    def afisare_dupa_senioritate(self):
        """
        Afișează angajații grupați după senioritate
        """
        senioritati = ["Junior", "Mid", "Senior"]
        for seniority in senioritati:
            print(f"\n--- {seniority} ---")
            angajati_seniori = [ang for ang in self.angajati if ang.senioritate == seniority]
            if angajati_seniori:
                for ang in angajati_seniori:
                    print(f"{ang.nume} {ang.prenume} - {ang.departament}")
            else:
                print("Niciun angajat")

    def afisare_dupa_departament(self):
        """
        Afișează angajații grupați după departament
        """
        departamente = set(ang.departament for ang in self.angajati)
        for dept in departamente:
            print(f"\n--- {dept} ---")
            angajati_dept = [ang for ang in self.angajati if ang.departament == dept]
            for ang in angajati_dept:
                print(f"{ang.nume} {ang.prenume} - {ang.senioritate}")

    def meniu(self):
        """
        Meniu principal pentru interacțiune
        """
        while True:
            print("\n--- Sistem Management Angajați ---")
            print("1. Adăugare angajat")
            print("2. Cautare angajat")
            print("3. Modificare date angajat")
            print("4. Ștergere angajat")
            print("5. Afișare angajați")
            print("6. Calculator cost total salarii")
            print("7. Calculator cost total salarii departament")
            print("8. Calculator fluturaș salar")
            print("9. Afișare angajați după senioritate")
            print("10. Afișare angajați după departament")
            print("11. Ieșire")

            try:
                optiune = int(input("Alegeți o opțiune: "))
                
                if optiune == 1:
                    self.adaugare_angajat()
                elif optiune == 2:
                    self.cautare_angajat()
                elif optiune == 3:
                    self.modificare_angajat()
                elif optiune == 4:
                    self.stergere_angajat()
                elif optiune == 5:
                    self.afisare_angajati()
                elif optiune == 6:
                    self.calcul_total_salarii()
                elif optiune == 7:
                    self.calcul_salarii_departament()
                elif optiune == 8:
                    self.calcul_fluturas_salar()
                elif optiune == 9:
                    self.afisare_dupa_senioritate()
                elif optiune == 10:
                    self.afisare_dupa_departament()
                elif optiune == 11:
                    print("La revedere!")
                    break
                else:
                    print("Opțiune invalidă!")
            except ValueError:
                print("Introduceți un număr!")

def main():
    sistem = SistemManagementAngajati()
    sistem.meniu()

if __name__ == "__main__":
    main()