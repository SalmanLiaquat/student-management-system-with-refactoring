r_list = []

def get_student_data():
    
    r_num = ""
    s_name = ""
    n_sub = 0
    sub_count = 0
    g_result = ""
    
    print("\n--- STARTING DATA ENTRY FOR ONE STUDENT ---")
    
    r_num = input("Enter the Student's Roll Number (eg 101): ")
    s_name = input("Enter the student's Full Name: ")
    
    n_sub = int(input("Enter the total number of subjects for this student: "))

    s_record = {}
    s_record['R_N'] = r_num
    s_record['Name'] = s_name
    s_record['SubList'] = []
    
    while sub_count < n_sub:
        sub_count = sub_count + 1
        print("  > Subject Number " + str(sub_count) + " of " + str(n_sub) + ":")
        
        sub_name = input("    Enter the name of the subject: ")
        m_obtain = float(input("    Enter the marks obtained (e.g. 85.50): "))

        if m_obtain < 0 or m_obtain > 100:
            print("    [Warning]: Marks are out of valid range (0–100).")

        if m_obtain >= 90:
            g_result = "A"
        elif m_obtain >= 80:
            g_result = "B"
        elif m_obtain >= 70:
            g_result = "C"
        elif m_obtain >= 60:
            g_result = "D"
        elif m_obtain >= 35:
            g_result = "E"
        else:
            g_result = "F"

        s_record['SubList'].append({
            'N': sub_name,
            'M': m_obtain,
            'G': g_result
        })

    return s_record


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


def calculate_student_average(sub_data):
    total = 0
    count = 0

    for d in sub_data:
        total = total + d['M']
        count = count + 1

    if count == 0:
        return 0
    return total / count


def display_student_summary(student):
    avg = calculate_student_average(student['SubList'])
    
    print("\n--- STUDENT SUMMARY ---")
    print("Name:", student['Name'])
    print("Roll No:", student['R_N'])
    print("Total Subjects:", len(student['SubList']))
    print("Average Marks:", "{:.2f}".format(avg))

    if avg >= 85:
        print("Final Result: Excellent")
    elif avg >= 70:
        print("Final Result: Good")
    elif avg >= 50:
        print("Final Result: Average")
    else:
        print("Final Result: Needs Improvement")


def delete_student_record():
    global r_list
    r_no = input("Enter Roll Number to delete: ")
    found = False

    for i in range(len(r_list)):
        if r_list[i]['R_N'] == r_no:
            del r_list[i]
            found = True
            print("Record deleted successfully.")
            break

    if not found:
        print("No record found with this roll number.")


def list_all_students():
    if len(r_list) == 0:
        print("No students available.")
        return

    print("\n--- ALL STUDENT RECORDS ---")
    for s in r_list:
        print("Roll:", s['R_N'], "| Name:", s['Name'])


# ------------------ NEW LEGACY FUNCTIONS ADDED ------------------

def count_grade_distribution():
    grade_count = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}

    for s in r_list:
        for sub in s['SubList']:
            g = sub['G']
            if g in grade_count:
                grade_count[g] = grade_count[g] + 1

    print("\n--- GRADE DISTRIBUTION REPORT ---")
    for k in grade_count:
        print("Grade", k, ":", grade_count[k])


def find_topper():
    highest_avg = -1
    topper = None

    for s in r_list:
        avg = calculate_student_average(s['SubList'])
        if avg > highest_avg:
            highest_avg = avg
            topper = s

    if topper:
        print("\n--- CLASS TOPPER ---")
        print("Name:", topper['Name'])
        print("Roll No:", topper['R_N'])
        print("Average:", "{:.2f}".format(highest_avg))
    else:
        print("No students found.")


def pass_fail_report():
    pass_count = 0
    fail_count = 0

    for s in r_list:
        avg = calculate_student_average(s['SubList'])
        if avg >= 35:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    print("\n--- PASS / FAIL REPORT ---")
    print("Passed Students:", pass_count)
    print("Failed Students:", fail_count)


def update_student_name():
    roll = input("Enter Roll Number to update name: ")
    for s in r_list:
        if s['R_N'] == roll:
            new_name = input("Enter new name: ")
            s['Name'] = new_name
            print("Name updated successfully.")
            return
    print("Student not found.")


def search_by_name():
    name = input("Enter student name to search: ")
    found = False

    for s in r_list:
        if s['Name'].lower() == name.lower():
            display_table_data(s['Name'], s['R_N'], s['SubList'])
            found = True

    if not found:
        print("No student found with this name.")


# ------------------ MAIN LOOP ------------------

def main_app_loop():
    
    global r_list
    r_list = []

    print("\n*****************************************************************")
    print("* WELCOME TO THE STUDENT RECORD MANAGEMENT SYSTEM  *")
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
            added = 0
            while added < count:
                data = get_student_data()
                r_list.append(data)
                added = added + 1
                print("Student record added.")

        elif choice == "2":
            roll = input("Enter roll number to search: ")
            for s in r_list:
                if s['R_N'] == roll:
                    display_table_data(s['Name'], s['R_N'], s['SubList'])
                    display_student_summary(s)
                    break
            else:
                print("Student not found.")

        elif choice == "3":
            delete_student_record()

        elif choice == "4":
            list_all_students()

        elif choice == "5":
            count_grade_distribution()

        elif choice == "6":
            find_topper()

        elif choice == "7":
            pass_fail_report()

        elif choice == "8":
            update_student_name()

        elif choice == "9":
            search_by_name()

        elif choice == "10":
            print("Exiting application...")
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main_app_loop()
