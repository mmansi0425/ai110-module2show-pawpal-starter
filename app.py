import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

if "owner" not in st.session_state:
    st.session_state.owner = Owner(
        name="",
        email="",
        available_minutes=60
    )

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()


st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

# The Owner object lives in st.session_state so it (and its pets/tasks)
# persists across Streamlit reruns. We grab a shortcut reference here.
owner = st.session_state.owner
scheduler = st.session_state.scheduler

# Priority in the UI is a word, but Task.priority is a number where 1 is
# highest. This little map converts between the two.
PRIORITY_TO_NUMBER = {"high": 1, "medium": 2, "low": 3}

st.subheader("Owner")
owner.name = st.text_input("Owner name", value=owner.name or "Jordan")
owner.available_minutes = st.number_input(
    "Available minutes today", min_value=1, max_value=1440, value=owner.available_minutes
)

st.divider()

st.subheader("Add a Pet")
col1, col2 = st.columns(2)
with col1:
    pet_name = st.text_input("Pet name", value="Mochi")
with col2:
    species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add pet"):
    owner.add_pet(Pet(name=pet_name, species=species))
    st.success(f"Added {pet_name} the {species}.")

st.divider()

st.subheader("Add a Task")

if not owner.ets:
    st.info("Add a pet first, then you can add tasks for it.")
else:
    # Let the user pick which pet the task belongs to. We show the pet names
    # and use the selected index to find the matching Pet object.
    pet_names = [pet.name for pet in owner.pets]
    selected_index = pet_names.index(
        st.selectbox("Which pet is this task for?", pet_names)
    )
    selected_pet = owner.pets[selected_index]

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        task = Task(
            name=task_title,
            duration=int(duration),
            priority=PRIORITY_TO_NUMBER[priority],
        )
        selected_pet.add_task(task)
        st.success(f"Added '{task_title}' for {selected_pet.name}.")

# Show every pet and its current tasks so the user can see what they've built.
if owner.pets:
    st.write("Current pets and tasks:")
    for pet in owner.pets:
        st.markdown(f"**{pet.name}** ({pet.species})")
        if pet.tasks:
            for task in pet.tasks:
                st.write(f"- {task.name} — {task.duration} min (priority {task.priority})")
        else:
            st.caption("No tasks yet.")

st.divider()

st.subheader("Build Schedule")
st.caption("Generates a plan that fits your available time, highest priority first.")

if st.button("Generate schedule"):
    plan = scheduler.generate_plan(owner)
    if plan:
        st.write("Here's your plan for today:")
        for task in plan:
            st.write(f"- {task.name} — {task.duration} min (priority {task.priority})")
    else:
        st.info("No tasks fit your available time. Add tasks or increase available minutes.")
