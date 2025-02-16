def ex1(a, b):
    """Exercise 1: Display quotient and remainder of division"""
    if b == 0:
        return "Nu se poate împărți la zero!"
    return f"Catul: {a // b}, Restul: {a % b}"

def ex2(a, b):
    """Exercise 2: Display numbers raised to power"""
    return f"{a} la puterea {b} = {a ** b}\n{b} la puterea {a} = {b ** a}"

def ex3(a, b):
    """Exercise 3: Check if second number is divisible by first"""
    if a == 0:
        return "Nu se poate împărți la zero!"
    return f"{b} {'este' if b % a == 0 else 'nu este'} divizibil cu {a}"

def ex4(num):
    """Exercise 4: Check if number is even or odd"""
    return "par" if num % 2 == 0 else "impar"

def ex5(num):
    """Exercise 5: Check if number is in range 100-150"""
    return 100 <= num <= 150

def ex6(num):
    """Exercise 6: Check if number is < 50 or > 100"""
    return num < 50 or num > 100

def ex7(a, b):
    """Exercise 7: Determine and display number types"""
    return f"Primul numar este {type(a).__name__}\nAl doilea numar este {type(b).__name__}"

def ex8(a, b):
    """Exercise 8: Determine which number is larger"""
    if a == b:
        return "Numerele sunt egale"
    return f"{'Primul' if a > b else 'Al doilea'} numar este mai mare"

def ex9(str1, str2):
    """Exercise 9: Check if first string is in second string"""
    return f"'{str1}' {'se regăsește' if str1 in str2 else 'nu se regăsește'} în '{str2}'"

def ex10():
    """Exercise 10: Extract word 'pere' from string"""
    text = "Ana are 10 mere si 5 pere."
    return text.split()[-1].rstrip('.')

def ex11(numbers_str, search_num):
    """Exercise 11: Check if number is in comma-separated list"""
    numbers = [int(x.strip()) for x in numbers_str.split(',')]
    return search_num in numbers

def ex12(a, b):
    """Exercise 12: Find smaller number and check if even"""
    smaller = min(a, b)
    return f"Numărul mai mic este {smaller}" + (f" și este par" if smaller % 2 == 0 else "")

def ex13(num):
    """Exercise 13: Check if number is divisible by 3 or 5"""
    if num % 3 == 0 and num % 5 == 0:
        return "Numărul este divizibil cu 3 și cu 5"
    elif num % 3 == 0:
        return "Numărul este divizibil cu 3"
    elif num % 5 == 0:
        return "Numărul este divizibil cu 5"
    return "Numărul nu este divizibil nici cu 3, nici cu 5"

def ex14(num):
    """Exercise 14: FizzBuzz"""
    if num % 3 == 0 and num % 5 == 0:
        return "fizzbuzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
    return str(num)

def ex15():
    """Exercise 15: Extract name and surname from string"""
    text = "Nume: Voicu, Prenume: Librimir"
    nume = text.split('Nume: ')[1].split(',')[0]
    prenume = text.split('Prenume: ')[1]
    return f"Nume: {nume}, Prenume: {prenume}"

def ex16():
    """Exercise 16: Count occurrences of 'pere'"""
    text = "mere, pere, mere, mere, pere, struguri"
    return text.count('pere')

def ex17():
    """Exercise 17: Remove word 'intergalactic' from string"""
    text = "Ana are 10 mingi de fotbal intergalactic"
    return text.replace(" intergalactic", "")

def verify_password(password):
    """Exercise 18: Verify password requirements"""
    errors = []
    
    if len(password) < 10:
        errors.append("Parola trebuie să aibă cel puțin 10 caractere")
    if ' ' in password:
        errors.append("Parola nu trebuie să conțină spații")
    
    if errors:
        print("Status: INCORECT")
        print("Erori găsite:")
        for error in errors:
            print(f"- {error}")
    else:
        print("Status: CORECT")
        print("Parola îndeplinește toate cerințele:")
        print("- Are cel puțin 10 caractere")
        print("- Nu conține spații")
    
    return None

# Test functions
if __name__ == "__main__":
    print("Testing exercise solutions:")
    
    # Example usage of each function
    print("\nEx1:", ex1(10, 3))
    print("Ex2:", ex2(2, 3))
    print("Ex3:", ex3(3, 9))
    print("Ex4:", ex4(7))
    print("Ex5:", ex5(125))
    print("Ex6:", ex6(75))
    print("Ex7:", ex7(5, 5.5))
    print("Ex8:", ex8(10, 20))
    print("Ex9:", ex9("Ana", "Ana are mere"))
    print("Ex10:", ex10())
    print("Ex11:", ex11("1, 2, 3, 4, 5", 3))
    print("Ex12:", ex12(7, 4))
    print("Ex13:", ex13(15))
    print("Ex14:", ex14(15))
    print("Ex15:", ex15())
    print("Ex16:", ex16())
    print("Ex17:", ex17())
    
    # Test password verification with different passwords
    print("\nTesting password verification:")
    print("\nTest 1 - Parola scurtă:")
    verify_password("scurt")
    
    print("\nTest 2 - Parola cu spații:")
    verify_password("parola cu spatii")
    
    print("\nTest 3 - Parola corectă:")
    verify_password("ParolaCorecta123")