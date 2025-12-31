# student-management-system-with-refactoring


## Project Overview
This project demonstrates the **Extract Class** refactoring technique by moving from a procedural dictionary-based system to an Object-Oriented approach.

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
### Files
* `Before_refactoring.py`: The original legacy code.
* `Extract_class_refactoring.py`: The newly refactored code.
* `Rename Variable_refactoring`: The refacetor code by apply rename variable refactoring technique.
* `Extract_Method_refactoring`: Refactor the code BY Extract Method.

