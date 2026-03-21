# Student Grade Tracker

# Initial dictionary with students and their grades
students = {
    "Ana": [8, 9, 10],
    "Mihai": [7, 6, 8],
    "Elena": [10, 10, 9]
}

def calculate_average(grades):
    """Calculate average grade for a list of grades"""
    return sum(grades) / len(grades)

def print_all_averages():
    """Print each student's average grade"""
    print("=== Student Averages ===")
    for name, grades in students.items():
        average = calculate_average(grades)
        print(f"{name}: {average:.2f}")

def find_highest_average():
    """Find and return the student with highest average"""
    highest_avg = 0
    best_student = ""
    
    for name, grades in students.items():
        average = calculate_average(grades)
        if average > highest_avg:
            highest_avg = average
            best_student = name
    
    return best_student, highest_avg

def count_passed_students():
    """Count students with average >= 6"""
    passed_count = 0
    for name, grades in students.items():
        average = calculate_average(grades)
        if average >= 6:
            passed_count += 1
    return passed_count

def add_new_student():
    """Add a new student with grades"""
    name = input("Enter student name: ")
    grades_input = input("Enter grades separated by spaces: ")
    grades = [int(g) for g in grades_input.split()]
    students[name] = grades
    print(f"Added {name} with grades {grades}")

def show_student_grades():
    """Show grades for a specific student"""
    name = input("Enter student name: ")
    if name in students:
        print(f"{name}'s grades: {students[name]}")
        print(f"Average: {calculate_average(students[name]):.2f}")
    else:
        print(f"Student {name} not found!")

# Main program
def main():
    while True:
        print("\n=== Student Grade Tracker Menu ===")
        print("1. Show all averages")
        print("2. Show student with highest average")
        print("3. Count passed students (>= 6)")
        print("4. Add new student")
        print("5. Show specific student grades")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print_all_averages()
        elif choice == "2":
            best_student, avg = find_highest_average()
            print(f"Highest average: {best_student} with {avg:.2f}")
        elif choice == "3":
            passed = count_passed_students()
            print(f"Students passed: {passed} out of {len(students)}")
        elif choice == "4":
            add_new_student()
        elif choice == "5":
            show_student_grades()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main program
if __name__ == "__main__":
    main()