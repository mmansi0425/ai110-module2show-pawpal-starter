"""Tests for the PawPal+ system."""

from datetime import date

from pawpal_system import Pet, Scheduler, Task


def test_mark_complete_changes_status():
    task = Task(name="Walk", duration=30, priority=1)
    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_increases_task_count():
    pet = Pet(name="Rex", species="dog")
    assert len(pet.tasks) == 0

    pet.add_task(Task(name="Feed", duration=10, priority=2))

    assert len(pet.tasks) == 1


def test_one_off_task_has_no_next_occurrence():
    task = Task(name="Vet Visit", duration=45, priority=1)

    next_task = task.mark_complete()

    assert next_task is None


def test_daily_task_repeats_one_day_later():
    task = Task(
        name="Walk",
        duration=30,
        priority=1,
        frequency="daily",
        due_date=date(2026, 7, 7),
    )

    next_task = task.mark_complete()

    assert next_task is not None
    assert next_task.due_date == date(2026, 7, 8)
    assert next_task.completed is False
    assert next_task.frequency == "daily"


def test_weekly_task_repeats_seven_days_later():
    task = Task(
        name="Bath",
        duration=20,
        priority=2,
        frequency="weekly",
        due_date=date(2026, 7, 7),
    )

    next_task = task.mark_complete()

    assert next_task.due_date == date(2026, 7, 14)


def test_complete_task_adds_next_occurrence_to_pet():
    pet = Pet(name="Luna", species="dog")
    walk = Task(
        name="Walk",
        duration=30,
        priority=1,
        frequency="daily",
        due_date=date(2026, 7, 7),
    )
    pet.add_task(walk)

    pet.complete_task(walk)

    assert len(pet.tasks) == 2
    assert pet.tasks[1].due_date == date(2026, 7, 8)


def test_find_conflicts_detects_same_start_time():
    scheduler = Scheduler()
    tasks = [
        Task(name="Walk", duration=30, priority=1, time="08:00"),
        Task(name="Play", duration=20, priority=2, time="08:00"),
    ]

    warnings = scheduler.find_conflicts(tasks)

    assert len(warnings) == 1
    assert "08:00" in warnings[0]


def test_find_conflicts_returns_empty_when_no_clash():
    scheduler = Scheduler()
    tasks = [
        Task(name="Walk", duration=30, priority=1, time="08:00"),
        Task(name="Feed", duration=10, priority=1, time="07:30"),
    ]

    warnings = scheduler.find_conflicts(tasks)

    assert warnings == []
