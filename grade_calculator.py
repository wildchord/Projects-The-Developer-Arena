# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
#Author - Aishni Rathore

def calculate_grade(average):
    """Calculate grade and comment based on average marks."""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from your teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within the specified range."""
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"Please enter a number between {min_val} and {max_val}. - grade_calculator.py:25")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a whole number or decimal. - grade_calculator.py:29")


def get_positive_int(prompt):
    """Get a positive integer value."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive number! - grade_calculator.py:38")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a whole number. - grade_calculator.py:42")


def main():
    print("= - grade_calculator.py:46" * 50)
    print("STUDENT GRADE CALCULATOR - grade_calculator.py:47")
    print("= - grade_calculator.py:48" * 50)
    print()

    num_students = get_positive_int("Enter number of students: ")

    student_names = []
    student_marks = []
    student_results = []

    for i in range(num_students):
        print(f"\n=== STUDENT {i + 1} === - grade_calculator.py:58")

        name = input("Student name: ").strip()
        while not name:
            print("Name cannot be empty! - grade_calculator.py:62")
            name = input("Student name: ").strip()
        student_names.append(name)

        print("Enter marks (0100): - grade_calculator.py:66")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        student_marks.append([math, science, english])

        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_results.append({
            'average': average,
            'grade': grade,
            'comment': comment
        })

    print("\n - grade_calculator.py:82" + "=" * 50)
    print("RESULTS SUMMARY - grade_calculator.py:83")
    print("= - grade_calculator.py:84" * 50)
    print(f"{'Name':20} | {'Avg':>5} | {'Grade':^5} | Comment - grade_calculator.py:85")
    print("" * 70)

    for i in range(num_students):
        name = student_names[i]
        avg = student_results[i]['average']
        grade = student_results[i]['grade']
        comment = student_results[i]['comment']
        print(f"{name:20} | {avg:5.1f} | {grade:^5} | {comment} - grade_calculator.py:93")

    if num_students > 0:
        averages = [result['average'] for result in student_results]
        class_avg = sum(averages) / len(averages)
        max_avg = max(averages)
        min_avg = min(averages)
        max_index = averages.index(max_avg)
        min_index = averages.index(min_avg)

        print("\n - grade_calculator.py:103" + "=" * 50)
        print("CLASS STATISTICS - grade_calculator.py:104")
        print("= - grade_calculator.py:105" * 50)
        print(f"Total Students: {num_students} - grade_calculator.py:106")
        print(f"Class Average: {class_avg:.1f} - grade_calculator.py:107")
        print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]}) - grade_calculator.py:108")
        print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]}) - grade_calculator.py:109")

    print("\n - grade_calculator.py:111" + "=" * 50)
    print("Thank you for using the Grade Calculator! - grade_calculator.py:112")
    print("= - grade_calculator.py:113" * 50)


if __name__ == "__main__":
    main()
