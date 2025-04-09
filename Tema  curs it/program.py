import csv
import json
import os
import statistics

# Definim calea absolută către directorul de bază al proiectului
base_path = r'D:\ITSCHOOL PYTHON\school\high_school'
class_a_path = os.path.join(base_path, 'classA')
class_b_path = os.path.join(base_path, 'classB')
output_path = os.path.join(base_path, 'output')

# Creăm directorul pentru output dacă nu există
os.makedirs(output_path, exist_ok=True)

# Funcție pentru a încărca datele din fișierele CSV (ClassA - Filologie)
def load_csv_data(file_name):
    file_path = os.path.join(class_a_path, file_name)
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Funcție pentru a încărca datele din fișierele JSON (ClassB - Mate-Info)
def load_json_data(file_name):
    file_path = os.path.join(class_b_path, file_name)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Funcție pentru a salva datele în format JSON
def save_to_json(data, file_name):
    file_path = os.path.join(output_path, file_name)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

try:
    # Încărcare date pentru ClassA (Filologie)
    class_a_data = {
        '9': load_csv_data('9_grade.csv'),
        '10': load_csv_data('10_grade.csv'),
        '11': load_csv_data('11_grade.csv'),
        '12': load_csv_data('12_grade.csv')
    }

    # Încărcare date pentru ClassB (Mate-Info)
    class_b_data = {
        '9': load_json_data('9_grade.json'),
        '10': load_json_data('10_grade.json'),
        '11': load_json_data('11_grade.json'),
        '12': load_json_data('12_grade.json')
    }

    # Cerința 1: Elevii din clasele de Filologie (ClassA) cu nota peste 90 la Istorie
    print("1) Elevii din clasele de Filologie cu nota peste 90 la Istorie:")
    for grade, students in class_a_data.items():
        for student in students:
            history_grade = float(student['History'])
            if history_grade > 90:
                print(f"Clasa {grade}: {student['Name']} - Nota la Istorie: {history_grade}")
    print()

    # Cerința 2: Elevii din clasele de Mate-Info (ClassB) cu media mai mică decât 80
    print("2) Elevii din clasele de Mate-Info cu media generală mai mică decât 80:")
    for grade, students in class_b_data.items():
        for student in students:
            grades = student['grades']
            average = (float(grades['math']) + float(grades['english']) + float(grades['science'])) / 3
            if average < 80:
                print(f"Clasa {grade}: {student['name']} - Media: {average:.2f}")
    print()

    # Cerința 3: Media generală a tuturor claselor de Filologie
    print("3) Media generală a claselor de Filologie:")
    filology_class_averages = {}
    for grade, students in class_a_data.items():
        total_grades = []
        for student in students:
            student_avg = (float(student['Geography']) + float(student['English']) + float(student['History'])) / 3
            total_grades.append(student_avg)
        class_avg = statistics.mean(total_grades)
        filology_class_averages[grade] = class_avg
        print(f"Clasa {grade}: {class_avg:.2f}")

    overall_filology_avg = statistics.mean(filology_class_averages.values())
    print(f"Media generală a tuturor claselor de Filologie: {overall_filology_avg:.2f}")
    print()

    # Cerința 4: Clasele de Mate-Info în ordine crescătoare a mediei generale
    print("4) Clasele de Mate-Info în ordine crescătoare a mediei generale:")
    math_info_class_averages = {}
    for grade, students in class_b_data.items():
        total_grades = []
        for student in students:
            grades = student['grades']
            student_avg = (float(grades['math']) + float(grades['english']) + float(grades['science'])) / 3
            total_grades.append(student_avg)
        class_avg = statistics.mean(total_grades)
        math_info_class_averages[grade] = class_avg

    sorted_math_info_classes = sorted(math_info_class_averages.items(), key=lambda x: x[1])
    for grade, avg in sorted_math_info_classes:
        print(f"Clasa {grade}: {avg:.2f}")
    print()

    # Cerința 5: Conversia fișierelor CSV pentru clasele de Filologie în fișiere JSON
    print("5) Conversia fișierelor CSV pentru clasele de Filologie în fișiere JSON")
    for grade, students in class_a_data.items():
        json_data = []
        for student in students:
            json_student = {
                "name": student['Name'],
                "grades": {
                    "geography": float(student['Geography']),
                    "english": float(student['English']),
                    "history": float(student['History'])
                }
            }
            json_data.append(json_student)
        
        output_file = f"{grade}_grade_filology.json"
        save_to_json(json_data, output_file)
        print(f"Fișierul {output_file} a fost creat în {output_path}")

except FileNotFoundError as e:
    print(f"Eroare: {e}")
    print("\nVerificați dacă structura directoarelor este corectă:")
    print(f"ClassA path: {class_a_path}")
    print(f"ClassB path: {class_b_path}")
    print("\nListare directoare existente:")
    
    # Afișăm conținutul directorului de bază pentru a verifica structura
    if os.path.exists(base_path):
        print(f"Conținutul directorului {base_path}:")
        for item in os.listdir(base_path):
            print(f" - {item}")
    else:
        print(f"Directorul de bază {base_path} nu există!")