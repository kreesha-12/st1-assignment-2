Activity 1 

1. The ability to judge whether the code is actually correct and appropriate - An engineer needs to understand programming concepts well enough to read the generated code critically and spot bugs.
2. Requirements analysis and problem solving skills - Ai can write code but it cannot determine what a client actually needs. Someone would still have to manually translate a vague request into a clear, testable requirement.
3. System design and integration knowledge - Understanding how pieces fit together is something that Ai can suggest but not decide on its own. An engineer needs the broader knowledge to know which suggestions to accept or reject.

Activity 2 - Is This Software Engineering?

Scenario A: Only programming - A 50 line calculator is a small, self-contained script with no real requirements or design processes, it's just writing code to solve an immediate problem

Scenario B: Both programming and software engineering - A payroll system for 5,000 employees requires careful designing, testing, security, error handling and documentation. The consequences of something like this failing demand a disciplined engineering process, not just a simple working code. 

Scenario C: Only programming - Generating a simple appointment app from one prompt is still just producing code. There's no verification process and no consideration of long term maintainability unless a human engineer adds that afterwards.

Activity 3 - SmartCare Problem Analysis

Stakeholder 1 - Receptionist: Needs an easy way to book, view, edit, and cancel appointments quickly, plus reliable search so patient records aren't hard to find

Stakeholder 2 - Practitioner: Needs clear visibility of their own schedule and appointment history, without conflicting or duplicate bookings

Stakeholder 3 - Clinic Manager: Needs accurate, up-to-date reporting on appointments and clinic operations to support staffing and decision making

Stakeholder 4 - Patient: Needs confidence that their appointment is correctly recorded, not duplicated, and that their personal information is handled securely

Task 2 - Identify current problems
1. Appointments are sometimes booked twice for the same slot, since spreadsheets and paper records don't automatically check for duplicate or conflicting bookings
2. Patient records are difficult to locate quickly, since information is scattered across spreadsheets and paper rather than stored in one searchable system
3. Appointment status is inconsistent, making it unclear which appointments are still active, completed, or cancelled
4. Cancelling appointments is a manual process, which is slow, as well as error prone and makes it hard to keep records accurate and up to date

Task 3 - Ask client questions
1. When an appointment is cancelled, should the record be deleted entirely, or kept as "cancelled" for historical tracking and reporting?
2. Should the system actively prevent double booking a practitioner at the same date and time?
3. Besides name, what other information needs to be stored for patients and practitioners?
4. What specific operational reports does management need, and how often do they need to be generated?
5. Will practitioners or patients need direct access to the system themselves, or will receptionists be the only users entering and managing data?

Activity 4 - Critique an AI Response

Appointment management: Client evidence? Yes, explicitly requested and central to the reported problems. In scope? Yes. Decision? Accept - core feature client asked for 

Facial recognition login: Client evidence? No, not mentioned by the client. In scope? No. Decision? Reject - unnecessary complexity 

AI diagnosis recommendations: Client evidence? No. In scope? No. Decision? Reject - far outside scope

Patient search: Client evidence? Yes. In scope? Yes. Decision? Accept - supports the stated problem 

Online payment: Client evidence? No. In scope? Sort of. Decision? Keep unverified - could be a reasonable future feature, but needs to be confirmed with the client before building

Practitioner schedule view: Client evidence? Yes. In scope? Yes. Decision? Accept

Insurance processing: Client evidence? No. In scope? No. Decision? Reject

Treatment-plan generation: Client evidence? No. In scope: No. Decision? Reject - outside scope and inappropriate for an appointment management system, carries clinical risk

Exit question: Write one activity that a software engineer must perform and that cannot safely be delegated entirely to AI.
 
Verifying that a system meets a client's actual needs and correctly handles edge cases through testing. AI cannot know whether the code built was on right assumptions and whether it handles real world scenarios safely. This requires a human to run the code, test it against realistic scenarios, compare it to the requirements, and take responsibility for confirming it works correctly before it's trusted or deployed.


