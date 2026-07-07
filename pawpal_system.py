"""PawPal+ system classes.

Implements the pet care scheduling logic based on the UML design in
diagrams/uml.mmd.
"""

from dataclasses import dataclass, field
from datetime import date, timedelta


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    time: str = "00:00"  # start time in "HH:MM" 24-hour format
    completed: bool = False
    frequency: str = "none"  # how often the task repeats: "none", "daily", "weekly"
    due_date: date | None = None  # the day this task is due, or None if not set

    def mark_complete(self) -> "Task | None":
        """Mark this task as completed.

        If the task repeats ("daily" or "weekly"), build and return the next
        occurrence. Otherwise return None because there is nothing to repeat.
        """
        self.completed = True

        # A one-off task has no next occurrence.
        if self.frequency == "none":
            return None

        # Figure out how many days until the task should happen again.
        if self.frequency == "daily":
            gap = timedelta(days=1)
        elif self.frequency == "weekly":
            gap = timedelta(days=7)
        else:
            # Unknown frequency, so treat it like a one-off task.
            return None

        # Work out the next due date. If this task never had one, start today.
        current_due = self.due_date if self.due_date is not None else date.today()
        next_due = current_due + gap

        # Create the next occurrence as a fresh, not-yet-completed task.
        return Task(
            name=self.name,
            duration=self.duration,
            priority=self.priority,
            time=self.time,
            completed=False,
            frequency=self.frequency,
            due_date=next_due,
        )


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)

    def complete_task(self, task: Task) -> Task | None:
        """Mark one of this pet's tasks complete and schedule its next repeat.

        If the task recurs, the next occurrence is added to this pet's list
        automatically. Returns that new task, or None if it does not repeat.
        """
        next_task = task.mark_complete()
        if next_task is not None:
            self.add_task(next_task)
        return next_task


@dataclass
class Owner:
    name: str
    email: str
    available_minutes: int
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner's list of pets."""
        self.pets.append(pet)

    def get_all_tasks(self) -> list[Task]:
        """Return all incomplete tasks across every pet owned."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                if not task.completed:
                    all_tasks.append(task)
        return all_tasks


class Scheduler:
    def generate_plan(self, owner: Owner) -> list[Task]:
        """Build a prioritized task plan that fits the owner's available time."""
        tasks = owner.get_all_tasks()
        sorted_tasks = self.sort_tasks(tasks)
        return self.filter_tasks(sorted_tasks, owner.available_minutes)

    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        """Return tasks ordered by priority, highest priority first."""
        # Put the most important tasks first (priority 1 is highest).
        return sorted(tasks, key=lambda task: task.priority)

    def sort_by_time(self, tasks: list[Task]) -> list[Task]:
        """Return tasks ordered by start time, earliest first."""
        # "HH:MM" strings sort in the correct order as plain text,
        # because the hours come first and every value is zero-padded.
        return sorted(tasks, key=lambda task: task.time)

    def filter_tasks_by(
        self,
        owner: Owner,
        pet_name: str | None = None,
        completed: bool | None = None,
    ) -> list[Task]:
        """Return the owner's tasks, optionally filtered by pet and/or status.

        - pet_name: only tasks belonging to the pet with this name.
        - completed: True keeps finished tasks, False keeps unfinished ones.
        Leaving an argument as None means "don't filter on that."
        """
        chosen = []
        for pet in owner.pets:
            # Skip this pet entirely if a name was given and doesn't match.
            if pet_name is not None and pet.name != pet_name:
                continue
            for task in pet.tasks:
                # Skip this task if a status was given and doesn't match.
                if completed is not None and task.completed != completed:
                    continue
                chosen.append(task)
        return chosen

    def filter_tasks(self, tasks: list[Task], available_minutes: int) -> list[Task]:
        """Select tasks in order until the available minutes are used up."""
        # Add tasks one by one until we run out of available time.
        chosen = []
        minutes_left = available_minutes
        for task in tasks:
            if task.duration <= minutes_left:
                chosen.append(task)
                minutes_left = minutes_left - task.duration
        return chosen

    def find_conflicts(self, tasks: list[Task]) -> list[str]:
        """Return warning messages for tasks that start at the same time.

        Compares every pair of tasks by their start time. Instead of raising
        an error, it collects a friendly warning for each clash and returns
        the list (which is empty when there are no conflicts).
        """
        warnings = []
        # Compare each task with the ones after it so no pair is checked twice.
        for i in range(len(tasks)):
            for j in range(i + 1, len(tasks)):
                first = tasks[i]
                second = tasks[j]
                if first.time == second.time:
                    warnings.append(
                        "Conflict: '{}' and '{}' are both scheduled at {}.".format(
                            first.name,
                            second.name,
                            first.time,
                        )
                    )
        return warnings
