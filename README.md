# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:
## 🖥️ Sample Output

```text
Today's Schedule
-------------------------
- Feed Breakfast at 07:30 (10 min, Priority 1)
- Morning Walk at 08:00 (30 min, Priority 1)
- Brush Fur at 09:15 (15 min, Priority 2)

Luna's Tasks
-------------------------
- Morning Walk at 08:00
- Feed Breakfast at 07:30

Schedule Conflicts
-------------------------
- Conflict: 'Morning Walk' and 'Play Time' are both scheduled at 08:00.
```

## 🧪 Testing PawPal+

```bash
python3 -m pytest
pytest

# Run with coverage:
The automated tests verify:

- Task completion updates the task status correctly.
- Adding a task increases a pet's task count.
- Tasks are sorted in chronological order.
- Tasks can be filtered by pet name and completion status.
- The scheduler respects the available time limit.
- Conflict detection identifies tasks scheduled at the same time.
- Recurring task behavior.
- Edge cases such as empty task lists and exact time boundaries.
```
# Paste your pytest output here
```text
==================== test session starts =====================
platform darwin -- Python 3.14.0, pytest-9.1.0, pluggy-1.6.0
rootdir: /Users/mansimohanraj/ai110-module2show-pawpal-starter
plugins: anyio-4.14.0
collected 11 items

tests/test_pawpal.py ...........                       [100%]

===================== 11 passed in 0.01s =====================

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature |.             Method(s)                              | Notes |                                    
---------------------------------------------------------------------------------------- |
| Task sorting      | `Scheduler.sort_by_time()`    | Sorts tasks by scheduled start time in chronological order.                              |
| Filtering         | `Scheduler.filter_tasks_by()` | Filters tasks by pet name or completion status.                                          |
| Conflict handling | `Scheduler.find_conflicts()`  | Detects tasks with the same scheduled start time and returns warning messages.           |
| Recurring tasks   | `Task.mark_complete()`        | Automatically creates the next daily or weekly task after a recurring task is completed. |


## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
