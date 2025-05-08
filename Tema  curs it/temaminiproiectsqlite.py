import sqlite3
import re
from typing import List, Optional, Dict, Any, Tuple
import os

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

class DatabaseManager:
    """
    Clasa pentru gestionarea conexiunii și operațiunilor cu baza de date SQLite
    """
    def __init__(self, db_name: str = "angajati.db"):
        """
        Inițializează managerul bazei de date și creează tabelele necesare dacă nu există
        
        Args:
            db_name (str): Numele fișierului bazei de date
        """
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
        # Conectare la baza de date și creare tabele
        self.connect()
        self.create_tables()
        self.close()
    
    def connect(self):
        """Stabilește conexiunea cu baza de date"""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
    
    def close(self):
        """Închide conexiunea cu baza de date"""
        if self.connection:
            self.connection.commit()
            self.connection.close()
            self.connection = None
            self.cursor = None
    
    def create_tables(self):
        """Creează tabelele necesare dacă nu există deja"""
        # Tabel departamente
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS departamente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT UNIQUE NOT NULL
        )
        ''')
        
        # Tabel seniorități
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS senioritati (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nume TEXT UNIQUE NOT NULL
        )
        ''')
        
        # Tabel angajați
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS angajati (
            cnp TEXT PRIMARY KEY,
            nume TEXT NOT NULL,
            prenume TEXT NOT NULL,
            varsta INTEGER NOT NULL,
            salar REAL NOT NULL,
            departament_id INTEGER NOT NULL,
            senioritate_id INTEGER NOT NULL,
            FOREIGN KEY (departament_id) REFERENCES departamente (id),
            FOREIGN KEY (senioritate_id) REFERENCES senioritati (id)
        )
        ''')
        
        # Populare tabele cu date inițiale dacă sunt goale
        self.cursor.execute("SELECT COUNT(*) FROM departamente")
        if self.cursor.fetchone()[0] == 0:
            departamente = ["IT", "Vânzări", "HR", "Marketing", "Financiar"]
            for dept in departamente:
                self.cursor.execute("INSERT INTO departamente (nume) VALUES (?)", (dept,))
        
        self.cursor.execute("SELECT COUNT(*) FROM senioritati")
        if self.cursor.fetchone()[0] == 0:
            senioritati = ["Junior", "Mid", "Senior"]
            for sen in senioritati:
                self.cursor.execute("INSERT INTO senioritati (nume) VALUES (?)", (sen,))
        
        self.connection.commit()
    
    def execute_query(self, query: str, params: tuple = ()) -> List[Tuple]:
        """
        Execută un query SQL și returnează rezultatele
        
        Args:
            query (str): Query-ul SQL de executat
            params (tuple): Parametrii pentru query
            
        Returns:
            List[Tuple]: Lista de rezultate
        """
        try:
            self.connect()
            self.cursor.execute(query, params)
            results = self.cursor.fetchall()
            return results
        finally:
            self.close()
    
    def execute_update(self, query: str, params: tuple = ()) -> int:
        """
        Execută un query SQL de tip UPDATE, INSERT sau DELETE
        
        Args:
            query (str): Query-ul SQL de executat
            params (tuple): Parametrii pentru query
            
        Returns:
            int: Numărul de rânduri afectate
        """
        try:
            self.connect()
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.rowcount
        finally:
            self.close()
    
    def get_all_departamente(self) -> List[str]:
        """Returnează lista departamentelor disponibile"""
        results = self.execute_query("SELECT nume FROM departamente ORDER BY nume")
        return [row[0] for row in results]
    
    def get_all_senioritati(self) -> List[str]:
        """Returnează lista seniorităților disponibile"""
        results = self.execute_query("SELECT nume FROM senioritati ORDER BY nume")
        return [row[0] for row in results]
    
    def get_departament_id(self, nume_departament: str) -> int:
        """Obține ID-ul unui departament după nume"""
        result = self.execute_query(
            "SELECT id FROM departamente WHERE nume = ?", 
            (nume_departament,)
        )
        if result:
            return result[0][0]
        return None
    
    def get_senioritate_id(self, nume_senioritate: str) -> int:
        """Obține ID-ul unei seniorități după nume"""
        result = self.execute_query(
            "SELECT id FROM senioritati WHERE nume = ?", 
            (nume_senioritate,)
        )
        if result:
            return result[0][0]
        return None
    
    def get_department_name(self, departament_id: int) -> str:
        """Obține numele departamentului după ID"""
        result = self.execute_query(
            "SELECT nume FROM departamente WHERE id = ?", 
            (departament_id,)
        )
        if result:
            return result[0][0]
        return None
    
    def get_senioritate_name(self, senioritate_id: int) -> str:
        """Obține numele seniorității după ID"""
        result = self.execute_query(
            "SELECT nume FROM senioritati WHERE id = ?", 
            (senioritate_id,)
        )
        if result:
            return result[0][0]
        return None
    
    def add_angajat(self, angajat: Angajat) -> bool:
        """
        Adaugă un angajat în baza de date
        
        Args:
            angajat (Angajat): Instanța angajatului de adăugat
            
        Returns:
            bool: True dacă adăugarea a reușit, False altfel
        """
        departament_id = self.get_departament_id(angajat.departament)
        senioritate_id = self.get_senioritate_id(angajat.senioritate)
        
        if not departament_id or not senioritate_id:
            return False
        
        try:
            self.execute_update(
                """INSERT INTO angajati 
                   (cnp, nume, prenume, varsta, salar, departament_id, senioritate_id) 
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (angajat.cnp, angajat.nume, angajat.prenume, angajat.varsta, 
                 angajat.salar, departament_id, senioritate_id)
            )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_angajat_by_cnp(self, cnp: str) -> Optional[Angajat]:
        """
        Găsește un angajat după CNP
        
        Args:
            cnp (str): CNP-ul angajatului căutat
            
        Returns:
            Optional[Angajat]: Instanța angajatului sau None dacă nu este găsit
        """
        result = self.execute_query(
            """SELECT a.cnp, a.nume, a.prenume, a.varsta, a.salar, 
               d.nume, s.nume
               FROM angajati a
               JOIN departamente d ON a.departament_id = d.id
               JOIN senioritati s ON a.senioritate_id = s.id
               WHERE a.cnp = ?""",
            (cnp,)
        )
        
        if result:
            row = result[0]
            return Angajat(
                cnp=row[0],
                nume=row[1],
                prenume=row[2],
                varsta=row[3],
                salar=row[4],
                departament=row[5],
                senioritate=row[6]
            )
        return None
    
    def update_angajat_salar(self, cnp: str, salar: float) -> bool:
        """
        Actualizează salariul unui angajat
        
        Args:
            cnp (str): CNP-ul angajatului
            salar (float): Noul salariu
            
        Returns:
            bool: True dacă actualizarea a reușit, False altfel
        """
        rows_affected = self.execute_update(
            "UPDATE angajati SET salar = ? WHERE cnp = ?",
            (salar, cnp)
        )
        return rows_affected > 0
    
    def delete_angajat(self, cnp: str) -> bool:
        """
        Șterge un angajat din baza de date
        
        Args:
            cnp (str): CNP-ul angajatului de șters
            
        Returns:
            bool: True dacă ștergerea a reușit, False altfel
        """
        rows_affected = self.execute_update(
            "DELETE FROM angajati WHERE cnp = ?",
            (cnp,)
        )
        return rows_affected > 0
    
    def get_all_angajati(self) -> List[Angajat]:
        """
        Returnează lista tuturor angajaților
        
        Returns:
            List[Angajat]: Lista de obiecte Angajat
        """
        results = self.execute_query(
            """SELECT a.cnp, a.nume, a.prenume, a.varsta, a.salar, 
               d.nume, s.nume
               FROM angajati a
               JOIN departamente d ON a.departament_id = d.id
               JOIN senioritati s ON a.senioritate_id = s.id
               ORDER BY a.nume, a.prenume"""
        )
        
        angajati = []
        for row in results:
            angajati.append(Angajat(
                cnp=row[0],
                nume=row[1],
                prenume=row[2],
                varsta=row[3],
                salar=row[4],
                departament=row[5],
                senioritate=row[6]
            ))
        
        return angajati
    
    def get_total_salarii(self) -> float:
        """
        Calculează suma totală a salariilor
        
        Returns:
            float: Suma totală a salariilor
        """
        result = self.execute_query("SELECT SUM(salar) FROM angajati")
        if result and result[0][0]:
            return float(result[0][0])
        return 0.0
    
    def get_total_salarii_departament(self, departament: str) -> float:
        """
        Calculează suma salariilor pentru un anumit departament
        
        Args:
            departament (str): Numele departamentului
            
        Returns:
            float: Suma salariilor din departament
        """
        departament_id = self.get_departament_id(departament)
        if not departament_id:
            return 0.0
        
        result = self.execute_query(
            "SELECT SUM(salar) FROM angajati WHERE departament_id = ?",
            (departament_id,)
        )
        
        if result and result[0][0]:
            return float(result[0][0])
        return 0.0
    
    def get_angajati_by_senioritate(self, senioritate: str) -> List[Angajat]:
        """
        Returnează angajații cu o anumită senioritate
        
        Args:
            senioritate (str): Nivelul de senioritate căutat
            
        Returns:
            List[Angajat]: Lista de angajați
        """
        senioritate_id = self.get_senioritate_id(senioritate)
        if not senioritate_id:
            return []
        
        results = self.execute_query(
            """SELECT a.cnp, a.nume, a.prenume, a.varsta, a.salar, 
               d.nume, s.nume
               FROM angajati a
               JOIN departamente d ON a.departament_id = d.id
               JOIN senioritati s ON a.senioritate_id = s.id
               WHERE a.senioritate_id = ?
               ORDER BY a.nume, a.prenume""",
            (senioritate_id,)
        )
        
        angajati = []
        for row in results:
            angajati.append(Angajat(
                cnp=row[0],
                nume=row[1],
                prenume=row[2],
                varsta=row[3],
                salar=row[4],
                departament=row[5],
                senioritate=row[6]
            ))
        
        return angajati
    
    def get_angajati_by_departament(self, departament: str) -> List[Angajat]:
        """
        Returnează angajații dintr-un anumit departament
        
        Args:
            departament (str): Numele departamentului
            
        Returns:
            List[Angajat]: Lista de angajați
        """
        departament_id = self.get_departament_id(departament)
        if not departament_id:
            return []
        
        results = self.execute_query(
            """SELECT a.cnp, a.nume, a.prenume, a.varsta, a.salar, 
               d.nume, s.nume
               FROM angajati a
               JOIN departamente d ON a.departament_id = d.id
               JOIN senioritati s ON a.senioritate_id = s.id
               WHERE a.departament_id = ?
               ORDER BY a.nume, a.prenume""",
            (departament_id,)
        )
        
        angajati = []
        for row in results:
            angajati.append(Angajat(
                cnp=row[0],
                nume=row[1],
                prenume=row[2],
                varsta=row[3],
                salar=row[4],
                departament=row[5],
                senioritate=row[6]
            ))
        
        return angajati
    
    def get_departamente_counts(self) -> Dict[str, int]:
        """
        Numără angajații din fiecare departament
        
        Returns:
            Dict[str, int]: Dicționar cu numele departamentului și numărul de angajați
        """
        results = self.execute_query(
            """SELECT d.nume, COUNT(a.cnp)
               FROM departamente d
               LEFT JOIN angajati a ON d.id = a.departament_id
               GROUP BY d.nume
               ORDER BY d.nume"""
        )
        
        return {row[0]: row[1] for row in results}


class SistemManagementAngajati:
    def __init__(self):
        """
        Inițializare sistem de management cu conexiunea la baza de date
        """
        self.db_manager = DatabaseManager()

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
                if not self.db_manager.get_angajat_by_cnp(cnp):
                    break
                else:
                    print("CNP deja există în sistem!")
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
        
        # Validare departament - SCHIMBAT: nu mai folosim .capitalize()
        departamente = self.db_manager.get_all_departamente()
        while True:
            print("Departamente disponibile:", ', '.join(departamente))
            departament = input("Introduceți departamentul: ").strip()  # Am eliminat .capitalize()
            if departament in departamente:
                break
            else:
                print("Departament invalid!")
        
        # Validare senioritate
        senioritati = self.db_manager.get_all_senioritati()
        while True:
            print("Nivele de senioritate:", ', '.join(senioritati))
            senioritate = input("Introduceți senioritatea: ").capitalize()
            if senioritate in senioritati:
                break
            else:
                print("Nivel de senioritate invalid!")
        
        # Creare angajat nou
        angajat_nou = Angajat(cnp, nume, prenume, varsta, salar, departament, senioritate)
        if self.db_manager.add_angajat(angajat_nou):
            print("Angajat adăugat cu succes!")
        else:
            print("Eroare la adăugarea angajatului!")

    def cautare_angajat(self) -> Optional[Angajat]:
        """
        Caută un angajat după CNP
        
        Returns:
            Optional[Angajat]: Angajatul găsit sau None
        """
        cnp = input("Introduceți CNP-ul angajatului: ")
        angajat = self.db_manager.get_angajat_by_cnp(cnp)
        
        if angajat:
            print(f"\nAngajat găsit: {angajat.nume} {angajat.prenume}")
            print(f"CNP: {angajat.cnp}")
            print(f"Vârsta: {angajat.varsta}")
            print(f"Departament: {angajat.departament}")
            print(f"Senioritate: {angajat.senioritate}")
            print(f"Salar: {angajat.salar:.2f} RON")
            return angajat
        else:
            print("Angajat negăsit!")
            return None

    def modificare_angajat(self):
        """
        Modifică datele unui angajat
        """
        angajat = self.cautare_angajat()
        if angajat:
            print("\n--- Modificare Angajat ---")
            print("Lăsați câmpul necompletat pentru a păstra datele curente.")
            
            # Modificare salar
            nou_salar = input(f"Salar curent {angajat.salar} RON. Nou salar: ")
            if nou_salar:
                try:
                    nou_salar = float(nou_salar)
                    if self.validare_salar(nou_salar):
                        if self.db_manager.update_angajat_salar(angajat.cnp, nou_salar):
                            print("Salar actualizat cu succes!")
                        else:
                            print("Eroare la actualizarea salarului!")
                    else:
                        print("Salar invalid!")
                except ValueError:
                    print("Salar invalid!")

    def stergere_angajat(self):
        """
        Șterge un angajat din sistem
        """
        cnp = input("Introduceți CNP-ul angajatului de șters: ")
        if self.db_manager.delete_angajat(cnp):
            print("Angajat șters cu succes!")
        else:
            print("Angajat negăsit!")

    def afisare_angajati(self):
        """
        Afișează toți angajații
        """
        angajati = self.db_manager.get_all_angajati()
        
        if not angajati:
            print("Nu există angajați!")
            return
        
        print("\n--- Lista Angajați ---")
        for angajat in angajati:
            print(f"CNP: {angajat.cnp}, Nume: {angajat.nume} {angajat.prenume}, "
                  f"Departament: {angajat.departament}, Senioritate: {angajat.senioritate}")

    def calcul_total_salarii(self):
        """
        Calculează costul total al salariilor
        """
        total = self.db_manager.get_total_salarii()
        print(f"Cost total salarii: {total:.2f} RON")

    def calcul_salarii_departament(self):
        """
        Calculează costul total al salariilor pentru un departament
        """
        departamente = self.db_manager.get_all_departamente()
        print("Departamente disponibile:", ', '.join(departamente))
        departament = input("Introduceți departamentul: ").strip()  # Am eliminat .capitalize()
        
        if departament in departamente:
            total = self.db_manager.get_total_salarii_departament(departament)
            print(f"Cost total salarii departament {departament}: {total:.2f} RON")
        else:
            print("Departament invalid!")

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
            print(f"Angajat: {angajat.nume} {angajat.prenume}")
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
        senioritati = self.db_manager.get_all_senioritati()
        
        for senioritate in senioritati:
            print(f"\n--- {senioritate} ---")
            angajati = self.db_manager.get_angajati_by_senioritate(senioritate)
            
            if angajati:
                for ang in angajati:
                    print(f"{ang.nume} {ang.prenume} - {ang.departament}")
            else:
                print("Niciun angajat")

    def afisare_dupa_departament(self):
        """
        Afișează angajații grupați după departament
        """
        departamente = self.db_manager.get_all_departamente()
        
        for departament in departamente:
            print(f"\n--- {departament} ---")
            angajati = self.db_manager.get_angajati_by_departament(departament)
            
            if angajati:
                for ang in angajati:
                    print(f"{ang.nume} {ang.prenume} - {ang.senioritate}")
            else:
                print("Niciun angajat")
    
    def statistici_departamente(self):
        """
        Afișează statistici despre departamente
        """
        stats = self.db_manager.get_departamente_counts()
        
        print("\n--- Statistici Departamente ---")
        for dept, count in stats.items():
            print(f"{dept}: {count} angajați")

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
            print("11. Statistici departamente")
            print("12. Ieșire")

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
                    self.statistici_departamente()
                elif optiune == 12:
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