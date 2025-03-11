#Funcția pentru exercițiul 42
def exercise_42():
    """Create a tuple with 5 different elements and display the second and last element."""
    # Afișează titlul exercițiului pentru o mai bună organizare
    print("\n=== Exercise 42 ===")
    # Creează un tuple cu 5 elemente diferite (numere întregi)
    my_tuple = (10, 20, 30, 40, 50)
    # Afișează întregul tuple creat
    print("Tuple:", my_tuple)
    # Afișează al doilea element al tuple-ului, accesându-l cu indexul 1 (indexarea începe de la 0)
    print("Second element:", my_tuple[1])
    # Afișează ultimul element al tuple-ului folosind indexarea negativă (-1)
    print("Last element:", my_tuple[-1])
    # Pauză pentru a permite utilizatorului să citească rezultatul înainte de a continua
    input("\nPress Enter to continue...")

# Funcția pentru exercițiul 43
def exercise_43():
    """Create 2 tuples with 3 elements each. Concatenate them and display the resulting tuple."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 43 ===")
    # Creează primul tuple cu 3 elemente numerice
    tuple1 = (1, 2, 3)
    # Creează al doilea tuple cu 3 elemente de tip string
    tuple2 = ('a', 'b', 'c')
    # Concatenează cele două tuple-uri folosind operatorul + și stochează rezultatul
    result_tuple = tuple1 + tuple2
    # Afișează primul tuple
    print("First tuple:", tuple1)
    # Afișează al doilea tuple
    print("Second tuple:", tuple2)
    # Afișează tuple-ul rezultat în urma concatenării
    print("Concatenated tuple:", result_tuple)
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcția pentru exercițiul 44
def exercise_44():
    """Create a tuple with 10 elements. Read an element from the keyboard and check if it's in the tuple."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 44 ===")
    # Creează un tuple cu 10 elemente numerice
    ten_tuple = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    # Afișează tuple-ul creat
    print("Tuple:", ten_tuple)
    # Bloc try pentru a gestiona erorile posibile la conversia input-ului
    try:
        # Citește un număr de la tastatură și îl convertește la int
        element = int(input("Enter a number to check if it's in the tuple: "))
        # Verifică dacă elementul introdus se află în tuple
        if element in ten_tuple:
            # Afișează mesaj dacă elementul este găsit
            print(f"{element} is in the tuple")
        else:
            # Afișează mesaj dacă elementul nu este găsit
            print(f"{element} is not in the tuple")
    # Prinde excepția în cazul în care input-ul nu poate fi convertit la int
    except ValueError:
        # Afișează mesaj de eroare
        print("Invalid input. Please enter a number.")
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcția pentru exercițiul 45
def exercise_45():
    """Create a tuple with 5 elements. Read an element from the keyboard and display its index."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 45 ===")
    # Creează un tuple cu 5 elemente de tip string (nume de fructe)
    five_tuple = ('apple', 'banana', 'cherry', 'date', 'elderberry')
    # Afișează tuple-ul creat
    print("Tuple:", five_tuple)
    # Citește un element de la tastatură
    search_element = input("Enter an element to find its index: ")
    # Verifică dacă elementul introdus se află în tuple
    if search_element in five_tuple:
        # Afișează indexul elementului găsit folosind metoda .index()
        print(f"Index of {search_element}: {five_tuple.index(search_element)}")
    else:
        # Afișează "not found" conform cerinței dacă elementul nu este găsit
        print("not found")
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcția pentru exercițiul 46
def exercise_46():
    """Create a tuple with 10 elements. Extract a subtuple from position 2 to 5 and display it."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 46 ===")
    # Creează un tuple cu 10 elemente (literele de la a la j)
    alphabet_tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
    # Afișează tuple-ul original
    print("Original tuple:", alphabet_tuple)
    # Extrage un subtuple de la indexul 2 până la indexul 5 inclusiv (indexul 6 este exclus în slicing-ul Python)
    subtuple = alphabet_tuple[2:6]  # From index 2 to 5 (6 is exclusive)
    # Afișează subtuple-ul extras
    print("Subtuple from position 2 to 5:", subtuple)
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcția pentru exercițiul 47
def exercise_47():
    """Given a list [1,1,2,2,2,3,4,5,5,5,5,6,7,8,9,9,9], remove duplicate elements and display the result."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 47 ===")
    # Creează lista cu elemente duplicate conform cerinței
    duplicate_list = [1, 1, 2, 2, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 9, 9]
    # Afișează lista originală
    print("Original list:", duplicate_list)
    # Elimină duplicatele folosind metoda dict.fromkeys care păstrează ordinea elementelor și convertește rezultatul înapoi la listă
    unique_list = list(dict.fromkeys(duplicate_list))  # Method 1: Using dictionary
    # Afișează lista după eliminarea duplicatelor folosind prima metodă
    print("List after removing duplicates (method 1):", unique_list)
    
    # Elimină duplicatele convertind lista la set (care nu permite duplicate) și apoi convertind rezultatul înapoi la listă
    unique_list2 = list(set(duplicate_list))
    # Afișează lista după eliminarea duplicatelor folosind a doua metodă
    print("List after removing duplicates (method 2):", unique_list2)
    # Comentariu explicativ despre diferența dintre cele două metode
    # Note: set method doesn't preserve order, while dict.fromkeys does
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcția pentru găsirea manuală a elementelor comune între două seturi
def find_common_elements_manually(set1, set2):
    """
    Finds common elements between two sets without using built-in set methods.
    
    Args:
        set1: First set
        set2: Second set
        
    Returns:
        A set containing common elements
    """
    # Creează un set gol pentru a stoca elementele comune
    common_elements = set()
    
    # Iterează prin fiecare element din primul set
    for element in set1:
        # Verifică dacă elementul există și în al doilea set
        if element in set2:
            # Dacă elementul există în ambele seturi, îl adaugă la setul de rezultate
            common_elements.add(element)
    
    # Returnează setul cu elementele comune
    return common_elements

# Funcția pentru exercițiul 48
def exercise_48():
    """Given two sets: {1,2,3,4,5,6} and {4,5,6,7,8,9}, display elements that are in both sets."""
    # Afișează titlul exercițiului
    print("\n=== Exercise 48 ===")
    # Creează primul set cu elementele specificate
    set1 = {1, 2, 3, 4, 5, 6}
    # Creează al doilea set cu elementele specificate
    set2 = {4, 5, 6, 7, 8, 9}
    # Afișează primul set
    print("Set 1:", set1)
    # Afișează al doilea set
    print("Set 2:", set2)
    
    # Metoda 1: Folosind metoda predefinită intersection()
    common_elements = set1.intersection(set2)
    # Afișează elementele comune găsite cu metoda predefinită
    print("Elements in both sets (using intersection method):", common_elements)
    
    # Metoda 2: Folosind algoritmul manual implementat
    manual_common_elements = find_common_elements_manually(set1, set2)
    # Afișează elementele comune găsite cu algoritmul manual
    print("Elements in both sets (using manual algorithm):", manual_common_elements)
    
    # Verifică dacă ambele metode produc același rezultat
    print("Both methods give the same result:", common_elements == manual_common_elements)
    
    # Afișează explicația algoritmului manual folosit
    print("\nAlgorithm explanation:")
    print("1. We created an empty set to store common elements")
    print("2. We iterated through each element of the first set")
    print("3. For each element, we checked if it exists in the second set")
    print("4. If an element exists in both sets, we added it to our result set")
    print("5. Time Complexity: O(n) where n is the size of the first set")
    print("6. Space Complexity: O(m) where m is the number of common elements")
    
    # Pauză pentru a permite utilizatorului să citească rezultatul
    input("\nPress Enter to continue...")

# Funcție pentru a rula toate exercițiile în secvență
def run_all_exercises():
    """Run all exercises in sequence."""
    # Apelează pe rând fiecare funcție de exercițiu
    exercise_42()
    exercise_43()
    exercise_44()
    exercise_45()
    exercise_46()
    exercise_47()
    exercise_48()

# Funcția principală care afișează meniul și gestionează selecțiile utilizatorului
def main():
    """Main menu to select and run exercises."""
    # Buclă infinită pentru a menține meniul activ până când utilizatorul alege să iasă
    while True:
        # Afișează titlul meniului principal
        print("\n=== Python Tuple and Set Exercises ===")
        # Afișează opțiunile meniului
        print("1. Exercise 42: Display elements from a 5-element tuple")
        print("2. Exercise 43: Concatenate two tuples")
        print("3. Exercise 44: Check if an element is in a tuple")
        print("4. Exercise 45: Find index of an element in a tuple")
        print("5. Exercise 46: Extract a subtuple")
        print("6. Exercise 47: Remove duplicates from a list")
        print("7. Exercise 48: Find common elements in two sets")
        print("8. Run all exercises")
        print("0. Exit")
        
        # Citește opțiunea utilizatorului
        choice = input("\nEnter your choice (0-8): ")
        
        # Verifică opțiunea aleasă și execută acțiunea corespunzătoare
        if choice == '1':
            # Apelează funcția pentru exercițiul 42 dacă utilizatorul alege 1
            exercise_42()
        elif choice == '2':
            # Apelează funcția pentru exercițiul 43 dacă utilizatorul alege 2
            exercise_43()
        elif choice == '3':
            # Apelează funcția pentru exercițiul 44 dacă utilizatorul alege 3
            exercise_44()
        elif choice == '4':
            # Apelează funcția pentru exercițiul 45 dacă utilizatorul alege 4
            exercise_45()
        elif choice == '5':
            # Apelează funcția pentru exercițiul 46 dacă utilizatorul alege 5
            exercise_46()
        elif choice == '6':
            # Apelează funcția pentru exercițiul 47 dacă utilizatorul alege 6
            exercise_47()
        elif choice == '7':
            # Apelează funcția pentru exercițiul 48 dacă utilizatorul alege 7
            exercise_48()
        elif choice == '8':
            # Apelează funcția pentru a rula toate exercițiile dacă utilizatorul alege 8
            run_all_exercises()
        elif choice == '0':
            # Afișează mesaj de încheiere
            print("Exiting program. Goodbye!")
            # Iese din bucla while pentru a termina programul
            break
        else:
            # Afișează mesaj de eroare pentru opțiuni invalide
            print("Invalid choice. Please try again.")

# Verifică dacă scriptul este rulat direct (nu importat ca modul) și apelează funcția main() dacă este cazul
if __name__ == "__main__":
    main()
