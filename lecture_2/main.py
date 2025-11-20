def generate_profile(age: int) -> str:
    """
    This function generates users life stage based on current age.

    Args:
        age (int) : Users current age

    Returns:
        str : User's life stage (Child, Teenager, Adult)
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def get_hobbies() -> list:
    """
    Get a list of user's favorite hobbies.

    Returns:
        list: List of user hobbies.
    """
    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

        if hobby.lower() != "stop" and hobby != "":
            hobbies.append(hobby)
        else:
            break

    return hobbies


def create_user_profile(name: str, age: int, hobbies: list) -> dict:
    """
    Create a user profile dictionary with all required information.

    Args:
        name (str): User's name
        age (int): User's age
        hobbies (list): List of user's hobbies

    Returns:
        dict: Complete user profile
    """
    life_stage = generate_profile(age)

    return {
        "name": name.strip(),
        "age": age,
        "stage": life_stage,
        "hobbies": hobbies,
    }


def display_profile_summary(user_profile: dict):
    """
    Display user profile summary.

    Args:
        user_profile (dict): User profile info
    """
    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile["name"]}")
    print(f"Age: {user_profile["age"]}")
    print(f"Life Stage: {user_profile["stage"]}")
    if len(user_profile["hobbies"]) == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile["hobbies"])})")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")
    print("---")
    return


def main():
    """Main logic of lecture_2"""
    # Display greeting message
    print("-" * 47)
    print("| Welcome to the Mini User Profile Generator! |")
    print("-" * 47)

    # Get input data from user
    user_name = str(input("Enter your full name: "))
    birth_year_str = str(input("Enter your birth year: "))
    birth_year = int(birth_year_str)

    # Calculate the user's current age
    current_age = 2025 - birth_year

    # Get a list of hobbies from user
    hobbies = get_hobbies()

    # Create user_profile dictionary
    user_profile = create_user_profile(user_name, current_age, hobbies)

    # Display profile summary
    display_profile_summary(user_profile)


if __name__ == "__main__":
    main()
