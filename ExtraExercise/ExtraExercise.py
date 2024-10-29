# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:03:00 2024

@author: User
"""

from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring #`This imports the askstring function from the tkinter.simpledialog module
import os

# Define the main application
class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management")
        self.root.geometry("800x800")
        
        # Load student data from file
        self.student_file = "ExtraExercise.txt"
        self.students = self.load_data()

        # Define UI elements
        self.listbox = Listbox(root, width=80, height=15)
        self.listbox.pack(pady=20)
        
        self.load_button = Button(root, text="View Student Records", command=self.view_records)
        self.load_button.pack(pady=5)  # Added vertical padding between buttons

        self.sort_button = Button(root, text="Sort Student Records", command=self.sort_records)
        self.sort_button.pack(pady=5)
        
        self.add_button = Button(root, text="Add Student Record", command=self.add_record)
        self.add_button.pack(pady=5)
        
        self.delete_button = Button(root, text="Delete Student Record", command=self.delete_record)
        self.delete_button.pack(pady=5)
        
        self.update_button = Button(root, text="Update Student Record", command=self.update_record)
        self.update_button.pack(pady=5)

    def load_data(self):
        """Load student data from a text file."""
        students = []
        if os.path.exists(self.student_file):
            with open(self.student_file, "r") as f:
                for line in f:
                    student = line.strip().split(',')
                    if len(student) == 3:  # Expected format: Name,Code,Mark
                        students.append({"name": student[0], "code": student[1], "mark": student[2]})
        return students

    def save_data(self):
        """Save student data to the text file."""
        with open(self.student_file, "w") as f:
            for student in self.students:
                f.write(f"{student['name']},{student['code']},{student['mark']}\n")

    def view_records(self):
        """Display all student records in the listbox."""
        self.listbox.delete(0, END)
        for student in self.students:
            self.listbox.insert(END, f"Name: {student['name']}, Code: {student['code']}, Mark: {student['mark']}")

    def sort_records(self):
        """Sort student records and display in ascending or descending order."""
        order = askstring("Sort Order", "Enter 'asc' for ascending or 'desc' for descending:")
        if order == "asc":
            self.students.sort(key=lambda x: x['name'])
        elif order == "desc":
            self.students.sort(key=lambda x: x['name'], reverse=True)
        else:
            messagebox.showerror("Error", "Invalid input. Please enter 'asc' or 'desc'.")
            return
        self.view_records()

    def add_record(self):# In this the user will enter the new students name, code for the student and the marks of the new student
        """Add a new student record."""
        name = askstring("Input", "Enter Student Name:")
        code = askstring("Input", "Enter Student Code:")
        mark = askstring("Input", "Enter Student Mark:")
        if name and code and mark:
            self.students.append({"name": name, "code": code, "mark": mark})
            self.save_data()#when the user is done with the enter the information of the student then this line of code will save the data in the file
            self.view_records()
        else:
            messagebox.showerror("Error", "All fields are required.")

    def delete_record(self):#In this the user can delete the information of the student
        """Delete a student record by name or code."""
        identifier = askstring("Delete Record", "Enter Student Name or Code:")#in this line of code the user can delete the students information by entering the students name or the students code
        if identifier: #in this the function identifies the student by the name or code 
            self.students = [s for s in self.students if s['name'] != identifier and s['code'] != identifier]
            self.save_data()
            self.view_records()
        else:
            messagebox.showerror("Error", "Name or Code is required to delete a record.")

    def update_record(self):#in this the user can update any students information
        """Update an existing student record."""
        identifier = askstring("Update Record", "Enter Student Name or Code to update:")#the user have to enter the students name or the code to update the students information
        student = next((s for s in self.students if s['name'] == identifier or s['code'] == identifier), None)
        if student:# In this the user can update the students name or code of the student and the marks of the student 
            choice = askstring("Update Field", "Enter 'name' to update Name, 'code' for Code, or 'mark' for Mark:")
            if choice == "name":
                new_name = askstring("New Name", "Enter new name:")
                if new_name:
                    student['name'] = new_name
            elif choice == "code":
                new_code = askstring("New Code", "Enter new code:")
                if new_code:
                    student['code'] = new_code
            elif choice == "mark":
                new_mark = askstring("New Mark", "Enter new mark:")
                if new_mark:
                    student['mark'] = new_mark
            else:
                messagebox.showerror("Error", "Invalid option.")
                return
            self.save_data()
            self.view_records()
        else:
            messagebox.showerror("Error", "Student not found.")

# Main window
root = Tk()
app = StudentRecordApp(root)
root.mainloop()

