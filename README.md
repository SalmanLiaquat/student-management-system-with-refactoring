# student-management-system-with-refactoring


## Project Overview
This project demonstrates the **Extract Class,Rename Variables / Methods,Extract Method,Inline Method,Replace Temp with Query,Remove Dead Code, and Introduce Parameter Object** refactoring technique by moving from a procedural dictionary-based system to an Object-Oriented approach.

### Step 1: Extract Class
- **Problem:** Student data was stored in raw dictionaries, leading to poor encapsulation and high maintenance costs.
- **Solution:** Created `Student` and `StudentManager` classes to separate data from logic.

### Step 2: Rename Variables / Methods
- Renamed ambiguous variable names (e.g., `r_num` → `roll_number`)
- Renamed methods for clarity (e.g., `get_student_data()` → `input_student_data()`)
- Loop variables renamed for readability (`s` → `student`, `d` → `subject`)

### Step 3: Extract Method
- Split large blocks into smaller, meaningful methods
- `calculate_grade()`, `input_subject_data()`, and report helper methods
- Improved readability, reusability, and maintainability
- External behavior unchanged

### Step 4: Inline Method
- Inlined simple methods to reduce indirection:
  - `calculate_grade()` directly in `input_student_data()`
  - `_print_grade_distribution()` in `grade_distribution_report()`
  - `_calculate_pass_fail()` in `pass_fail_report()`
  - `_find_class_topper()` in `class_topper_report()`
- External behavior remains unchanged
- Improved code readability and reduced unnecessary method calls



