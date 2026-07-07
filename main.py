from datetime import date

from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(
        name="Mansi",
        email="mansi.mohanraj@gmail.com",
        available_minutes=60
    )

    dog = Pet(name="Luna", species="Dog")
    dog.add_task(Task("Morning Walk", 30, 1, "08:00", frequency="daily", due_date=date(2026, 7, 7)))
    dog.add_task(Task("Feed Breakfast", 10, 1, "07:30"))
    owner.add_pet(dog)

    cat = Pet(name="Bentley", species="Cat")
    cat.add_task(Task("Brush Fur", 15, 2, "09:15"))
    cat.add_task(Task("Feed Breakfast", 10, 3, "07:45"))
    # Play Time clashes with Luna's Morning Walk (both start at 08:00).
    cat.add_task(Task("Play Time", 20, 2, "08:00"))
    owner.add_pet(cat)

    scheduler = Scheduler()

    # Show the plan that fits the owner's available time, in time order.
    schedule = scheduler.generate_plan(owner)
    schedule = scheduler.sort_by_time(schedule)

    print("Today's Schedule")
    print("-" * 25)

    for task in schedule:
        print(
            "- {} at {} ({} min, Priority {})".format(
                task.name,
                task.time,
                task.duration,
                task.priority
            )
        )

    # Show just Luna's tasks, using the new filter method.
    luna_tasks = scheduler.filter_tasks_by(owner, pet_name="Luna")

    print()
    print("Luna's Tasks")
    print("-" * 25)

    for task in luna_tasks:
        print("- {} at {}".format(task.name, task.time))

    # Check every scheduled task for start-time clashes.
    all_tasks = scheduler.filter_tasks_by(owner)
    conflicts = scheduler.find_conflicts(all_tasks)

    print()
    print("Schedule Conflicts")
    print("-" * 25)
    if conflicts:
        for warning in conflicts:
            print("- {}".format(warning))
    else:
        print("- No conflicts found.")

    # Complete Luna's recurring walk. This automatically schedules tomorrow's.
    walk = dog.tasks[0]
    next_walk = dog.complete_task(walk)

    print()
    print("Recurring Tasks")
    print("-" * 25)
    print("- Completed '{}' due {}".format(walk.name, walk.due_date))
    if next_walk is not None:
        print("- Next '{}' scheduled for {}".format(next_walk.name, next_walk.due_date))


if __name__ == "__main__":
    main()