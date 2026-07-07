"""Tests for the PawPal+ system."""

from pawpal_system import Pet, Task


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
