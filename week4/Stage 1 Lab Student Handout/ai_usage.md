Part A: 
data stored must be: patient name, practitioner name, appointment time and date
functions that may be useful: book_appointment, display_appointments, cancel_appointment, find_appointment, update_appointment
What could go wrong: double booking, typos in patient or practitioner names creating inconsistent records, no way to tell which appointments are still active vs. already cancelled, data lost entirely if the program closes
Unclear requirements: can one patient have multiple appointments? should practitioner names be validated against an actual list of clinic staff, or can any name be typed in? should the system prevent bookings outside clinic operating hours?

PART C:
🧩 1. What the code does
Core idea: It builds a dictionary representing an appointment and adds it to a list called appointments.
Here’s the flow:
It checks whether patient_name is empty.
If it is, it raises a ValueError.
It creates a dictionary with three keys: "patient", "practitioner", and "time".
It appends that dictionary to a global list named appointments.
This is a minimal data‑collection helper—it doesn’t validate much, but it stores the appointment.
⚠️ 2. Three limitations
Missing validation — Only the patient name is checked. Practitioner name, time format, and conflicts are ignored.
Global dependency — It assumes appointments already exists and is accessible. If not, the function breaks.
No error handling for duplicates — It doesn’t check whether the same patient already has an appointment at that time.
🔧 3. Suggested improvements
Add more validation  
Validate practitioner name, ensure appointment time is a proper datetime, and check for scheduling conflicts.
Use a class or module structure  
Encapsulate appointment storage instead of relying on a global list.
Return the created appointment  
Returning the dictionary makes the function easier to test and reuse.
Add logging or persistence  
Instead of just appending to a list, write to a file or database.
❓ 4. Two questions to test your understanding
Why is relying on a global appointments list risky in larger programs
What advantage does validating the appointment time format give you
to answer your questions, a global variable can be modified from anywhere in the code, making bugs hard to trace and testing harder since functions depend on state outside themselves. In bigger programs with multiple files or contributors, this raises the risk of the list being changed unexpectedly or in conflicting ways. Also, validating the time catches mistakes immediately at booking, rather than causing confusing errors later when the data is sorted, compared, or displayed. It also makes real scheduling features possible, like detecting conflicts or checking if a time is in the past, which can't be done reliably with an arbitrary string.
Your answers are sharp — you’ve captured the real reasons these issues matter in actual software, not just theory. Let me build on what you said and push your understanding a bit further.
🎯 Your reasoning, refined
You’re absolutely right that a global list makes the function fragile. The deeper issue is that it breaks referential transparency — the function’s output depends on hidden external state. That makes debugging unpredictable and unit testing painful.
Your point about time validation is spot‑on. Treating time as structured data (e.g., datetime) unlocks every scheduling feature: conflict detection, sorting, filtering, reminders, and preventing invalid bookings.
You’re thinking like someone who’s moving from “writing code that works” to “writing code that scales.”
Tool used: Microsoft Copilot Purpose: Part C

Part D:
AI GENERATED CODE FROM COPILOT:
# A list to store all appointments
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    """Store a basic appointment entry in a list."""

    # Basic validation to help beginners avoid common mistakes
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not practitioner_name:
        raise ValueError("Practitioner name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")

    # Create a simple dictionary to represent the appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Store it in the list
    appointments.append(appointment)

    return appointment
