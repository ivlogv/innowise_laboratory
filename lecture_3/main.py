"""This module contains Student Grade Analyzer program"""

students = [] # Empty list to store students data


def check_student_exist(name: str):
    """
    Check student's name in students list

    Args:
        name (str): Student name

    Returns:
        bool: Student existance    
    """
    if any(student["name"] == name for student in students.copy()):
        print("Student already exists.")
        return True
    return False


def update_student_grades(name: str, grade: int):
    """
    Add new grade to a student's grades by given name.
    
    Args:
        name (str): Name of a student
        grade (int): Grade to add to list
    """
    for student in students:
        if student["name"] == name:
            student["grades"].append(grade)


def add_student():
    """Add new user to dictionary"""
    name = str(input("Enter studens name: "))
    if not check_student_exist(name):
        new_student = {
            "name": name,
            "grades": []
        }
        students.append(new_student)


def add_grades():
    """
    Add grades list for specific student.
    Input numbers 0-100
    """
    name = str(input("Enter studens name: "))
    if check_student_exist(name):
        # ask for grades
        while True:
            grade_str = input("Enter a grade (or 'done' to finish):")
            if grade_str.lower() == "done":
                break
            try:
                grade = int(grade_str)
                if 0 <= grade <=100:
                    update_student_grades(name, grade)
                else:
                    print("Invalid input. Please enter a number (0-100).")
            except ValueError:
                print("Invalid input. Please enter a number (0-100).")



def show_report():
    """Get a list of each student's average grade."""


def find_top_performer():
    """Find the student with the highest average grade."""


def main():
    """Main logic of Studeent Grade Analyzer, lecture 3"""
    # Main loop
    while True:
        print("--- Student Grade Analyzer ---")
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")
        print("-" * 30)
        print(students)

        # Handle potential input errors
        try:
            choice = int(input("Enter your choice: "))

            # Switch between menu numbers
            match choice:
                case 1:
                    print("add new student")
                    add_student()
                case 2:
                    print("add grades for a student")
                    add_grades()
                case 3:
                    print("show report")
                    show_report()
                case 4:
                    print("find top performer")
                    find_top_performer()
                case 5:
                    print("Exiting program.")
                    break
                case _:
                    print("Invalid input. Please enter a correct number (1-5).")
        # Handle not numeric input
        except ValueError:
            print("Invalid input. Please enter a number.")
        # Handle program break (Ctrl+C)
        except KeyboardInterrupt:
            print("\nUser cancelled the program. Exiting program.")
            break


if __name__ == "__main__":
    main()
