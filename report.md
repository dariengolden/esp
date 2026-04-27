# Exam Scheduling Problem — Project Report

**Members:** Andrew and Darien

---

## Problem Overview

The Exam Scheduling Problem (ESP) is a common challenge universities face every semester. The goal is to assign exams to timeslots and rooms in a way that avoids conflicts and makes the best use of available resources. Students should not have two exams at the same time, rooms should not be double-booked, and rooms should be large enough to seat all students taking the exam.

---

## Inputs

The system collects the following details from the user for each course:

| Input | Example |
|-------|---------|
| Course title | Artificial Intelligence |
| Number of students | 30 |
| Student IDs | 65001, 65002, 65003 |
| Exam duration (hours) | 2 |

Rooms and timeslots are hardcoded in the system:

**Rooms:** R101 (40 seats), R102 (30 seats), Lab1 (25 seats)

**Timeslots:** Day 1 Slot 1, Day 1 Slot 2, Day 2 Slot 1, Day 2 Slot 2

---

## Constraints

- A room must be large enough to fit all students enrolled in the course.
- A room cannot be booked for two exams at the same time.
- A student cannot have two exams scheduled at the same time (hard conflict).
- The scheduler tries to avoid placing too many exams on the same day for one student.

---

## Heuristic Used

After scheduling, the quality of the timetable is measured using this scoring formula:

```
score = 1000H + 10O + 5C + 1000R + 2W
```

| Variable | Meaning |
|----------|---------|
| H | Hard conflicts — a student has 2 exams at the same day and slot |
| O | Overload — a student has more than 2 exams on the same day |
| C | Consecutive exams — a student has back-to-back slots on the same day |
| R | Room capacity issue — the room is too small for the course |
| W | Room wastage — unused seats in the assigned room |

A lower score means a better schedule. Hard conflicts and room capacity issues are weighted highest (1000) because they are unacceptable in a real timetable.

---

## Team Work Division

| Member | Responsibilities |
|--------|-----------------|
| Andrew | `heuristic.py`, `README.md`, `report.md` |
| Darien | `data.py`, `scheduler.py`, `main.py` connections |

---

## Expected Output

```
========== EXAM TIMETABLE ==========

Course: Artificial Intelligence
Room: R101
Day: 1
Slot: 1
Duration: 2 hour(s)

Course: Data Structures
Room: R102
Day: 1
Slot: 2
Duration: 1 hour(s)

=====================================
Schedule Score: 10
(Lower score = better schedule)
```
