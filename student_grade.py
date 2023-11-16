# Function to calculate the weighted average for a student
def calculate_weighted_average(student):
    assignment_weight = 0.1
    theory_test_weight = 0.5
    lab_test_weight = 0.3
    mini_project_weight = 0.1

    assignment_score = sum(student['assignment'])
    theory_test_score = sum(student['theory_test']) / len(student['theory_test'])
    lab_test_score = sum(student['lab_test']) / len(student['lab_test'])
    mini_project_score = student['mini_project']

    weighted_average = (
        assignment_score * assignment_weight +
        theory_test_score * theory_test_weight +
        lab_test_score * lab_test_weight +
        mini_project_score * mini_project_weight
    )

    return weighted_average

# Function to determine the grade based on the calculated average
def determine_grade(average):
    if average >= 90:
        return 'S'
    elif average >= 80:
        return 'A'
    elif average >= 70:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 50:
        return 'D'
    elif average >= 35:
        return 'E'
    else:
        return 'F'

# Input for 5 students
students = []

for _ in range(5):
    student_data = {
        'name': input("Enter student name: "),
        'assignment': list(map(float, input("Enter assignment scores (comma-separated): ").split(','))),
        'theory_test': list(map(float, input("Enter theory test scores (comma-separated): ").split(','))),
        'lab_test': list(map(float, input("Enter lab test scores (comma-separated): ").split(','))),
        'mini_project': float(input("Enter mini project score: "))
    }

    students.append(student_data)

# Calculate class average and average grade
total_weighted_average = sum(calculate_weighted_average(student) for student in students)
class_average = total_weighted_average / len(students)

class_grade = determine_grade(class_average)

print(f"\nClass Average: {class_average:.2f}")
print(f"Average Grade: {class_grade}")