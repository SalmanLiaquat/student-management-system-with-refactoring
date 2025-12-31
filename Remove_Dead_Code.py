
class Student:
    def __init__(self, roll_number, student_name):
        self.roll_number = roll_number
        self.student_name = student_name
        self.subjects = []

    def add_subject(self, subject_name, marks_obtained, grade):
        self.subjects.append({
            'name': subject_name,
            'marks': marks_obtained,
            'grade': grade
        })

    def calculate_average(self):
        return sum(s['marks'] for s in self.subjects) / len(self.subjects) if self.subjects else 0

    def show_summary(self):
        print("\n--- STUDENT SUMMARY ---")
        print("Name:", self.student_name)
        print("Roll No:", self.roll_number)
        print("Total Subjects:", len(self.subjects))
        print("Average Marks:", "{:.2f}".format(self.calculate_average()))

        if self.calculate_average() >= 85:
            print("Final Result: Excellent")
        elif self.calculate_average() >= 70:
            print("Final Result: Good")
        elif self.calculate_average() >= 50:
            print("Final Result: Average")
        else:
            print("Final Result: Needs Improvement")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def find_by_roll(self, roll_number):
        for student in self.students:
            if student.roll_number == roll_number:
                return student
        return None

    def delete_student(self, roll_number):
        for i, student in enumerate(self.students):
            if student.roll_number == roll_number:
                del self.students[i]
                return True
        return False

    def list_all_students(self):
        if not self.students:
            print("No students available.")
            return
        print("\n--- ALL STUDENT RECORDS ---")
        for student in self.students:
            print("Roll:", student.roll_number, "| Name:", student.student_name)

    # ----------------- Reports -----------------
    def grade_distribution_report(self):
        grade_count = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
        for student in self.students:
            for s in student.subjects:
                grade_count[s['grade']] += 1

        print("\n--- GRADE DISTRIBUTION REPORT ---")
        for grade, count in grade_count.items():
            print("Grade", grade, ":", count)

    def class_topper_report(self):
        topper = max(self.students, key=lambda s: s.calculate_average(), default=None)
        if topper:
            print("\n--- CLASS TOPPER ---")
            print("Name:", topper.student_name)
            print("Roll No:", topper.roll_number)
            print("Average:", "{:.2f}".format(topper.calculate_average()))
        else:
            print("No students found.")

    def pass_fail_report(self):
        passed = sum(1 for s in self.students if s.calculate_average() >= 35)
        failed = len(self.students) - passed
        print("\n--- PASS / FAIL REPORT ---")
        print("Passed Students:", passed)
        print("Failed Students:", failed)

    # ----------------- Update/Search -----------------
    def update_student_name(self, roll_number):
        student = self.find_by_roll(roll_number)
        if student:
            student.student_name = input("Enter new name: ")
            print("Name updated successfully.")
        else:
            print("Student not found.")

    def search_student_by_name(self, search_name):
        found = False
        for s in self.students:
            if s.student_name.lower() == search_name.lower():
                show_subject_table(s.student_name, s.roll_number, s.subjects)
                found = True
        if not found:
            print("No student found with this name.")


# ------------------------ HELPER FUNCTIONS ------------------------

def input_student_data():
    roll_number = input("Enter Roll Number: ")
    student_name = input("Enter Full Name: ")
    student = Student(roll_number, student_name)

    for i in range(int(input("Enter total subjects: "))):
        subject_name = input("Enter subject name: ")
        marks = float(input("Enter marks (0-100): "))
        if marks < 0 or marks > 100:
            print("[Warning]: Marks out of valid range!")

        # Inline grade calculation
        if marks >= 90: grade = "A"
        elif marks >= 80: grade = "B"
        elif marks >= 70: grade = "C"
        elif marks >= 60: grade = "D"
        elif marks >= 35: grade = "E"
        else: grade = "F"

        student.add_subject(subject_name, marks, grade)
    return student


def show_subject_table(name, roll_number, subjects):
    if not subjects: return
    b_line = "=" * 85
    print("\n" + b_line)
    print(f"RECORD FOUND FOR: {name}\t\tROLL NUMBER: {roll_number}")
    print(b_line)
    print("SUBJECT NAME           MARKS OBTAINED      FINAL GRADE")
    print("--------------------   ------------------  ------------")
    for s in subjects:
        print(s['name'].ljust(22) + f"{s['marks']:.2f}".ljust(20) + s['grade'])
    print(b_line)


# ------------------------ MAIN APP LOOP ------------------------

def main_app_loop():
    sm = StudentManager()
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
        if choice == "1": sm.add_student(input_student_data())
        elif choice == "2":
            r = input("Roll Number: ")
            s = sm.find_by_roll(r)
            if s:
                show_subject_table(s.student_name, s.roll_number, s.subjects)
                s.show_summary()
            else: print("Student not found.")
        elif choice == "3":
            print("Deleted" if sm.delete_student(input("Roll: ")) else "Not found")
        elif choice == "4": sm.list_all_students()
        elif choice == "5": sm.grade_distribution_report()
        elif choice == "6": sm.class_topper_report()
        elif choice == "7": sm.pass_fail_report()
        elif choice == "8": sm.update_student_name(input("Roll: "))
        elif choice == "9": sm.search_student_by_name(input("Name: "))
        elif choice == "10": break
        else: print("Invalid choice.")


if __name__ == "__main__":
    main_app_loop()
