from enum import Enum


class Patient:
    """Represents a patient at SmartCare Clinic.
    Supports: FR-01, FR-04, FR-08
    """

    def __init__(self, name: str) -> None:
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Patient name cannot be empty")
        self._name: str = name.strip()

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f"Patient(name={self._name!r})"


class Practitioner:
    """Represents a practitioner at SmartCare Clinic.
    Supports: FR-02, FR-05, FR-10
    """

    def __init__(self, practitioner_id: str, name: str, specialty: str) -> None:
        if not practitioner_id or not isinstance(practitioner_id, str):
            raise ValueError("Practitioner ID cannot be empty")
        if not name or not isinstance(name, str) or not name.strip():
            raise ValueError("Practitioner name cannot be empty")
        if not specialty or not isinstance(specialty, str) or not specialty.strip():
            raise ValueError("Practitioner specialty cannot be empty")

        self._id: str = practitioner_id
        self._name: str = name.strip()
        self._specialty: str = specialty.strip()

    @property
    def name(self) -> str:
        return self._name

    @property
    def practitioner_id(self) -> str:
        return self._id

    @property
    def specialty(self) -> str:
        return self._specialty

    def __eq__(self, other: object) -> bool:
        # Two Practitioner objects represent the same practitioner
        # if they share the same ID, not just the same object reference.
        if not isinstance(other, Practitioner):
            return NotImplemented
        return self._id == other._id

    def __hash__(self) -> int:
        return hash(self._id)

    def __repr__(self) -> str:
        return f"Practitioner(id={self._id!r}, name={self._name!r}, specialty={self._specialty!r})"


class AppointmentStatus(Enum):
    BOOKED = "BOOKED"
    CANCELLED = "CANCELLED"


class AppointmentValidationError(Exception):
    """Raised when an Appointment fails business-rule validation."""
    pass


class AppointmentStateError(Exception):
    """Raised when an illegal status transition is attempted."""
    pass


class Appointment:
    """Represents a single booked appointment.
    Supports: FR-03, FR-04, FR-05, FR-06, FR-09, FR-10, NFR-04
    """

    def __init__(
        self,
        appointment_id: str,
        patient: Patient,
        practitioner: Practitioner,
        time: str,
    ) -> None:
        if not appointment_id:
            raise AppointmentValidationError("Appointment ID cannot be empty")  # FR-09
        if not patient:
            raise AppointmentValidationError("Patient cannot be empty")  # FR-04
        if not practitioner:
            raise AppointmentValidationError("Practitioner cannot be empty")  # FR-05
        if not time:
            raise AppointmentValidationError("Appointment time cannot be empty")  # FR-06

        self._appointment_id: str = appointment_id
        self._patient: Patient = patient
        self._practitioner: Practitioner = practitioner
        self._time: str = time
        self._status: AppointmentStatus = AppointmentStatus.BOOKED

    @property
    def appointment_id(self) -> str:
        return self._appointment_id

    @property
    def patient(self) -> Patient:
        return self._patient

    @property
    def practitioner(self) -> Practitioner:
        return self._practitioner

    @property
    def time(self) -> str:
        return self._time

    @property
    def status(self) -> AppointmentStatus:
        return self._status

    def cancel(self) -> None:
        """Cancel this appointment.
        Raises AppointmentStateError if it is already cancelled,
        preventing an illegal repeated transition.
        """
        if self._status == AppointmentStatus.CANCELLED:
            raise AppointmentStateError("Appointment is already cancelled")
        self._status = AppointmentStatus.CANCELLED

    def conflicts_with(self, other: "Appointment") -> bool:
        """FR-10: Two appointments conflict if they share the same
        practitioner (compared by ID, not object identity) and time.
        """
        if other is None:
            return False
        return self._practitioner == other._practitioner and self._time == other._time

    def __repr__(self) -> str:
        return (f"Appointment(id={self._appointment_id!r}, "
                f"patient={self._patient.name!r}, "
                f"practitioner={self._practitioner.name!r}, "
                f"time={self._time!r}, status={self._status.value})")


if __name__ == "__main__":
    p1 = Patient("Alice Smith")
    doc1 = Practitioner("P001", "Dr. John Doe", "General Practice")
    appt1 = Appointment("A001", p1, doc1, "2024-07-20 10:00 AM")
    print(appt1)

    print()
    print("=== Cancel once ===")
    appt1.cancel()
    print(appt1)

    print()
    print("=== Attempt illegal repeated cancel ===")
    try:
        appt1.cancel()
        print("BUG: no error raised")
    except AppointmentStateError as e:
        print("Correctly rejected:", e)

    print()
    print("=== Conflict check using two different Practitioner objects with same ID ===")
    doc1_copy = Practitioner("P001", "Dr. John Doe", "General Practice")
    p2 = Patient("Bob Johnson")
    appt2 = Appointment("A002", p2, doc1_copy, "2024-07-20 10:00 AM")
    appt3 = Appointment("A003", p1, doc1, "2024-07-20 10:00 AM")
    print("Conflict detected (should be True):", appt3.conflicts_with(appt2))