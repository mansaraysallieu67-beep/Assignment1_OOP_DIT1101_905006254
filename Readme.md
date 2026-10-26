Anonymous Patient Record System
1. Project Overview

The Anonymous Patient Record System is a simple, menu-driven Python application designed to manage basic patient records using anonymous identification numbers. It allows users to add patient records, display all stored records, search for individual patients, and validate the information entered.

The system uses object-oriented programming (OOP) to organise patient data and record management. It stores records in memory while the program is running, making it suitable for learning, demonstration, and introductory programming projects.

Important: This is an educational prototype, not a production-ready medical records system. Use fictional or properly anonymised data only.

2. Objectives

The main objectives of this project are to:

Create and manage anonymous patient records.
Validate patient identification numbers and input values.
Categorise patients by age band and condition category.
Record optional vital signs, including temperature and pulse.
Search for patient records using anonymous IDs.
Prevent duplicate patient identification numbers.
Demonstrate object-oriented programming concepts in Python.
3. Features
Add patient records: Enter an anonymous ID, age band, condition category, temperature, and pulse.
Display all records: View all patient records currently stored in the system.
Search records: Find a patient using their anonymous ID.
Input validation: Reject invalid IDs, age bands, condition categories, temperatures, and pulse values.
Duplicate prevention: Prevent multiple records from being added with the same anonymous ID.
Optional vital signs: Allow temperature and pulse to be left unrecorded.
Demonstration mode: Display fictional sample records and demonstrate record searching and duplicate-ID validation.
Menu-driven interface: Navigate the system through a simple command-line menu.
4. Technologies Used
Programming language: Python 3
Programming concepts: Object-oriented programming, classes, objects, methods, functions, loops, conditional statements, exception handling, and input validation.
Data storage: In-memory Python list.
Interface: Command-line interface (CLI).

No external Python packages are required.

5. System Requirements
Python 3 installed on your computer.
A text editor or Python-compatible IDE, such as Visual Studio Code, PyCharm, or IDLE.
A terminal or command prompt.
6. Installation and Setup
Step 1: Install Python

Download Python 3 from the official website:

https://www.python.org/downloads/

Verify the installation by running:

bash
python --version


Depending on your operating system, you may need to use:

bash
python3 --version

Step 2: Save the source code

Save the Python program in a file named:

text
patient_record_system.py

Step 3: Open a terminal

Navigate to the directory containing the Python file.

Step 4: Run the program

On Windows:

bash
python patient_record_system.py


On macOS or Linux:

bash
python3 patient_record_system.py

7. How to Use the System

After launching the program, the main menu appears:

text
ANONYMOUS PATIENT RECORD SYSTEM
Use fictional or anonymised information only.
Records are cleared when the program closes.

1. Add patient record
2. Display all records
3. Search for a record
4. Exit
Type demo to show fictional sample records.

Option 1: Add Patient Record

Select 1 to create a new patient record.

The system requests:

Anonymous ID in the format P001.
Age band.
Condition category.
Temperature in degrees Celsius, or Enter to skip.
Pulse in beats per minute, or Enter to skip.

The record is added if the supplied information is valid and the ID is not already in use.

Option 2: Display All Records

Select 2 to display every patient record stored during the current session.

If no records exist, the system displays a message indicating that no patient records are available.

Option 3: Search for a Record

Select 3 and enter an anonymous ID, such as P001.

The system displays the matching record if it exists. Otherwise, it reports that the record was not found.

Option 4: Exit

Select 4 to close the application.

Note: Records are not saved to a file or database. All records are lost when the program closes.

Demonstration Mode

Type demo at the main menu to run the demonstration.

The demonstration creates a separate system containing fictional sample records, displays them, searches for P001, and tests whether a duplicate ID is rejected. These demonstration records do not affect records in the main application.

8. Data Validation Rules
Field	Validation rule
Anonymous ID	Must begin with P, followed by exactly three digits.
Age band	Must be one of the predefined age bands.
Condition category	Must be one of the predefined categories.
Temperature	Optional; if entered, must be between 30°C and 45°C.
Pulse	Optional; if entered, must be a whole number from 20 to 250 bpm.
Duplicate ID	Not allowed within the same record system.
Available Age Bands
0-12
13-17
18-35
36-59
60+
Available Condition Categories
General
Respiratory
Digestive
Injury
Other
9. Project Structure

The project can be organised as follows:

text
anonymous-patient-record-system/
├── patient_record_system.py
└── README.md

patient_record_system.py contains the complete application.
README.md documents the project's purpose, features, setup, and usage.
10. Code Structure
Patient Class

The Patient class represents an individual patient record. It:

Defines the permitted age bands, condition categories, and vital-sign labels.
Validates anonymous identification numbers.
Validates and updates patient record information.
Formats patient information for display.
PatientRecordSystem Class

The PatientRecordSystem class manages the collection of patient records. It:

Stores Patient objects in a single list.
Adds records after checking their validity and uniqueness.
Searches for records by anonymous ID.
Displays all stored records.
Creates fictional sample records for demonstration purposes.
Input and Menu Functions

The supporting functions handle user interaction:

choose_option() — displays choices and validates menu selections.
read_temperature() — reads and validates temperature input.
read_pulse() — reads and validates pulse input.
add_patient() — collects information and adds a patient record.
search_patient() — searches for a patient record.
run_demo() — runs the demonstration.
main() — controls the main application loop.
11. Example Output

A sample patient record may appear as follows:

text
Anonymous ID: P001
Age band: 18-35
Condition category: General
Temperature (C): 36.7
Pulse (bpm): 72


The demonstration uses fictional data and does not represent a real patient.

12. Testing

The following test cases can be used to check the main functionality.

Test	Expected result
Add a valid patient record	Record is added successfully.
Enter an invalid anonymous ID	Input is rejected.
Add an existing anonymous ID	Duplicate record is rejected.
Enter a temperature outside 30–45°C	Input is rejected.
Enter a pulse outside 20–250 bpm	Input is rejected.
Leave temperature or pulse blank	Vital sign is stored as not recorded.
Search for an existing ID	Matching record is displayed.
Search for a nonexistent ID	Record-not-found message appears.
Display records when none exist	No-records message appears.
Run demonstration mode	Fictional sample records and duplicate-ID test are displayed.

These are expected outcomes; they should be verified by running the application.

13. Limitations
Records exist only in memory and are not persistent.
The system does not provide authentication or user roles.
There is no graphical user interface.
Records cannot currently be edited or deleted through the menu.
The system does not use a database.
Input validation does not establish whether vital signs are medically normal or abnormal.
The application has not been designed or assessed for clinical use, regulatory compliance, or secure handling of real patient information.
14. Possible Future Improvements

Future versions could include:

Saving and loading records using JSON, CSV, or a database.
Updating and deleting existing records.
Adding automated unit tests.
Introducing user authentication and access controls.
Developing a graphical interface or web application.
Adding record timestamps and audit logs.
Implementing appropriate encryption, privacy safeguards, and access logging before any legitimate handling of sensitive health information.
15. Privacy and Safety Notice

Although the system uses anonymous IDs, an ID alone does not guarantee that a record is anonymous. Patient information can still be identifiable when combined with other details.

Use fictional or properly anonymised information for demonstrations and testing. Do not use this prototype to store real patient information or make clinical decisions.

16. License

No license has been specified for this project. If you intend to publish or distribute it, consider selecting an appropriate open-source license, such as the MIT License, after confirming that it suits your intended use.

17. Author

Project: Anonymous Patient Record System
Language: Python 3
Project type: Educational / demonstration application