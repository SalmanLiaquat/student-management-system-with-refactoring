# Inline_Method_Refactoring.py

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
        total_marks = sum(subject['marks'] for subject in self.subjects)
        subject_count = len(self.subjects)
        return total_marks / subject_count if subject_count else 0

    def show_summary(self):
        avg = self.calculate_average()
        print("\n--- STUDENT SUMMARY ---")
        print("Name:", self.student_name)
        print("Roll No:", self.roll_number)
        print("Total Subjects:", len(self.subjects))
        print("Average Marks:", "{:.2f}".format(avg))

        if avg >= 85:
            print("Final Result: Excellent")
        elif avg >= 70:
            print("Final Result: Good")
        elif avg >= 50:
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
        for i in range(len(self.students)):
            if self.students[i].roll_number == roll_number:
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
            for subject in student.subjects:
                grade_count[subject['grade']] += 1

        print("\n--- GRADE DISTRIBUTION REPORT ---")
        for grade, count in grade_count.items():
            print("Grade", grade, ":", count)

    def class_topper_report(self):
        highest_avg = -1
        topper = None
        for student in self.students:
            avg = student.calculate_average()
            if avg > highest_avg:
                highest_avg = avg
                topper = student

        if topper:
            print("\n--- CLASS TOPPER ---")
            print("Name:", topper.student_name)
            print("Roll No:", topper.roll_number)
            print("Average:", "{:.2f}".format(topper.calculate_average()))
        else:
            print("No students found.")

    def pass_fail_report(self):
        pass_count = 0
        fail_count = 0
        for student in self.students:
            if student.calculate_average() >= 35:
                pass_count += 1
            else:
                fail_count += 1
        print("\n--- PASS / FAIL REPORT ---")
        print("Passed Students:", pass_count)
        print("Failed Students:", fail_count)

    # ----------------- Update/Search -----------------
    def update_student_name(self, roll_number):
        student = self.find_by_roll(roll_number)
        if student:
            new_name = input("Enter new name: ")
            student.student_name = new_name
            print("Name updated successfully.")
        else:
            print("Student not found.")

    def search_student_by_name(self, search_name):
        found = False
        for student in self.students:
            if student.student_name.lower() == search_name.lower():
                show_subject_table(student.student_name, student.roll_number, student.subjects)
                found = True
        if not found:
            print("No student found with this name.")


# ------------------------ HELPER FUNCTIONS ------------------------

def input_student_data():
    print("\n--- STARTING DATA ENTRY FOR ONE STUDENT ---")
    roll_number = input("Enter Roll Number: ")
    student_name = input("Enter Full Name: ")
    student = Student(roll_number, student_name)

    total_subjects = int(input("Enter total subjects: "))
    for i in range(total_subjects):
        print("Subject", i + 1)
        subject_name = input("Enter subject name: ")
        marks_obtained = float(input("Enter marks (0-100): "))
        if marks_obtained < 0 or marks_obtained > 100:
            print("[Warning]: Marks out of valid range!")

        # ----------------- Inline Method: Grade Calculation -----------------
        if marks_obtained >= 90:
            grade = "A"
        elif marks_obtained >= 80:
            grade = "B"
        elif marks_obtained >= 70:
            grade = "C"
        elif marks_obtained >= 60:
            grade = "D"
        elif marks_obtained >= 35:
            grade = "E"
        else:
            grade = "F"
        # --------------------------------------------------------------------

        student.add_subject(subject_name, marks_obtained, grade)

    return student


def show_subject_table(student_name, roll_number, subjects):
    if not subjects:
        print("\n!ERROR!: No subject data found.")
        return
    b_line = "=" * 85
    print("\n" + b_line)
    print("RECORD FOUND FOR: " + student_name + "\t\tROLL NUMBER: " + roll_number)
    print(b_line)
    print("SUBJECT NAME           MARKS OBTAINED      FINAL GRADE")
    print("--------------------   ------------------  ------------")
    for subject in subjects:
        marks_str = "{:.2f}".format(subject['marks'])
        print(subject['name'].ljust(22) + marks_str.ljust(20) + subject['grade'])
    print(b_line)


# ------------------------ MAIN APP LOOP ------------------------

def main_app_loop():
    student_manager = StudentManager()
    print("\n*****************************************************************")
    print("* WELCOME TO THE STUDENT RECORD MANAGEMENT SYSTEM V4.0 ALPHA     *")
    print("*****************************************************************")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Enter New Student Records")
        print("2. Search Student by Roll Number")
        print("3. Delete Student Record")
        print("4. Display All Students")
        print("5. Grade Distribution Report")
        print("6. Class Topper")
        print("7. Pass/Fail Report")
        print("8. Update Student Name")
        print("9. Search Student by Name")
        print("10. Exit Program")

        choice = input("Enter your choice (1-10): ")

        if choice == "1":
            count = int(input("How many students do you want to add?: "))
            for _ in range(count):
                student = input_student_data()
                student_manager.add_student(student)
                print("Student record added.")
        elif choice == "2":
            roll_number = input("Enter roll number to search: ")
            student = student_manager.find_by_roll(roll_number)
            if student:
                show_subject_table(student.student_name, student.roll_number, student.subjects)
                student.show_summary()
            else:
                print("Student not found.")
        elif choice == "3":
            roll_number = input("Enter Roll Number to delete: ")
            if student_manager.delete_student(roll_number):
                print("Student record deleted.")
            else:
                print("Student not found.")
        elif choice == "4":
            student_manager.list_all_students()
        elif choice == "5":
            student_manager.grade_distribution_report()
        elif choice == "6":
            student_manager.class_topper_report()
        elif choice == "7":
            student_manager.pass_fail_report()
        elif choice == "8":
            roll_number = input("Enter Roll Number to update name: ")
            student_manager.update_student_name(roll_number)
        elif choice == "9":
            search_name = input("Enter student name to search: ")
            student_manager.search_student_by_name(search_name)
        elif choice == "10":
            print("Exiting application...")
            break
        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main_app_loop()
