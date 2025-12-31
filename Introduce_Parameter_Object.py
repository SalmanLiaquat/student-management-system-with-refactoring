
class StudentData:
    def __init__(self, roll_number, student_name, subjects=None):
        self.roll_number = roll_number
        self.student_name = student_name
        self.subjects = subjects if subjects else []

    def add_subject(self, subject_name, marks, grade):
        self.subjects.append({'name': subject_name, 'marks': marks, 'grade': grade})

    def calculate_average(self):
        return sum(s['marks'] for s in self.subjects) / len(self.subjects) if self.subjects else 0

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student_data):
        self.students.append(student_data)

    def find_by_roll(self, roll_number):
        return next((s for s in self.students if s.roll_number == roll_number), None)

    def delete_student(self, roll_number):
        for i, s in enumerate(self.students):
            if s.roll_number == roll_number:
                del self.students[i]
                return True
        return False

    def list_all_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- ALL STUDENT RECORDS ---")
        for s in self.students:
            print(f"Roll: {s.roll_number} | Name: {s.student_name}")

    # ----------------- Reports -----------------
    def grade_distribution_report(self):
        grades = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
        for s in self.students:
            for sub in s.subjects:
                grades[sub['grade']] += 1
        print("\n--- GRADE DISTRIBUTION ---")
        for g, c in grades.items():
            print(f"Grade {g}: {c}")

    def class_topper_report(self):
        topper = max(self.students, key=lambda s: s.calculate_average(), default=None)
        if topper:
            print("\n--- CLASS TOPPER ---")
            print(f"Name: {topper.student_name}\nRoll: {topper.roll_number}\nAverage: {topper.calculate_average():.2f}")
        else:
            print("No students found.")

    def pass_fail_report(self):
        passed = sum(1 for s in self.students if s.calculate_average() >= 35)
        failed = len(self.students) - passed
        print("\n--- PASS/FAIL REPORT ---")
        print("Passed:", passed)
        print("Failed:", failed)

    def update_student_name(self, roll_number, new_name):
        student = self.find_by_roll(roll_number)
        if student:
            student.student_name = new_name
            print("Name updated successfully.")
        else:
            print("Student not found.")

    def search_student_by_name(self, search_name):
        found = False
        for s in self.students:
            if s.student_name.lower() == search_name.lower():
                show_subject_table(s)
                found = True
        if not found:
            print("No student found with this name.")


# --------------------- Helper Functions ---------------------

def input_student_data():
    print("\n--- Enter Student Data ---")
    roll_number = input("Enter Roll Number: ")
    student_name = input("Enter Student Name: ")
    student_data = StudentData(roll_number, student_name)

    total_subjects = int(input("Total subjects: "))
    for i in range(total_subjects):
        print(f"Subject {i+1}:")
        name = input("  Name: ")
        marks = float(input("  Marks (0-100): "))
        if marks < 0 or marks > 100:
            print("[Warning] Marks out of range!")
        grade = calculate_grade(marks)
        student_data.add_subject(name, marks, grade)

    return student_data

def calculate_grade(marks):
    if marks >= 90: return "A"
    elif marks >= 80: return "B"
    elif marks >= 70: return "C"
    elif marks >= 60: return "D"
    elif marks >= 35: return "E"
    else: return "F"

def show_subject_table(student_data):
    if not student_data.subjects:
        print("No subjects found.")
        return
    b_line = "=" * 85
    print("\n" + b_line)
    print(f"RECORD FOUND: {student_data.student_name} | ROLL: {student_data.roll_number}")
    print(b_line)
    print("SUBJECT NAME           MARKS OBTAINED      FINAL GRADE")
    print("--------------------   ------------------  ------------")
    for s in student_data.subjects:
        print(s['name'].ljust(22) + f"{s['marks']:.2f}".ljust(20) + s['grade'])
    print(b_line)
    print(f"Average Marks: {student_data.calculate_average():.2f}")


# --------------------- Main Application ---------------------

def main_app_loop():
    manager = StudentManager()
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Student")
        print("2. Search by Roll")
        print("3. Delete Student")
        print("4. List All Students")
        print("5. Grade Distribution")
        print("6. Class Topper")
        print("7. Pass/Fail Report")
        print("8. Update Name")
        print("9. Search by Name")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student(input_student_data())
            print("Student added successfully.")
        elif choice == "2":
            roll = input("Enter Roll Number: ")
            s = manager.find_by_roll(roll)
            if s:
                show_subject_table(s)
            else:
                print("Student not found.")
        elif choice == "3":
            roll = input("Enter Roll Number: ")
            print("Deleted" if manager.delete_student(roll) else "Not found")
        elif choice == "4":
            manager.list_all_students()
        elif choice == "5":
            manager.grade_distribution_report()
        elif choice == "6":
            manager.class_topper_report()
        elif choice == "7":
            manager.pass_fail_report()
        elif choice == "8":
            roll = input("Enter Roll Number: ")
            name = input("Enter New Name: ")
            manager.update_student_name(roll, name)
        elif choice == "9":
            name = input("Enter Student Name: ")
            manager.search_student_by_name(name)
        elif choice == "10":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_app_loop()
