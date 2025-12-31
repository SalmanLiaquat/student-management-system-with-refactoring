# Extract_Class_Refactoring.py

class Student:
    def __init__(self, roll_number, name):
        self.roll_number = roll_number
        self.name = name
        self.subjects = []

    def add_subject(self, subject_name, marks, grade):
        self.subjects.append({
            'N': subject_name,
            'M': marks,
            'G': grade
        })

    def calculate_average(self):
        total = 0
        count = 0
        for s in self.subjects:
            total += s['M']
            count += 1
        if count == 0:
            return 0
        return total / count

    def display_summary(self):
        avg = self.calculate_average()
        print("\n--- STUDENT SUMMARY ---")
        print("Name:", self.name)
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

    def find_by_roll(self, roll):
        for s in self.students:
            if s.roll_number == roll:
                return s
        return None

    def delete_student(self, roll):
        for i in range(len(self.students)):
            if self.students[i].roll_number == roll:
                del self.students[i]
                return True
        return False

    def list_all_students(self):
        if len(self.students) == 0:
            print("No students available.")
            return

        print("\n--- ALL STUDENT RECORDS ---")
        for s in self.students:
            print("Roll:", s.roll_number, "| Name:", s.name)

    def grade_distribution(self):
        grade_count = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
        for s in self.students:
            for sub in s.subjects:
                g = sub['G']
                if g in grade_count:
                    grade_count[g] += 1
        print("\n--- GRADE DISTRIBUTION REPORT ---")
        for k in grade_count:
            print("Grade", k, ":", grade_count[k])

    def class_topper(self):
        highest_avg = -1
        topper = None
        for s in self.students:
            avg = s.calculate_average()
            if avg > highest_avg:
                highest_avg = avg
                topper = s
        if topper:
            print("\n--- CLASS TOPPER ---")
            print("Name:", topper.name)
            print("Roll No:", topper.roll_number)
            print("Average:", "{:.2f}".format(highest_avg))
        else:
            print("No students found.")

    def pass_fail_report(self):
        pass_count = 0
        fail_count = 0
        for s in self.students:
            avg = s.calculate_average()
            if avg >= 35:
                pass_count += 1
            else:
                fail_count += 1
        print("\n--- PASS / FAIL REPORT ---")
        print("Passed Students:", pass_count)
        print("Failed Students:", fail_count)

    def search_by_name(self, name):
        found = False
        for s in self.students:
            if s.name.lower() == name.lower():
                display_table_data(s.name, s.roll_number, s.subjects)
                found = True
        if not found:
            print("No student found with this name.")

    def update_student_name(self, roll):
        for s in self.students:
            if s.roll_number == roll:
                new_name = input("Enter new name: ")
                s.name = new_name
                print("Name updated successfully.")
                return
        print("Student not found.")


# ------------------------ HELPER FUNCTIONS ------------------------

def get_student_data():
    print("\n--- STARTING DATA ENTRY FOR ONE STUDENT ---")

    roll = input("Enter Roll Number: ")
    name = input("Enter Full Name: ")
    total_subjects = int(input("Enter total subjects: "))

    student = Student(roll, name)

    for i in range(total_subjects):
        print("Subject", i + 1)
        sub_name = input("Enter subject name: ")
        marks = float(input("Enter marks (0-100): "))

        if marks < 0 or marks > 100:
            print("[Warning]: Marks out of valid range!")

        if marks >= 90:
            grade = "A"
        elif marks >= 80:
            grade = "B"
        elif marks >= 70:
            grade = "C"
        elif marks >= 60:
            grade = "D"
        elif marks >= 35:
            grade = "E"
        else:
            grade = "F"

        student.add_subject(sub_name, marks, grade)

    return student


def display_table_data(s_name, r_num, sub_data):
    if not sub_data:
        print("\n!ERROR!: No subject data found.")
        return

    b_line = "=" * 85
    print("\n" + b_line)
    print("RECORD FOUND FOR: " + s_name + "\t\tROLL NUMBER: " + r_num)
    print(b_line)

    print("SUBJECT NAME           MARKS OBTAINED      FINAL GRADE")
    print("--------------------   ------------------  ------------")

    for d in sub_data:
        m_str = "{:.2f}".format(d['M'])
        print(d['N'].ljust(22) + m_str.ljust(20) + d['G'])

    print(b_line)


# ------------------------ MAIN APP LOOP ------------------------

def main_app_loop():
    manager = StudentManager()

    print("\n*****************************************************************")
    print("* WELCOME TO THE STUDENT RECORD MANAGEMENT SYSTEM V1.0 ALPHA     *")
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
                student = get_student_data()
                manager.add_student(student)
                print("Student record added.")

        elif choice == "2":
            roll = input("Enter roll number to search: ")
            student = manager.find_by_roll(roll)
            if student:
                display_table_data(student.name, student.roll_number, student.subjects)
                student.display_summary()
            else:
                print("Student not found.")

        elif choice == "3":
            roll = input("Enter Roll Number to delete: ")
            if manager.delete_student(roll):
                print("Student record deleted.")
            else:
                print("Student not found.")

        elif choice == "4":
            manager.list_all_students()

        elif choice == "5":
            manager.grade_distribution()

        elif choice == "6":
            manager.class_topper()

        elif choice == "7":
            manager.pass_fail_report()

        elif choice == "8":
            roll = input("Enter Roll Number to update name: ")
            manager.update_student_name(roll)

        elif choice == "9":
            name = input("Enter student name to search: ")
            manager.search_by_name(name)

        elif choice == "10":
            print("Exiting application...")
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main_app_loop()
