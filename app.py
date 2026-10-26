class Patient:
    AGE_BANDS = ("0-12", "13-17", "18-35", "36-59", "60+")
    CONDITION_CATEGORIES = (
        "General",
        "Respiratory",
        "Digestive",
        "Injury",
        "Other",
    )
    VITAL_SIGN_LABELS = ("Temperature (C)", "Pulse (bpm)")

    def __init__(
        self,
        anonymous_id,
        age_band,
        condition_category,
        temperature_c=None,
        pulse_bpm=None,
    ):
        if not self.is_valid_anonymous_id(anonymous_id):
            raise ValueError("ID must be P followed by three digits.")

        self.anonymous_id = anonymous_id
        self.update_record(
            age_band,
            condition_category,
            temperature_c,
            pulse_bpm,
        )

    @staticmethod
    def is_valid_anonymous_id(anonymous_id):
        return (
            isinstance(anonymous_id, str)
            and len(anonymous_id) == 4
            and anonymous_id[0] == "P"
            and all(
                character in "0123456789"
                for character in anonymous_id[1:]
            )
        )

    def update_record(
        self,
        age_band,
        condition_category,
        temperature_c=None,
        pulse_bpm=None,
    ):
        # Check all values before changing any attributes.
        if age_band not in self.AGE_BANDS:
            raise ValueError("Invalid age band.")

        if condition_category not in self.CONDITION_CATEGORIES:
            raise ValueError("Invalid condition category.")

        if temperature_c is not None:
            if (
                isinstance(temperature_c, bool)
                or not isinstance(temperature_c, (int, float))
                or not 30 <= temperature_c <= 45
            ):
                raise ValueError(
                    "Temperature must be between 30 and 45 C."
                )

        if pulse_bpm is not None:
            if (
                isinstance(pulse_bpm, bool)
                or not isinstance(pulse_bpm, int)
                or not 20 <= pulse_bpm <= 250
            ):
                raise ValueError(
                    "Pulse must be a whole number from 20 to 250."
                )

        self.age_band = age_band
        self.condition_category = condition_category
        self.temperature_c = temperature_c
        self.pulse_bpm = pulse_bpm

    def display_info(self):
        temperature = (
            "Not recorded"
            if self.temperature_c is None
            else f"{self.temperature_c:.1f}"
        )
        pulse = (
            "Not recorded"
            if self.pulse_bpm is None
            else str(self.pulse_bpm)
        )

        return (
            f"Anonymous ID: {self.anonymous_id}\n"
            f"Age band: {self.age_band}\n"
            f"Condition category: {self.condition_category}\n"
            f"{self.VITAL_SIGN_LABELS[0]}: {temperature}\n"
            f"{self.VITAL_SIGN_LABELS[1]}: {pulse}"
        )


class PatientRecordSystem:
    def __init__(self):
        # This is the only list used to store Patient objects.
        self.records = []

    def add_record(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient objects can be added.")

        if self.find_record(patient.anonymous_id) is not None:
            raise ValueError("This anonymous ID already exists.")

        self.records.append(patient)

    def find_record(self, anonymous_id):
        for patient in self.records:
            if patient.anonymous_id == anonymous_id:
                return patient

        return None

    def display_records(self):
        if not self.records:
            print("\nNo patient records available.")
            return

        for patient in self.records:
            print("-" * 40)
            print(patient.display_info())

        print("-" * 40)

    @classmethod
    def create_sample_system(cls):
        system = cls()

        system.add_record(
            Patient("P001", "18-35", "General", 36.7, 72)
        )
        system.add_record(
            Patient("P002", "36-59", "Respiratory")
        )

        return system


def choose_option(title, options):
    print(f"\n{title}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Choose an option: "))

            if 1 <= choice <= len(options):
                return options[choice - 1]

            print("Choose one of the displayed options.")
        except ValueError:
            print("Enter a whole number.")


def read_temperature():
    while True:
        value = input(
            "Temperature in C (30-45; Enter to skip): "
        ).strip()

        if value == "":
            return None

        try:
            temperature = float(value)

            if 30 <= temperature <= 45:
                return temperature

            print("Temperature must be between 30 and 45 C.")
        except ValueError:
            print("Enter a valid number.")


def read_pulse():
    while True:
        value = input(
            "Pulse in bpm (20-250; Enter to skip): "
        ).strip()

        if value == "":
            return None

        try:
            pulse = int(value)

            if 20 <= pulse <= 250:
                return pulse

            print("Pulse must be between 20 and 250 bpm.")
        except ValueError:
            print("Enter a whole number.")


def add_patient(system):
    print("\nADD PATIENT RECORD")

    while True:
        anonymous_id = input(
            "Anonymous ID, e.g. P001: "
        ).strip().upper()

        if not Patient.is_valid_anonymous_id(anonymous_id):
            print("Use P followed by three digits, e.g. P001.")
        elif system.find_record(anonymous_id) is not None:
            print("This ID already exists. Use another ID.")
        else:
            break

    age_band = choose_option(
        "Select age band:",
        Patient.AGE_BANDS,
    )
    category = choose_option(
        "Select condition category:",
        Patient.CONDITION_CATEGORIES,
    )

    patient = Patient(
        anonymous_id,
        age_band,
        category,
        read_temperature(),
        read_pulse(),
    )

    system.add_record(patient)
    print(f"\nRecord {anonymous_id} added successfully.")


def search_patient(system):
    anonymous_id = input(
        "\nEnter anonymous ID to search: "
    ).strip().upper()

    if not Patient.is_valid_anonymous_id(anonymous_id):
        print("Invalid ID. Use a format such as P001.")
        return

    patient = system.find_record(anonymous_id)

    if patient is None:
        print("Record not found.")
    else:
        print("\nRECORD FOUND")
        print(patient.display_info())


def run_demo():
    # Uses a separate system so demo records do not affect your records.
    demo_system = PatientRecordSystem.create_sample_system()

    print("\nDEMONSTRATION — FICTIONAL RECORDS")
    demo_system.display_records()

    print("\nSEARCH FOR P001")
    patient = demo_system.find_record("P001")

    if patient is not None:
        print(patient.display_info())

    print("\nDUPLICATE-ID TEST")

    try:
        demo_system.add_record(
            Patient("P001", "60+", "Other")
        )
    except ValueError as error:
        print(f"Duplicate rejected: {error}")


def main():
    system = PatientRecordSystem()

    print("ANONYMOUS PATIENT RECORD SYSTEM")
    print("Use fictional or anonymised information only.")
    print("Records are cleared when the program closes.")

    while True:
        print("\n1. Add patient record")
        print("2. Display all records")
        print("3. Search for a record")
        print("4. Exit")
        print("Type demo to show fictional sample records.")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            add_patient(system)
        elif choice == "2":
            system.display_records()
        elif choice == "3":
            search_patient(system)
        elif choice == "4":
            print("Goodbye. Records have not been saved.")
            break
        elif choice == "demo":
            run_demo()
        else:
            print("Enter 1, 2, 3, 4, or demo.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram closed. Records have not been saved.")