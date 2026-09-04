# task 1
# Create and run a simple Python file with basic input, output statements
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time: {appointment1_time}")

# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time: {appointment2_time}")

# task1enhanced
# Use lists, dictionaries and functions to enhance the Python file
appointments = []

def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)

def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | Practitioner: {appointment['practitioner']} | Time: {appointment['time']}")

#PART F TESTS
#Test 1: normal appointment book_appointment('Carol Lee', 'Dr. Smith', '2024-08-01 09:00 AM')
#display_appointments()
#Test 2: Blank patient name book_appointment('', 'Dr. Smith', '2024-08-01 09:00 AM')
#Test 3: Two appointments for the same practitioner/time book_appointment('Dan Kim', 'Dr. Smith', '2024-08-01 09:00 AM')
#book_appointment('Eve Chan', 'Dr. Smith', '2024-08-01 09:00 AM')
#display_appointments()
#Test 4: Strange input book_appointment(None, 'Dr. Smith', '2024-08-01 09:00 AM')
#Test 4: Strange input book_appointment('Frank Wu', 'Dr. Smith', None)
#display_appointments()

#PART G Improve one thing
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
    if not appointment_time:
        raise ValueError("Appointment time cannot be empty")


#AI CODE
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