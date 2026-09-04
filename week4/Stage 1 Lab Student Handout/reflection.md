PART G: One line improvement (done in python file)
Adding a check for appointment_time closes the gap where the system previously accepted "None" as a valid time without any warning. Now it says "ValueError: Appointment time cannot be empty" same with if you try input a blank patient name 

PART H: Reflection
Before using AI, I built a simple human-written prototype that used lists, dictionaries, and functions to record patient appointments. It only validated that the patient name wasn't empty and runnning it also revealed a few gaps such as no duplicate booking checks, no validation on the appointment time and no way to cancel or edit an appointment

Using AI as tutor helped me understand why relying on a global list becomes risky in larger programs, since any part of the code can modify it unexpectedly. Also why validating input formats (like appointment time) matters for preventing bad data.

The AI did make assumptions I hadn't asked for, when generating an alternative version, it validated all three fields instead of just patient name, and added docstrings and structure I didn't explicitly request. I verified this by actually running both versions against the same test cases (normal input, blank names, duplicate bookings) which showed the AI version caught mistakes that my version didn't have.

The engineering work that remained for me was deciding which single improvement to make, understanding exactly why it mattered, and implementing and testing it myself.

