class Patient:

    def __init__(self, name):
        if not name:
            raise ValueError("Patient name cannot be empty")
        self.name = name

    def get_name(self):
        return self.name


class Practitioner:

    def __init__(self, name):
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        self.name = name

    def get_name(self):
        return self.name


class Appointment:

    def __init__(self, appointment_id, patient, practitioner, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.time = time
        self.status = "booked"

        if not self.is_valid():
            raise ValueError("Appointment is missing required information")

    def is_valid(self):

        return bool(self.patient) and bool(self.practitioner) and bool(self.time)

    def conflicts_with(self, other_appointment):
        """Checks whether this appointment clashes with another
        (same practitioner, same time).
        Supports: FR-10
        """
        return (
                self.practitioner.get_name() == other_appointment.practitioner.get_name()
                and self.time == other_appointment.time
        )

    def __str__(self):
        return (f"Appointment {self.appointment_id}: "
                f"Patient={self.patient.get_name()}, "
                f"Practitioner={self.practitioner.get_name()}, "
                f"Time={self.time}, Status={self.status}")


if __name__ == "__main__":
    p1 = Patient("Alice Smith")
    doc1 = Practitioner("Dr. John Doe")
    appt1 = Appointment(1, p1, doc1, "2024-07-20 10:00 AM")
    print(appt1)