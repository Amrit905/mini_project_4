# Student Performance Analytics Toolkit

# Global variable
count = 0

# Function to calculate total marks
def total_marks(marks):
    return sum(marks)

# Function to calculate average marks
def average_marks(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)

# Function to calculate grade
def grade(avg):
    if avg >= 75:
        return "Distinction"
    elif avg >= 60:
        return "First Division"
    elif avg >= 40:
        return "Pass"
    else:
        return "Fail"

# Function to add student details
def add_student(name, marks):
    return {
        "name": name,
        "marks": marks
    }

# Function to display student report
def student_report(s_id, data):
    marks = data["marks"]
    total = total_marks(marks)
    avg = average_marks(marks)
    result = grade(avg)

    print("\n---------------------------")
    print("rollno/id:",s_id)
    print("Name:", data["name"])
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Grade:", result)

# Using filter and map with lambda
def top_students(students):
    result = filter(
        lambda x: average_marks(x["marks"]) >= 75,
        students.values()
    )

    names = list(map(lambda x: x["name"], result))
    return names

# Using *args
def class_average(*marks):
    return sum(marks) / len(marks)

# Using **kwargs
def class_details(**details):
    for key, value in details.items():
        print(key, ":", value)

# Default and positional arguments
def student_info(sid, name="Unknown"):
    print("ID:", sid, "Name:", name)

# Recursion function
def sum_number(n):
    if n == 0:
        return 0
    return n + sum_number(n - 1)

# Scope example
def show_scope():
    x = 10
    print("Local variable:", x)

def change_count():
    global count
    count = count + 1

# Main program
def main():

    students = {}

    students["S101"] = add_student("amrit", [56,67, 88])
    students["S102"] = add_student("himanshi", [43, 88, 78])
    students["S103"] = add_student("khusi", [67, 26, 23])

    print("STUDENT PERFORMANCE REPORT")

    for sid, data in students.items():
        student_report(sid, data)

    print("\nTop Students:")
    print(top_students(students))

    print("\nClass Average:")
    print(class_average(75, 80, 95))

    print("\nRecursion:")
    print(sum_number(5))
    print(sum_number(3))
    print(sum_number(4))

    print("\nScope:")
    show_scope()

    print("\nStudent Information:")
    student_info("S101", "amrit")
    student_info("S102","himanshi")
    student_info("S103","khusi")

    print("\nClass Details:")
    class_details(subject="Python", passing_marks=40)

    change_count()
    print("Count:", count)


main()