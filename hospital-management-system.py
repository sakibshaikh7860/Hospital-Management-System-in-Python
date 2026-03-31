import csv
import os

PATIENT_FILE = "patients.csv"
BILL_FILE = "bills.csv"

# Create file if not exists
def create_file():
    if not os.path.exists(PATIENT_FILE):
        with open(PATIENT_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Gender", "Mobile", "Disease", "Doctor"])

    if not os.path.exists(BILL_FILE):
        with open(BILL_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Patient_ID", "Name", "Doctor_Fees", "Medicine_Charges", "Total"])


def add_patient():
    print("\n--- Add Patient Record ---")
    pid = input("Enter Patient ID: ")
    name = input("Enter Patient Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    mobile = input("Enter Mobile No: ")
    disease = input("Enter Disease/Problem: ")
    doctor = input("Enter Doctor Name: ")

    with open(PATIENT_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pid, name, age, gender, mobile, disease, doctor])

    print("Patient Added Successfully!")


def view_patients():
    print("\n--- All Patient Records ---")
    with open(PATIENT_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_patient():
    print("\n--- Search Patient ---")
    pid = input("Enter Patient ID to Search: ")

    found = False
    with open(PATIENT_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == pid:
                print("\n✅ Patient Found:")
                print("ID:", row[0])
                print("Name:", row[1])
                print("Age:", row[2])
                print("Gender:", row[3])
                print("Mobile:", row[4])
                print("Disease:", row[5])
                print("Doctor:", row[6])
                found = True
                break

    if not found:
        print("Patient Not Found!")


def delete_patient():
    print("\n--- Delete Patient Record ---")
    pid = input("Enter Patient ID to Delete: ")

    rows = []
    deleted = False

    with open(PATIENT_FILE, "r") as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(PATIENT_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] == pid:
                deleted = True
                continue
            writer.writerow(row)

    if deleted:
        print("✅ Patient Deleted Successfully!")
    else:
        print("Patient ID Not Found!")


def billing():
    print("\n--- Billing System ---")
    pid = input("Enter Patient ID: ")

    patient_found = False
    pname = ""

    with open(PATIENT_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == pid:
                pname = row[1]
                patient_found = True
                break

    if not patient_found:
        print("Patient Not Found! Billing not possible.")
        return

    doctor_fees = int(input("Enter Doctor Fees: "))
    medicine_charges = int(input("Enter Medicine Charges: "))

    total = doctor_fees + medicine_charges

    with open(BILL_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([pid, pname, doctor_fees, medicine_charges, total])

    print("\nBill Generated Successfully!")
    print("Patient Name:", pname)
    print("Doctor Fees:", doctor_fees)
    print("Medicine Charges:", medicine_charges)
    print("Total Bill:", total)


def view_bills():
    print("\n--- All Bills ---")
    with open(BILL_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def main_menu():
    create_file()

    while True:
        print("\n==============================")
        print("  HOSPITAL MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Billing")
        print("6. View Bills")
        print("7. Exit")
        print("==============================")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            billing()
        elif choice == "6":
            view_bills()
        elif choice == "7":
            print("Thank You!")
            break
        else:
            print("Invalid Choice! Try Again.")


main_menu()
