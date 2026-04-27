# main.py - Entry point for the Exam Scheduling System

from data import get_courses, get_rooms, get_timeslots
from scheduler import create_schedule, print_schedule
from heuristic import score_schedule


def main():
    print("==============================")
    print("    Exam Scheduling System    ")
    print("==============================")

    # Step 1: Collect course details from the user
    courses = get_courses()

    if not courses:
        print("No courses entered. Exiting.")
        return

    # Step 2: Load hardcoded rooms and timeslots
    rooms = get_rooms()
    timeslots = get_timeslots()

    # Step 3: Build the schedule
    schedule = create_schedule(courses, rooms, timeslots)

    # Step 4: Print the timetable
    print_schedule(schedule)

    # Step 5: Score the schedule and display the result
    score = score_schedule(schedule)
    print(f"Schedule Score: {score}")
    print("(Lower score = better schedule)")


if __name__ == "__main__":
    main()
