"""PawPal+ system class skeleton.

Generated from the UML design in diagrams/uml.mmd.
Method bodies are left as stubs (`pass`) — no scheduling logic yet.
"""

from dataclasses import dataclass, field


@dataclass
class Task:
    name: str
    duration: int
    priority: int
    completed: bool = False

    def mark_complete(self) -> None:
        pass


@dataclass
class Pet:
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass


@dataclass
class Owner:
    name: str
    email: str
    available_minutes: int
    pets: list[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass


class Scheduler:
    def generate_plan(self, owner: Owner) -> list[Task]:
        pass

    def sort_tasks(self, tasks: list[Task]) -> list[Task]:
        pass

    def filter_tasks(self, tasks: list[Task], available_minutes: int) -> list[Task]:
        pass
