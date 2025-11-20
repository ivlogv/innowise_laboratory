"""This module contains Student Grade Analyzer program"""

students = [
    {"name": None, "grades": []}
]


def add_student():
    """Add new user to dictionary"""


def add_grades(student_name: str):
    """
    Add grades list for specific student.
    Input numbers 0-100

    Args:
        student_name (str): Name of a student
    """
    return student_name


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
                    add_grades("test")
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
                    print("Invalid input. Please enter a number 1-5.")
        # Handle not numeric input
        except ValueError:
            print("Invalid input. Please enter a number.")
        # Handle program break (Ctrl+C)
        except KeyboardInterrupt:
            print("\nUser cancelled the program. Exiting program.")
            break


if __name__ == "__main__":
    main()
