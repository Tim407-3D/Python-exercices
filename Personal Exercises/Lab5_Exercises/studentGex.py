students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [60, 75, 70],
    "David": [95, 100,90]
}

def calculate_average(scores):
    total=0
    for score in scores:
        total += score
    return total / len(scores)

def get_letter_grade(avg):
    if avg>=90:
        return "A"
    elif avg<=89 and avg>=80:
        return "B"
    elif avg<=79 and avg>=70:
        return "C"
    elif avg<=69 and avg>=60:
        return "D"
    else:
        return "F"

def get_students_report(name,grades):
    avarage= calculate_average(grades)
    letter_grade= get_letter_grade(avarage)
    return f"{name}: {avarage} - {letter_grade}"

def class_average(students):
    total=0
    for student, scores in students.items():
        total += calculate_average(scores)
    return total / len(students)

def top_student(students):
    if len(students) == 0:
        return None
    top_student =0
    for student in students:
       top_student = max(top_student, calculate_average(students[student]))
    return top_student

def worst_students(students):
    if len(students) == 0:
        return None
        #It is passed to float('inf') to initialize a variable with positive infinity,
        #  typically for comparison purposes.
    worst = float('inf')
    for student, scores in students.items():
        student_avg = calculate_average(scores)
        if student_avg < worst:
            worst = student_avg
    return worst
       

def main():
    for student, scores in students.items():
        average = calculate_average(scores)
        grade = get_letter_grade(average)
       
        print(f"{student}: {average} - {grade}")
    top= top_student(students)
    for student, scores in students.items():
        if calculate_average(scores) == top:
            name = student
            break
    print(f"Top student: {name}")

    worst= worst_students(students)
    for student, scores in students.items():
        if calculate_average(scores) == worst:
            name = student
            break
    print(f"Worst student: {name}")
if __name__ == "__main__":
    main()
