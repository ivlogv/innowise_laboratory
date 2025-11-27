"""This module contains Student Grade Analyzer program"""

students = []  # Empty list to store students data


def check_student_exist(name: str) -> bool:
    """
    Check students existence by given name.

    Args:
        name (str): Student name

    Returns:
        bool: True if student exists, False if not
    """
    return any(student["name"] == name for student in students)


def is_valid_student(s: dict) -> bool:
    """
    Check if student is valid dict with name and grades
    and grades are not empty list.

    Args:
        s (dict): Student data

    Returns:
        bool: True if student is valid, False otherwise
    """
    # Check all validation cases
    return (
        isinstance(s, dict)
        and "name" in s
        and "grades" in s
        and isinstance(s["grades"], list)
        and len(s["grades"]) > 0
    )


def validate_students() -> bool:
    """
    Validate if there are students in the list
    and students have grades.

    Returns:
        bool: True if there are students, False otherwise
    """
    # Check if there are students
    # If not, print message and return
    if not students:
        print("There are no students. Add students first.")
        return False

    # Filter students without grades
    valid_students = [s for s in students if is_valid_student(s)]
    if not valid_students:
        print("No grades available. Add grades first.")
        return False

    return True


def update_student_grades(name: str, grade: int) -> None:
    """
    Add new grade to a student's grades by given name.

    Args:
        name (str): Name of a student
        grade (int): Grade to add to list
    """
    # Find student by name
    student = next((s for s in students if s["name"] == name), None)
    if student:
        #  Add grade to students grades list
        student["grades"].append(grade)


def add_student() -> None:
    """Add new user to dictionary"""
    # Get student name
    name = str(input("Enter students name: "))
    # Add student to list if not exists
    if not check_student_exist(name):
        new_student = {"name": name, "grades": []}
        students.append(new_student)
    else:
        print("Student already exists.")


def add_grades() -> None:
    """
    Add grades list for concrete student.
    Input numbers 0-100
    """
    # Get student name
    name = str(input("Enter students name: "))
    if check_student_exist(name):
        # Input grades until 'done' is entered
        while True:
            grade_str = input("Enter a grade (or 'done' to finish): ")
            if grade_str.lower() == "done":
                break
            try:
                grade = int(grade_str)
                if 0 <= grade <= 100:
                    # Add grade to student's grades if valid range
                    update_student_grades(name, grade)
                else:
                    print("Invalid input. Please enter a number (0-100).")
            except ValueError:
                print("Invalid input. Please enter a number (0-100).")
    else:
        print("Student does not exist. Add the student first.")


def calculate_avg(grades: list[int]) -> float:
    """
    Calculate average grade from grades list.

    Args:
        grades (list[int]): List of grades

    Returns:
        float: Average grade
        None: If there are no grades
    """
    # Validate grades list by filtering non-numeric values
    numeric_grades = [g for g in grades if isinstance(g, (int, float))]
    # Return None if there are no numeric grades
    if not numeric_grades:
        return None
    # Handle potential ZeroDivisionError
    try:
        return sum(numeric_grades) / len(numeric_grades)
    except ZeroDivisionError:
        print("There are no grades. Add grades first.")


def show_report() -> None:
    """Get a list of each student's average grade."""
    #  Validate if there are students with grades
    if not validate_students():
        return

    avg_grades = []
    # Calculate average grade for each student
    # and print it, N/A if no grades
    for student in students:
        # Validate student data
        if not is_valid_student(student):
            print("Student's data is invalid, skipping.")
            continue
        # If valid, calculate average grade
        avg_num = calculate_avg(student["grades"])
        avg = str(round(avg_num, 1)) if avg_num is not None else "N/A"
        avg_grades.append(avg_num)
        print(f"{student['name']}'s average grade is {avg}.")
    # Calculate and print max, min, overall average
    valid_avg_grades = [avg for avg in avg_grades if avg is not None]
    if valid_avg_grades:
        print(f"Max Average: {round(max(valid_avg_grades), 1)}.")
        print(f"Min Average: {round(min(valid_avg_grades), 1)}.")
        print(
            "Overall Average: " +
            f"{round(sum(valid_avg_grades) / len(valid_avg_grades), 1)}."
        )
    else:
        print("There are no grades. Add grades first.")


def find_top_performer():
    """Find the student with the highest average grade."""
    #  Validate if there are students with grades
    if not validate_students():
        return
    # Filter students with invalid data
    valid_students = [s for s in students if is_valid_student(s)]
    if not valid_students:
        print("No valid student data found.")
        return

    # Find the student with the highest average grade
    top_performer = max(
        valid_students,
        key=lambda s: calculate_avg(s["grades"]) or -1
    )
    # Calculate top performer's average grade
    top_avg = calculate_avg(top_performer["grades"])
    if top_avg is not None:
        print(
            "The student with the highest average is",
            f"{top_performer["name"]} with a grade of {round(top_avg, 1)}.",
        )
    else:
        print(f"{top_performer['name']} has no grades yet.")


def main():
    """Main logic of Student Grade Analyzer, lecture 3"""
    # Main loop
    while True:
        print()
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
                    add_student()
                case 2:
                    add_grades()
                case 3:
                    show_report()
                case 4:
                    find_top_performer()
                case 5:
                    break
                case _:
                    print("Invalid input. Please enter a correct number.")
        # Handle not numeric input
        except ValueError:
            print("Invalid input. Please enter a number.")
        # Handle program break (Ctrl+C)
        except KeyboardInterrupt:
            print("\nUser cancelled the program. Exiting program.")
            break


if __name__ == "__main__":
    main()
