"""from tkinter import *
from tkinter import messagebox

frame_main=Tk()
frame_main.geometry('500x600')
frame_main.title('sample GUI ')

fram1=PanedWindow(frame_main ,orient=VERTICAL )
fram1.pack(fill=BOTH,expand=1)

fram2=PanedWindow(frame_main ,orient=VERTICAL)
fram2.pack(fill=BOTH,expand=1)                 



list=Listbox(fram1 ,selectmode=MULTIPLE)
for i in range(90):
    
    list.insert(i,i)

def  fun():
    messagebox.showinfo('any', list.curselection())

b1=Button(fram1,text='Toasdasp',bg='red',command=fun)
b2=Label(fram1,text='labelaasdasdsddown',bg='red')
b3=Label(fram1,text='label asdasd  ',bg='red')

fram1.add(b1)
fram1.add(b2)
fram1.add(b3)

b1.place(x=10,y=90)
b2.place(x=10,y=120)
b3.place(x=10,y=20)
list.place(x=150,y=10)


list1=Listbox(fram2 ,selectmode=MULTIPLE)
for i in range(90):
    
    list1.insert(i,i)

def  fun1():
    messagebox.showinfo('any', list1.curselection())

b4=Button(fram2,text='Toasdasp',bg='red',command=fun1)

b5=Label(fram2,text='labelaasdasdsddown',bg='red')
b6=Label(fram2,text='label asdasd  ',bg='red')

fram2.add(b4)
fram2.add(b5)
fram2.add(b6)
fram2.add(list1)

b4.place(x=10,y=90)
b5.place(x=10,y=120)
b6.place(x=10,y=20)
list1.place(x=150,y=10)
frame_main.mainloop()"""

# this fram to print all output of double linked list and show data
from tkinter import *
from tkinter import messagebox
import StudentClass as sc
import BinaryTree as tree

Students_listD = tree.BinaryTree()

frame_main=Tk()
frame_main.geometry('600x700')
frame_main.title('sample GUI ')
 
scrolbar=Scrollbar(frame_main)
  
scrolbar.pack(side=RIGHT,fill=Y)
 
list=Listbox(frame_main,yscrollcommand = scrolbar.set,width='300',height='450')
 
list.pack(side=LEFT,fill=BOTH)
btn10=Button(frame_main).pack()
# to fill the list 



# Add Students to the list using the new methods
stu1=sc.Student(1, 'abd1', "mode", 3,30) 
stu2=sc.Student(2, 'abd1', "mode", 10,40) 
stu3=sc.Student(3, 'abd2', "mode", 21,50) 
stu4=sc.Student(4, 'abd4', "mode", 52,10)
stu5=sc.Student(5, 'abd4', "mode", 23,12) 
stu6=sc.Student(6, 'abd5', "mode", 20,0)

binrytree=tree.BinaryTree()

binrytree.insert(stu1)
binrytree.insert(stu2)
binrytree.insert(stu3)
binrytree.insert(stu4)
binrytree.insert(stu5)
binrytree.insert(stu6)
 
current= binrytree.root
ind=0
while current:
    
     
    list.insert(ind,current)
    ind+=1    
    current=current.

for i in range(10):
    list.insert(i,i)


# make the items move with move scrollbar
scrolbar.config(command=list.yview)

frame_main.mainloop()


""" 
import mysql.connector as mysql

 #   to save the first or second or last from rigister page 

# solve the  class attrubute to save value of methods 

conn = mysql.connect(
    host="localhost",
    user="abdshuber",
    password="abdshuber",
    database="student_db"  # replace with your actual database name
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM student_information")  # replace with your actual table name
rows = cursor.fetchall()

print(rows)
# Close the cursor and connection
cursor.close()
conn.close()
"""