import mysql
import tkinter as tk

# Connect to the Oracle database
connection = mysql.connect(user="abdshuber", password="abd2001", host="hostname:3307/service_name")
# Create a cursor object to execute SQL statements
cursor = connection.cursor()

# Tkinter application code
def save_student():
    # Get student information from Tkinter input fields
    student_name = name_entry.get()
    student_age = age_entry.get()
    student_grade = grade_entry.get()

    # SQL statement to insert student information into the database
    insert_query = "INSERT INTO students (name, age, grade) VALUES (:name, :age, :grade)"

    # Execute the SQL statement with student information
    cursor.execute(insert_query, {"name": student_name, "age": student_age, "grade": student_grade})

    # Commit the transaction to save the changes
    connection.commit()

    # Clear the input fields after saving
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    
# فحص الربط 
# Create the Tkinter application window
window = tk.Tk()

# Create Tkinter input fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

grade_label = tk.Label(window, text="Grade:")
grade_label.pack()
grade_entry = tk.Entry(window)
grade_entry.pack()

save_button = tk.Button(window, text="Save", command=save_student)
save_button.pack()
 
window.mainloop()

 
cursor.close()
connection.close()





# SET PAGESIZE 20  
# SET LINESIZE 100  

# COLUMN username FORMAT A15  
# COLUMN default_tablespace FORMAT A15
# COLUMN temporary_tablespace FORMAT A15

 
# SELECT username, default_tablespace, temporary_tablespace
# FROM dba_users
# WHERE username LIKE 'APEX%';



# ''' 
# from StudentClass import *
# class Student:
#     def __init__(self, id, firstName, lastName, midExam, finalExam):
#         self.id = id
#         self.firstName = firstName
#         self.lastName = lastName
#         self.midExam = midExam
#         self.finalExam = finalExam
#         self.prev = None
#         self.next = None
    
#     def get_midExam(self):
#         temp = int(self.midExam)  
#         return temp
    
#     def get_finalExam(self):
#         temp = int(self.finalExam)
#         return temp
    
#     def get_total(self):
#         total = self.get_finalExam() + self.get_midExam()
#         return total
    
#     def get_estimation(self):
#         total = self.get_total()
#         if total >= 90:
#             return "Excellent"
#         elif 80 <= total < 90:
#             return "Very Good"
#         elif 70 <= total < 80:
#             return "Good"
#         else:
#             return "Bad Grade :<"
    
#     def __str__(self):
#         return f"Student ID: {self.id}, First Name: {self.firstName}, Last Name: {self.lastName}, Mid Exam: {self.midExam}, Final Exam: {self.finalExam}, Total: {self.get_total()}, Estimation: {self.get_estimation()}"


# class BinaryTree:
#     def __init__(self):
#         self.root = None
    
#     def insert(self, student):
#         if self.root is None:
#             self.root = student
#         else:
#             self._insert_recursive(student, self.root)
    
#     def _insert_recursive(self, student, current_node):
#         if student.get_total() < current_node.get_total():
#             if current_node.prev is None:
#                 current_node.prev = student
#             else:
#                 self._insert_recursive(student, current_node.prev)
#         else:
#             if current_node.next is None:
#                 current_node.next = student
#             else:
#                 self._insert_recursive(student, current_node.next)
#     def inorder_traversal(self):
#         self._inorder_recursive(self.root)
    
#     def _inorder_recursive(self, current_node):
#         if current_node is not None:
#             self._inorder_recursive(current_node.prev)
#             print(current_node)
#             self._inorder_recursive(current_node.next)
                        
# student1 = Student(1, "John", "Doe", 40, 30)
# student2 = Student(2, "Jane", "Smith", 25, 30)
# student3 = Student(3, "Alice", "Johnson", 35, 50)
# student4 = Student(4, "Bob", "Williams", 40, 50)
# student5=  Student(5,"Bob2", "Williams",10, 30)

# binaryList=BinaryTree()
# dubleList=DoublyLinkedList()

# binaryList.insert(student1)
# binaryList.insert(student2)
# binaryList.insert(student3)
# binaryList.insert(student4)
# binaryList.insert(student5)
# # 
# dubleList.append(1, "John", "Doe", 40, 30)
# dubleList.append(2, "Jane", "Smith", 25, 30)
# dubleList.append(3, "Alice", "Johnson", 35, 50)
# dubleList.add_first(4, "Bob", "Williams", 40, 50)
# dubleList.add_first(5,"Bob2", "Williams",10, 30)
 
# binaryList.inorder_traversal()

# print('------------------------------')
# current=dubleList.head
# while current  is not None:
#     print(current)
#     current=current.next
     

# # print(binaryList)
# ''' 