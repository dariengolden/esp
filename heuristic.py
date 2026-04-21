# Heuristic scoring function for exam schedules
# Beginner-friendly style with simple loops and clear comments

def score_schedule(schedule):
	"""
	Score a schedule. Lower score is better.

	Expected schedule format (simple list of dicts):
	Each exam is a dictionary with keys:
	  - course
	  - day
	  - slot
	  - room
	  - students (list of student IDs)
	  - room_capacity (int)
	"""

	hard_conflicts = 0
	same_day_overload = 0
	consecutive_exams = 0
	room_capacity_issues = 0
	room_wastage = 0

	# Track where each student has exams
	# student_exams[student_id] = list of (day, slot)
	student_exams = {}

	for exam in schedule:
		students = exam.get("students", [])
		day = exam.get("day")
		slot = exam.get("slot")
		room_capacity = exam.get("room_capacity", 0)

		# Room capacity problems
		if len(students) > room_capacity:
			room_capacity_issues += 1

		# Room wastage (empty seats)
		if room_capacity > len(students):
			room_wastage += (room_capacity - len(students))

		# Collect exams per student
		for student in students:
			if student not in student_exams:
				student_exams[student] = []
			student_exams[student].append((day, slot))

	# Check conflicts, same-day overload, and consecutive exams
	for student, exams in student_exams.items():
		# Count how many exams happen on each day
		exams_by_day = {}
		for day, slot in exams:
			if day not in exams_by_day:
				exams_by_day[day] = []
			exams_by_day[day].append(slot)

		# Hard conflicts: same day and same slot for the same student
		for day, slots in exams_by_day.items():
			seen_slots = set()
			for s in slots:
				if s in seen_slots:
					hard_conflicts += 1
				else:
					seen_slots.add(s)

		# Same-day overload: more than 2 exams in one day
		for day, slots in exams_by_day.items():
			if len(slots) > 2:
				same_day_overload += (len(slots) - 2)

		# Consecutive exams: adjacent slots on same day
		for day, slots in exams_by_day.items():
			unique_slots = sorted(list(set(slots)))
			for i in range(len(unique_slots) - 1):
				if unique_slots[i + 1] - unique_slots[i] == 1:
					consecutive_exams += 1

	# Final weighted score
	score = (
		1000 * hard_conflicts +
		10 * same_day_overload +
		5 * consecutive_exams +
		1000 * room_capacity_issues +
		2 * room_wastage
	)

	return score