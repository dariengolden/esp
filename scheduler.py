# scheduler.py - Core scheduling logic for the Exam Scheduling System


def room_available(room_name, day, slot, schedule):
    """
    Check if a room is free for a given day and slot.
    Returns True if available, False if already booked.
    """
    for exam in schedule:
        if exam["room"] == room_name and exam["day"] == day and exam["slot"] == slot:
            return False
    return True


def has_student_conflict(students, day, slot, schedule):
    """
    Check if any of the given students already have an exam at this day and slot.
    Returns True if there is a conflict, False if it is safe to schedule.
    """
    for exam in schedule:
        if exam["day"] == day and exam["slot"] == slot:
            for student in students:
                if student in exam["students"]:
                    return True
    return False


def create_schedule(courses, rooms, timeslots):
    """
    Try to assign each course a room and timeslot.
    Checks room capacity, room availability, and student conflicts.
    Returns a list of scheduled exam dictionaries.
    """
    schedule = []
    unscheduled = []

    for course in courses:
        assigned = False

        # Try each timeslot until one works
        for timeslot in timeslots:
            day = timeslot["day"]
            slot = timeslot["slot"]

            # Try each room until one works
            for room in rooms:
                # Skip if room is too small for the number of students
                if room["capacity"] < course["num_students"]:
                    continue

                # Skip if room is already booked at this time
                if not room_available(room["name"], day, slot, schedule):
                    continue

                # Skip if any student already has an exam at this time
                if has_student_conflict(course["students"], day, slot, schedule):
                    continue

                # All checks passed - assign the exam
                exam = {
                    "course": course["title"],
                    "room": room["name"],
                    "room_capacity": room["capacity"],
                    "day": day,
                    "slot": slot,
                    "duration": course["duration"],
                    "students": course["students"],
                }
                schedule.append(exam)
                assigned = True
                break  # Stop looking at rooms

            if assigned:
                break  # Stop looking at timeslots

        if not assigned:
            unscheduled.append(course["title"])

    # Warn the user if any courses could not be scheduled
    if unscheduled:
        print("\nWARNING: The following courses could not be scheduled:")
        for title in unscheduled:
            print(f"  - {title}")

    return schedule


def print_schedule(schedule):
    """Print the full exam timetable in a readable format."""
    print("\n========== EXAM TIMETABLE ==========")

    if not schedule:
        print("No exams were scheduled.")
        return

    for exam in schedule:
        print(f"\nCourse: {exam['course']}")
        print(f"Room: {exam['room']}")
        print(f"Day: {exam['day']}")
        print(f"Slot: {exam['slot']}")
        print(f"Duration: {exam['duration']} hour(s)")

    print("\n=====================================")
