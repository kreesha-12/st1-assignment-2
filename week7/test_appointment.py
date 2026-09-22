from smartcare_v04 import Patient, Practitioner, Appointment, AppointmentStatus, AppointmentValidationError

print('=== Test 1: Create valid objects ===')
p1 = Patient('Alice Smith')
doc1 = Practitioner('P001', 'Dr. John Doe', 'General Practice')
appt1 = Appointment('A001', p1, doc1, '2024-07-20 10:00 AM')
print('Created:', appt1.appointment_id, appt1.status)

print()
print('=== Test 2: Invalid input (missing practitioner) ===')
try:
    Appointment('A002', p1, None, '2024-07-20 11:00 AM')
    print('BUG: no error raised')
except AppointmentValidationError as e:
    print('Correctly rejected:', e)

print()
print('=== Test 3: Cancel a scheduled appointment ===')
try:
    appt1.status = AppointmentStatus.CANCELLED
    print('Cancelled by direct mutation:', appt1.status)
except AttributeError as e:
    print('No cancel() method exists, direct mutation used instead:', e)

print()
print('=== Test 4: Attempt an illegal repeated transition (cancel an already-cancelled appointment) ===')
try:
    appt1.status = AppointmentStatus.CANCELLED
    print('No error \u2014 status set to CANCELLED again with no complaint:', appt1.status)
except Exception as e:
    print('Error raised:', e)