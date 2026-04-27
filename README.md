# Exam Scheduling Problem (ESP)

**Members:** Andrew and Darien

## Project Description

This is a beginner-friendly Python console program that automatically generates an exam timetable for university courses. The user enters course details, and the system assigns each exam to a suitable room and timeslot. A heuristic scoring function then evaluates the quality of the schedule — a lower score means a better schedule.

## Files

| File | Description |
|------|-------------|
| `main.py` | Entry point — runs the full program |
| `data.py` | Collects course input from the user; stores hardcoded rooms and timeslots |
| `scheduler.py` | Core scheduling logic — assigns rooms and timeslots to courses |
| `heuristic.py` | Scoring function — rates how good the final schedule is |
| `README.md` | This file |
| `report.md` | Written report about the project |

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal in the project folder.
3. Run the program:

```
python main.py
```

4. Follow the prompts to enter your course details. For example:

```
Course title: Artificial Intelligence
Number of students: 30
Student IDs: 65001,65002,65003
Length of exam (in hours): 2
```

5. Type `done` when you have finished entering courses.
6. The program will display the timetable and a final score.
