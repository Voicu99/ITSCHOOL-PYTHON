def exercise_42():
    """Create a tuple with 5 different elements and display the second and last element."""
    # Funcția pentru exercițiul 42 cu docstring care explică ce face
    
    print("\n=== Exercise 42 ===")
    # Afișează titlul exercițiului pentru o mai bună organizare
    
    my_tuple = (10, 20, 30, 40, 50)
    # Creează un tuple cu 5 elemente diferite (numere întregi)
    
    print("Tuple:", my_tuple)
    # Afișează întregul tuple creat
    
    print("Second element:", my_tuple[1])
    # Afișează al doilea element al tuple-ului, accesându-l cu indexul 1 (indexarea începe de la 0)
    
    print("Last element:", my_tuple[-1])
    # Afișează ultimul element al tuple-ului folosind indexarea negativă (-1)
    
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul înainte de a continua

def exercise_43():
    """Create 2 tuples with 3 elements each. Concatenate them and display the resulting tuple."""
    # Funcția pentru exercițiul 43 cu docstring care explică ce face
    
    print("\n=== Exercise 43 ===")
    # Afișează titlul exercițiului
    
    tuple1 = (1, 2, 3)
    # Creează primul tuple cu 3 elemente numerice
    
    tuple2 = ('a', 'b', 'c')
    # Creează al doilea tuple cu 3 elemente de tip string
    
    result_tuple = tuple1 + tuple2
    # Concatenează cele două tuple-uri folosind operatorul + și stochează rezultatul
    
    print("First tuple:", tuple1)
    # Afișează primul tuple
    
    print("Second tuple:", tuple2)
    # Afișează al doilea tuple
    
    print("Concatenated tuple:", result_tuple)
    # Afișează tuple-ul rezultat în urma concatenării
    
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def exercise_44():
    """Create a tuple with 10 elements. Read an element from the keyboard and check if it's in the tuple."""
    # Funcția pentru exercițiul 44 cu docstring explicativ
    
    print("\n=== Exercise 44 ===")
    # Afișează titlul exercițiului
    
    ten_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    # Creează un tuple cu 10 elemente numerice
    
    print("Tuple:", ten_tuple)
    # Afișează tuple-ul creat
    
    try:
        # Bloc try pentru a gestiona erorile posibile la conversia input-ului
        
        element = int(input("Enter a number to check if it's in the tuple: "))
        # Citește un număr de la tastatură și îl convertește la int
        
        if element in ten_tuple:
            # Verifică dacă elementul introdus se află în tuple
            print(f"{element} is in the tuple")
            # Afișează mesaj dacă elementul este găsit
        else:
            print(f"{element} is not in the tuple")
            # Afișează mesaj dacă elementul nu este găsit
    except ValueError:
        # Prinde excepția în cazul în care input-ul nu poate fi convertit la int
        print("Invalid input. Please enter a number.")
        # Afișează mesaj de eroare
        
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def exercise_45():
    """Create a tuple with 5 elements. Read an element from the keyboard and display its index."""
    # Funcția pentru exercițiul 45 cu docstring explicativ
    
    print("\n=== Exercise 45 ===")
    # Afișează titlul exercițiului
    
    five_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
    # Creează un tuple cu 5 elemente de tip string (nume de fructe)
    
    print("Tuple:", five_tuple)
    # Afișează tuple-ul creat
    
    search_element = input("Enter an element to find its index: ")
    # Citește un element de la tastatură
    
    if search_element in five_tuple:
        # Verifică dacă elementul introdus se află în tuple
        print(f"Index of {search_element}: {five_tuple.index(search_element)}")
        # Afișează indexul elementului găsit folosind metoda .index()
    else:
        print("not found")
        # Afișează "not found" conform cerinței dacă elementul nu este găsit
        
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def exercise_46():
    """Create a tuple with 10 elements. Extract a subtuple from position 2 to 5 and display it."""
    # Funcția pentru exercițiul 46 cu docstring explicativ
    
    print("\n=== Exercise 46 ===")
    # Afișează titlul exercițiului
    
    alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    # Creează un tuple cu 10 elemente (literele de la a la j)
    
    print("Original tuple:", alphabet_tuple)
    # Afișează tuple-ul original
    
    subtuple = alphabet_tuple[2:6]  # From index 2 to 5 (6 is exclusive)
    # Extrage un subtuple de la indexul 2 până la indexul 5 inclusiv
    # (indexul 6 este exclus în slicing-ul Python)
    
    print("Subtuple from position 2 to 5:", subtuple)
    # Afișează subtuple-ul extras
    
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def exercise_47():
    """Given a list [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9], remove duplicate elements and display the result."""
    # Funcția pentru exercițiul 47 cu docstring explicativ
    
    print("\n=== Exercise 47 ===")
    # Afișează titlul exercițiului
    
    duplicate_list = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    # Creează lista cu elemente duplicate conform cerinței
    
    print("Original list:", duplicate_list)
    # Afișează lista originală
    
    unique_list = list(dict.fromkeys(duplicate_list))  # Method 1: Using dictionary
    # Elimină duplicatele folosind metoda dict.fromkeys care păstrează ordinea elementelor
    # și convertește rezultatul înapoi la listă
    
    print("List after removing duplicates (method 1):", unique_list)
    # Afișează lista după eliminarea duplicatelor folosind prima metodă
    
    # Alternative method using set
    unique_list2 = list(set(duplicate_list))
    # Elimină duplicatele convertind lista la set (care nu permite duplicate)
    # și apoi convertind rezultatul înapoi la listă
    
    print("List after removing duplicates (method 2):", unique_list2)
    # Afișează lista după eliminarea duplicatelor folosind a doua metodă
    
    # Note: set method doesn't preserve order, while dict.fromkeys does
    # Comentariu explicativ despre diferența dintre cele două metode
    
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def exercise_48():
    """Given two sets: {1,2,3,4,5,6} and {4,5,6,7,8,9}, display elements that are in both sets."""
    # Funcția pentru exercițiul 48 cu docstring explicativ
    
    print("\n=== Exercise 48 ===")
    # Afișează titlul exercițiului
    
    set1 = {1, 2, 3, 4, 5, 6}
    # Creează primul set cu elementele specificate
    
    set2 = {4, 5, 6, 7, 8, 9}
    # Creează al doilea set cu elementele specificate
    
    print("Set 1:", set1)
    # Afișează primul set
    
    print("Set 2:", set2)
    # Afișează al doilea set
    
    common_elements = set1.intersection(set2)
    # Găsește elementele comune (intersecția) celor două seturi folosind metoda .intersection()
    
    print("Elements in both sets:", common_elements)
    # Afișează elementele comune găsite
    
    input("\nPress Enter to continue...")
    # Pauză pentru a permite utilizatorului să citească rezultatul

def run_all_exercises():
    """Run all exercises in sequence."""
    # Funcție pentru a rula toate exercițiile în secvență
    
    exercise_42()
    exercise_43()
    exercise_44()
    exercise_45()
    exercise_46()
    exercise_47()
    exercise_48()
    # Apelează pe rând fiecare funcție de exercițiu

def main():
    """Main menu to select and run exercises."""
    # Funcția principală care afișează meniul și gestionează selecțiile utilizatorului
    
    while True:
        # Buclă infinită pentru a menține meniul activ până când utilizatorul alege să iasă
        
        print("\n=== Python Tuple and Set Exercises ===")
        # Afișează titlul meniului principal
        
        print("1. Exercise 42: Display elements from a 5-element tuple")
        print("2. Exercise 43: Concatenate two tuples")
        print("3. Exercise 44: Check if an element is in a tuple")
        print("4. Exercise 45: Find index of an element in a tuple")
        print("5. Exercise 46: Extract a subtuple")
        print("6. Exercise 47: Remove duplicates from a list")
        print("7. Exercise 48: Find common elements in two sets")
        print("8. Run all exercises")
        print("0. Exit")
        # Afișează opțiunile meniului
        
        choice = input("\nEnter your choice (0-8): ")
        # Citește opțiunea utilizatorului
        
        if choice == '1':
            exercise_42()
            # Apelează funcția pentru exercițiul 42 dacă utilizatorul alege 1
        elif choice == '2':
            exercise_43()
            # Apelează funcția pentru exercițiul 43 dacă utilizatorul alege 2
        elif choice == '3':
            exercise_44()
            # Apelează funcția pentru exercițiul 44 dacă utilizatorul alege 3
        elif choice == '4':
            exercise_45()
            # Apelează funcția pentru exercițiul 45 dacă utilizatorul alege 4
        elif choice == '5':
            exercise_46()
            # Apelează funcția pentru exercițiul 46 dacă utilizatorul alege 5
        elif choice == '6':
            exercise_47()
            # Apelează funcția pentru exercițiul 47 dacă utilizatorul alege 6
        elif choice == '7':
            exercise_48()
            # Apelează funcția pentru exercițiul 48 dacă utilizatorul alege 7
        elif choice == '8':
            run_all_exercises()
            # Apelează funcția pentru a rula toate exercițiile dacă utilizatorul alege 8
        elif choice == '0':
            print("Exiting program. Goodbye!")
            # Afișează mesaj de încheiere
            break
            # Iese din bucla while pentru a termina programul
        else:
            print("Invalid choice. Please try again.")
            # Afișează mesaj de eroare pentru opțiuni invalide

if __name__ == "__main__":
    main()
    # Verifică dacă scriptul este rulat direct (nu importat ca modul)
    # și apelează funcția main() dacă este cazul