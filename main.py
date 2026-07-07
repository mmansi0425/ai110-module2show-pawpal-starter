from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner(
        name="Mansi",
        email="mansi.mohanraj@gmail.com",
        available_minutes=60
    )

    dog = Pet(name="Luna", species="Dog")
    dog.add_task(Task("Morning Walk", 30, 1))
    dog.add_task(Task("Feed Breakfast", 10, 1))
    owner.add_pet(dog)

    cat = Pet(name="Bentley", species="Cat")
    cat.add_task(Task("Brush Fur", 15, 2))
    cat.add_task(Task("Feed Breakfast", 10, 3))
    owner.add_pet(cat)

    scheduler = Scheduler()
    schedule = scheduler.generate_plan(owner)

    print("Today's Schedule")
    print("-" * 25)

    for task in schedule:
        print(
            "- {} ({} min, Priority {})".format(
                task.name,
                task.duration,
                task.priority
            )
        )


if __name__ == "__main__":
    main()