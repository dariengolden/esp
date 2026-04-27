# data.py - Handles all input data collection and hardcoded system data

# Sample courses used for quick testing (type 'sample' at the first prompt)
sample_courses = [
    {
        "title": "Artificial Intelligence",
        "num_students": 30,
        "students": ["65001", "65002", "65003", "65004", "65005"],
        "duration": 2,
    },
    {
        "title": "Data Structures",
        "num_students": 20,
        "students": ["65006", "65007", "65002", "65008"],  # 65002 shared with AI
        "duration": 1,
    },
    {
        "title": "Database Systems",
        "num_students": 25,
        "students": ["65009", "65010", "65003", "65011"],  # 65003 shared with AI
        "duration": 2,
    },
    {
        "title": "Networks",
        "num_students": 15,
        "students": ["65012", "65013", "65014"],
        "duration": 1,
    },
]

# Hardcoded rooms available in the system
rooms = [
    {"name": "R101", "capacity": 40},
    {"name": "R102", "capacity": 30},
    {"name": "Lab1", "capacity": 25},
]

# Hardcoded timeslots available
timeslots = [
    {"day": 1, "slot": 1},
    {"day": 1, "slot": 2},
    {"day": 2, "slot": 1},
    {"day": 2, "slot": 2},
]


def get_courses():
    """Ask the user to enter course details. Returns a list of course dictionaries."""
    courses = []
    print("\n--- Enter Course Details ---")
    print("Type 'sample' to load test data, or type 'done' when finished.\n")

    while True:
        title = input("Course title (or 'sample' / 'done'): ").strip()

        # Load mock data for quick testing
        if title.lower() == "sample":
            print("  Loading sample courses...\n")
            return sample_courses

        if title.lower() == "done":
            break

        if not title:
            print("Course title cannot be empty. Please try again.")
            continue

        # Get number of students
        while True:
            try:
                num_students = int(input("Number of students: ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")

        # Get student IDs
        student_input = input("Student IDs (comma-separated, e.g. 65001,65002): ").strip()
        students = [s.strip() for s in student_input.split(",") if s.strip()]

        # Get exam duration
        while True:
            try:
                duration = int(input("Length of exam (in hours): ").strip())
                break
            except ValueError:
                print("Please enter a valid number.")

        course = {
            "title": title,
            "num_students": num_students,
            "students": students,
            "duration": duration,
        }
        courses.append(course)
        print(f"  Course '{title}' added.\n")

    return courses


def get_rooms():
    """Return the hardcoded list of rooms."""
    return rooms


def get_timeslots():
    """Return the hardcoded list of timeslots."""
    return timeslots
