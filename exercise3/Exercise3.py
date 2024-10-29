import tkinter as tk
from tkinter import messagebox

# Function to load student data from the file
def load_student_data(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        num_students = int(lines[0].strip())
        students = []
        for line in lines[1:num_students+1]:
            data = line.strip().split(',')
            student_code = data[0].strip()
            name = data[1].strip()
            marks = list(map(int, data[2:]))
            students.append((student_code, name, marks))
        return students
    except Exception as e:
        messagebox.showerror("Error", f"Could not load student data: {e}")
        return []

# Function to calculate the total score for each student
def calculate_total_score(marks):
    course_total = sum(marks[:3])  # sum of 3 course marks out of 20
    exam_score = marks[3]          # examination mark out of 100
    return course_total + exam_score

# Function to determine the grade based on the total score
def calculate_grade(total_score):
    if total_score >= 70:
        return 'A'
    elif total_score >= 60:
        return 'B'
    elif total_score >= 50:
        return 'C'
    elif total_score >= 40:
        return 'D'
    else:
        return 'F'

# Function to display all student records
def view_all_students():
    records_text.delete('1.0', tk.END)
    records_text.insert(tk.END, "Student Records:\n\n")
    for student in students:
        code, name, marks = student
        total = calculate_total_score(marks)
        grade = calculate_grade(total)
        records_text.insert(tk.END, f"Code: {code}, Name: {name}, Marks: {marks}, Total Score: {total}, Grade: {grade}\n")

# Function to view an individual student record by code
def view_individual_student():
    student_code = entry_student_code.get().strip()
    for student in students:
        code, name, marks = student
        if code == student_code:
            total = calculate_total_score(marks)
            grade = calculate_grade(total)
            messagebox.showinfo("Student Record", f"Code: {code}\nName: {name}\nMarks: {marks}\nTotal Score: {total}\nGrade: {grade}")
            return
    messagebox.showerror("Error", "Student not found!")

# Function to show student with highest total score
def show_highest_score():
    highest_student = max(students, key=lambda s: calculate_total_score(s[2]))
    code, name, marks = highest_student
    total = calculate_total_score(marks)
    grade = calculate_grade(total)
    messagebox.showinfo("Highest Score", f"Code: {code}\nName: {name}\nMarks: {marks}\nTotal Score: {total}\nGrade: {grade}")

# Function to show student with lowest total score
def show_lowest_score():
    lowest_student = min(students, key=lambda s: calculate_total_score(s[2]))
    code, name, marks = lowest_student
    total = calculate_total_score(marks)
    grade = calculate_grade(total)
    messagebox.showinfo("Lowest Score", f"Code: {code}\nName: {name}\nMarks: {marks}\nTotal Score: {total}\nGrade: {grade}")

# Load student data from the file
students = load_student_data('studentMarks.txt')

# GUI setup
window = tk.Tk()
window.title("Student Records Manager")

# Menu label
menu_label = tk.Label(window, text="Student Records Manager", font=('Arial', 16))
menu_label.pack()

# Buttons for each menu option
view_all_button = tk.Button(window, text="1. View All Student Records", command=view_all_students, font=('Arial', 12))
view_all_button.pack(pady=5)

entry_label = tk.Label(window, text="Enter Student Code for Individual Record:", font=('Arial', 12))
entry_label.pack()
entry_student_code = tk.Entry(window, font=('Arial', 12))
entry_student_code.pack(pady=5)

view_individual_button = tk.Button(window, text="2. View Individual Student Record", command=view_individual_student, font=('Arial', 12))
view_individual_button.pack(pady=5)

highest_score_button = tk.Button(window, text="3. Show Student with Highest Total Score", command=show_highest_score, font=('Arial', 12))
highest_score_button.pack(pady=5)

lowest_score_button = tk.Button(window, text="4. Show Student with Lowest Total Score", command=show_lowest_score, font=('Arial', 12))
lowest_score_button.pack(pady=5)

# Text box to display all student records
records_text = tk.Text(window, height=10, width=60, font=('Arial', 12))
records_text.pack(pady=10)

# Run the GUI loop
window.mainloop()
