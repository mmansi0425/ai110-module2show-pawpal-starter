# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
My initial UML design had four main classes: Owner, Pet, Task, and Scheduler. 

Owner: Stores info. regarding the pet owner including their name and amount of time they have avaiable for pet care. 
Pet: stores basic info about the pet (name, species, care tasks) 
Task: represents indivdual pet care activities: feeding, walking, grooming. Each task includes info like duration, priority, etc... 
Scheduler: organizing tasks into a daily schedule base on owner's available time and each task's priority.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Currently, I have not made any major changes to my initial design. As I continue to work on my project, I may refine the classes or add new methods.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decside which constraints mattered most?
My scheduler considers the owner's available time, task priority, task completion status, and scheduled task time. First, it selects tasks that fit within the owner's available minutes, prioritizing higher-priority tasks before lower ones. 
 It alsos sort tasks by their scheduled time and filter tasks by pet or completion status. I chose these constraints because they are the most important for helping a pet owner complete essential care tasks within a limited amount of time.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?
My scheduler uses a simple conflict detection algorithm that only checks whether two tasks have the exact same scheduled start time. The AI suggested a more efficient solution using a dictionary to group tasks by time, but I kept my original implementation because it is easier to read and understand. Since PawPal+ only manages a small number of pet care tasks, this simpler approach is a reasonable tradeoff between readability and performance.


---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?
I used Ai yools for brainstorming, debugging and refactoring. I used prompts starting with phrases like, "check __", "can you __"


**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
I did not accept the AI's suggestion in phase 4 step 5. The AI agent wanted to complicate the implementation, but I kept it the same. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?
I tested that tasks could be marked as complete, that adding a task to a pet updated the pet's task list, that tasks were sorted correctly by time, that filtering by pet and completion status worked, and that the scheduler detected tasks scheduled at the same time. These tests were important to verify the core features of the program. 


**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?
I am pretty confident that my scheduler works correctly. If I had more time, I would test more complex situations. 
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
- I am most satisfied with building the scheduling system and successfully connecting the backend logic to the Streamlit interface so that user actions created and managed real objects.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
- If I had another iteration, I would improve the scheduler by supporting overlapping task detection based on duration, allowing users to edit or delete tasks, and making recurring task scheduling more advanced.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I learned that designing and workshopping systems before implementing helps the program run better. 