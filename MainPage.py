from tkinter import *
from tkinter import messagebox
import StudentClass as sc
import BinaryTree as bt


class MainPageC():
    def __init__(self):
        self.add_event=None

    def set_add_event(self,val):
        self.add_event=val

    def get_add_event(self):
         return self.add_event        

obj=MainPageC()
        
def on_menu_select(item):
    obj.set_add_event(item)
    Rigster_fun()
    # frame_main.withdraw
    # frame_main.destroy()
 
def Rigster_fun():

        
            Rigister_fram=Tk()
            Rigister_fram.geometry('1300x700')

            Rigister_fram.title('Rigister Page ')
            
            
            #Info about page
            lb0=Label(Rigister_fram,text='Full All Information About New Student ',font=('verdana',16) ,fg='#58bff6').pack()

            # id
            lb1=Label(Rigister_fram,text='ID',font=3,fg='#58bff6')
            lb1.place(x=0,y=60)
            var_e1=StringVar()
            e1=Entry(Rigister_fram,textvariable=var_e1,font=3,justify=CENTER,bd=1 )
            e1.place(x=100,y=60) 

            # f_name
            lb2=Label(Rigister_fram,text='FirstName',font=3,fg='#58bff6')
            lb2.place(x=0,y=100)
            var_e2=StringVar()
            e2=Entry(Rigister_fram,textvariable=var_e2,font=3,justify=CENTER,bd=1)
            e2.place(x=100,y=100) 

            # lastname  
            lb3=Label(Rigister_fram,text='LastName',font=3,fg='#58bff6')
            lb3.place(x=0,y=140)
            var_e3=StringVar()
            e3=Entry(Rigister_fram,textvariable=var_e3,font=3,justify=CENTER,bd=1)
            e3.place(x=100,y=140) 

            # #  Mid exam  
            lb4=Label(Rigister_fram,text='MidExam',font=3,fg='#58bff6')
            lb4.place(x=0,y=180)
            var_sp=IntVar()
            sp=Spinbox(Rigister_fram ,textvariable=var_sp,font=3,width=16,from_=0,to=50  )
            sp.place(x=100,y=180)


            # #final exam
            lb5=Label(Rigister_fram,text='FinalExam',font=3,fg='#58bff6')
            lb5.place(x=0,y=220)
            var_sp1=IntVar()
            sp1=Spinbox(Rigister_fram ,textvariable=var_sp1,font=3,width=16,from_=0,to=50  )
            sp1.place(x=100,y=220)

            # # Total
            lb6=Label(Rigister_fram,text='Total',font=3,fg='#58bff6')
            lb6.place(x=0,y=260)
            var_e4=StringVar()

            e4=Entry(Rigister_fram,textvariable=var_e4,font=3,justify=CENTER,bd=1)
            e4.place(x=100,y=260) 
            e4.config(state="disabled")

            # #  Estimation
            lb7=Label(Rigister_fram,text='Estimation',font=3,fg='#58bff6')
            lb7.place(x=0,y=300)

            var_e5=StringVar()
            e5=Entry(Rigister_fram,textvariable=var_e5,font=3,justify=CENTER,bd=1)
            e5.place(x=100,y=300) 
            e5.config(state="disabled")
                
                 #add student and return to main page 
            def  Ok_fun():  
                        # add  new objdect                
                        
                    
                        if   obj.get_add_event().__eq__( 'first')   :
                            doublell.add_first(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get())
                            binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))      
                            list1.insert(END,doublell.head.__str__() )
                            
                        elif obj.get_add_event().__eq__('second'):
                            if doublell.head is not None: 
                                doublell.add_second(e1.get(), e2.get(),e3.get(),sp.get(), sp1.get())
                                binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))
                                list1.insert(END,doublell.head.__str__())
                            
                            else:messagebox.showerror("Error !!"," Try Add First Function")  
                        elif obj.get_add_event().__eq__('last')  :
                            if doublell.head is not None: 
                                doublell.add_last(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get())
                                binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))    
                                list1.insert(END,doublell.head.__str__())
                               
                            else:messagebox.showerror("Error !!"," Try Add First Function")  
                        else: messagebox.showerror('show Error','Enter correct data  !!')
                         
                        e1.delete(0, END)
                        e2.delete(0, END)
                        e3.delete(0, END)
                        e4.delete(0, END)
                        e5.delete(0, END)
                        sp.delete(0, END)
                        sp1.delete(0,END)
                         
                        file1=open('showdata.txt','a')
                        current=doublell.head
                        while current:
                                file1.write( f"\n{current}  \n ") 
                                current=current.next
                        file1.close()

                         
                        frame_main.mainloop()
                        Rigister_fram.withdraw
                        Rigister_fram.destroy()
                          
   
           
                
            def ignore_fun():

                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e4.delete(0, END)
                e5.delete(0, END)
                sp.delete(0,END)
                sp1.delete(0,END)
                #show the total and  Estimation in e4 e5
           
            def Result_fun():
                
                e4.config(state="normal")
                e5.config(state="normal")
                e4.delete(0, END)  
                e5.delete(0, END)  
                total=int(sp.get())+int(sp1.get())
                
                e4.insert(0, f"{total}")
                
                if int(total)>=90:
                    e5.insert(0,f"Excellent")
                    
                elif total>=80 and total < 90:
                    e5.insert(0, " very Good")
                elif total >= 70 and  total <80:
                    e5.insert(0, "Good")
                elif  total <70  and total > 60  :
                    e5.insert(0,  "Bad Grade :< ")
                else:e5.insert(0,"fiald !!")
                e4.config(state='readonly')
                e5.config(state='readonly')
                
                
            def More_fun():
                                                 
                        if   obj.get_add_event().__eq__('first'):
                            doublell.add_first(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get())
                            binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))
                            list1.insert(END,doublell.head.__str__())
                            
                        elif obj.get_add_event().__eq__('second'):
                            doublell.add_second(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get())
                            binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))
                            list1.insert(END,doublell.head.__str__())
                            
                        elif obj.get_add_event().__eq__('last')  :
                            doublell.add_last(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get())
                            binarytree.insert(bt.Student(e1.get(),e2.get(),e3.get(),sp.get(),sp1.get()))
                            list1.insert(END,doublell.head.__str__())
                             
                        else:messagebox.showeror('show Error','you are not selects add function  !!')

                        file1=open('showdata.txt','a')
                        current=doublell.head
                        while current:
                                file1.write( f"\n  {current}  \n ") 
                                current=current.next
                           
                        file1.close()
                         
                            
                        e1.delete(0, END)
                        e2.delete(0, END)
                        e3.delete(0, END)
                        e4.delete(0, END)
                        e5.delete(0, END)
                        sp.delete(0,END)
                        sp1.delete(0,END)
            # def save_file():
            #     file1=open('student_info.txt')
                
                
                    
            
                
            # btn OK
            btn1=Button(Rigister_fram,text='OK', width=10,fg='#58bff6',font=2,bd=1 ,command=Ok_fun)
            btn1.place(x=0,y=360)
            
            #  btn Ignore
            btn2=Button(Rigister_fram,text='Ignore', width=10,font=2,fg='#58bff6',bd=1,command=ignore_fun)
            btn2.place(x=120,y=360)

            # btn Result 
            btn3=Button(Rigister_fram,text='Result', width=10,fg='#58bff6',font=2,bd=1,command=Result_fun)
            btn3.place(x=240,y=360)

            #  btn More
            btn4=Button(Rigister_fram,text='More', width=10,fg='#58bff6',font=2,bd=1,command=More_fun)
            btn4.place(x=360,y=360)
            
            # btn4=Button(Rigister_fram,text="Save In File",width=10,fg='#58bff6',font=2,bd=1,command=save_file)
            
            
            scrolbar=Scrollbar(frame_main)            
            scrolbar.pack(side=RIGHT,fill=Y)
            list1=Listbox(Rigister_fram,yscrollcommand = scrolbar.set,width='90',height='30')

            list1.pack(side='right',fill=BOTH)
            
            scrolbar.config(command=list1.yview)
            
                    
            
            Rigister_fram.mainloop()


# '--------------------------------------------------------------------------------------------------------'
# '--------------------------------------------------------------------------------------------------------'

frame_main=Tk()
frame_main.geometry('1300x700')
frame_main.title('Main Page ')
menubar1=Menu(frame_main )
doublell=sc.DoublyLinkedList()
binarytree=bt.BinaryTree()


def minimum_page():
    frame_main.geometry('600x300')
    
def exit_fun():
    msg1=messagebox.showinfo('confirm message  ' ,"Thanks For Using My App" ) 
    frame_main.withdraw()
    frame_main.destroy()     
 
def del_at_first():
    if doublell.length()>0 and binarytree.root is not None:
        delf=doublell.delete_first()              
        binarytree.delete(delf)
    else:messagebox.showerror("Erorr","No Students To Delete")

def del_at_last():
    if doublell.length()>0 and binarytree.root is not None  :
        dell=doublell.delete_last()
        binarytree.delete(dell)    
    else:messagebox.showerror("Erorr","No Students To Delete")
def del_at_second():
    if doublell.length()>1 and  binarytree.root is not None :
        dels=doublell.delete_second() 
        binarytree.delete(dels)   
    else:messagebox.showerror("Erorr","No Students To Delete")
def printsorting():
     if doublell.length()>0:
        doublell.print_sorting()
     else:messagebox.showerror("Erorr","No Students To Print")
        
def printunsorting():
    if doublell.length()>0:
        doublell.print_unsorting()
    else:messagebox.showerror("Erorr","No Students To Print")
        
def printinorder():
    if binarytree.root is not None:
        binarytree.display_inorder(binarytree.root)
    else: messagebox.showerror("Erorr",' No Student To Print !! ')
def printpostorder():
    if binarytree.root is not None:
         binarytree.display_postorder(binarytree.root)    
    else: messagebox.showerror("Erorr",' No Student To Print !! ')
def printpreorder():
    if binarytree.root is not None:
         binarytree.display_preorder(binarytree.root)
    else: messagebox.showerror("Erorr",' No Student To Print !! ')

def showdata():
    import showData as shd
    shd.fun().mainloop()
    
    
    
 
contener=Label(frame_main,width=560 ,height=580,bg='#82e0aa').pack()    
lbl1=Label( contener,text='Data structure Project', font=35,width=35, height=2,bg='#5dade2'  ) 
lbl1.place(x=540,y=80)


lbl2=Label( contener,text='Worked By: ', font=35,width=35, height=2,bg='#5dade2' ) 
lbl2.place(x=540,y=120)


lbl2=Label( contener,text='Abd Mohammed Shuber  120210362', font=35,width=35, height=2,bg='#8686d0' ) 
lbl2.place(x=540,y=160)

btn11=Button( contener,text='Open file Students', font=35,width=35, height=2,bg='#8686d0',command=showdata )
btn11.place(x=540,y=240)

Inser_Menu=Menu(menubar1,tearoff=0,bg='#ebdef0')
Inser_Menu.add_command(label='At First',command=lambda: on_menu_select('first')) 
Inser_Menu.add_command(label='After second',command=lambda:  on_menu_select('second')) 
Inser_Menu.add_command(label='At Last',command= lambda: on_menu_select('last')) 



Delete_Menu=Menu(menubar1,tearoff=0)
Delete_Menu.add_command(label='Delete At First',command=del_at_first)
Delete_Menu.add_command(label='Delete After Second',command=del_at_second)
Delete_Menu.add_command(label='Delete At Last',command=del_at_last)


   
Print_Menu=Menu(menubar1,tearoff=0)
Print_Menu.add_command(label='Print Sorting List',command=printsorting)
Print_Menu.add_command(label='Print UNsorting List',command=printunsorting)
Print_Menu.add_command(label='Print Inorder',command=printinorder)
Print_Menu.add_command(label='Print Preorder',command=printpreorder)
Print_Menu.add_command(label='Print Postorder',command=printpostorder)

# Ready
Setting=Menu(menubar1,tearoff=0 )
Setting.add_command(label="Minmum Page", command=minimum_page)
Setting.add_command(label="Exit Page", command=exit_fun)

 

menubar1.add_cascade(label='Insert',menu=Inser_Menu,font=5)
menubar1.add_cascade(label='Delete',menu=Delete_Menu,font=5)
menubar1.add_cascade(label='Print',menu=Print_Menu,font=5)
menubar1.add_cascade(label='Setting',menu=Setting,font=5)


 
frame_main.config(menu=menubar1,bg='#9FE2BF' ) 
 
frame_main.mainloop()


 