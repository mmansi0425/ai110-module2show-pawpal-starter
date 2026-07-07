"""PawPal+ system classes.

Implements the pet care scheduling logic based on the UML design in
diagrams/uml.mmd.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet's task list."""
        self.tasks.append(task)


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
