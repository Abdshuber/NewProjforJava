# This student wiout node class
class Student:
    
    def __init__(self, id, firstName, lastName, midExam,finalExam):
             
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.midExam = midExam
        self.finalExam=finalExam
        self.prev = None
        self.next = None

    def get_midExam(self):
     
             temp =int(self.midExam)  
             return temp
    
        
    def get_finalExam(self):
         
             temp =int(self.finalExam)
             return  temp
         
   
    def get_total(self):
        total=(self.get_finalExam() + self.get_midExam())
        return total
    
    def get_estimation(self):
        if int(self.get_total())>=90:
            return "Excellent"
        elif int (self.get_total())>=80 and int(self.get_total()) < 90:
            return " very Good"
        elif int(self.get_total())>=70 and int(self.get_total())<80:
            return "Good"
        elif int(self.get_total())<70 :
          return  "Bad Grade :< "
      
    def __str__(self) :
         
        return f"student ID: {self.id} ,fName:{self.firstName} ,lName:{self.lastName},midExam: {self.midExam},finalExam:{self.finalExam},total:{self.get_total()},estimation: {self.get_estimation()}"  
        # return f" {self.id} ,  {self.firstName} ,  {self.lastName},   {self.midExam},  {self.finalExam},  {self.get_total()},    {self.get_estimation()}"  

 
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.prev=None
        self.next=None
         
    def append(self, id, firstName, lastName, midExam,finalExam):
        new_Student = Student(id, firstName, lastName, midExam,finalExam)

        if self.head is None:
            self.head = new_Student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_Student
            new_Student.prev = current

    def add_first(self, id, firstName, lastName, midExam,finalExam):
        new_Student = Student(id, firstName, lastName, midExam,finalExam)
        if self.head is None:
            self.head = new_Student
        else:
            new_Student.next = self.head
            self.head.prev = new_Student
            self.head = new_Student

    def add_second(self, id, firstName, lastName, midExam,finalExam):
        new_Student = Student(id, firstName, lastName, midExam,finalExam)
        if self.head is None:
            self.head = new_Student
        elif self.head.next is None:
            self.head.next = new_Student
            new_Student.prev = self.head
        else:
            second_node = self.head.next
            self.head.next = new_Student
            new_Student.prev = self.head
            new_Student.next = second_node
            second_node.prev = new_Student

    def add_last(self, id, firstName, lastName, midExam,finalExam):
        self.append(id, firstName, lastName, midExam,finalExam)

 
    def delete_first(self):
        temp=None
        if self.head is None:
            return          # No items to delete
        else:
            if self.head.next is None:
                temp=self.head
                self.head = None
                return temp    
            else:
                temp=self.head
                self.head = self.head.next
                self.head.prev = None
                return temp
    
    def delete_last(self):
        temp=None
        current=self.head
        if current is None:
            return temp  # No items to delete
        else: 
            
            while current.next:
                  current=current.next  
            temp=current    
            current.prev.next=None
            current=None
            return temp

    def delete_second(self):
        temp =None
        if self.head is None or self.head.next is None:
            return  temp  # No items or only one item, nothing to delete
        else:
            if self.head.next.next is None:
                temp=self.head.next
                self.head.next = None
                self.tail = self.head
                return temp
            else:
                temp=self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                return temp        
    # print methods
     
     
    def length(self):
        
        current =self.head
        length_list=0
        while current:
            length_list+=1
            current=current.next
        return length_list    


    def print_unsorting(self):
      nodes=[]
      current = self.head
      if self.head is not None:  
        while current:
           nodes.append(current)
        #    print(current)             
           current = current.next

      else: return None 
     
      file1=open('print_unsorting.txt','a')
      current=nodes[0]
      index=0
      while index<self.length():
            file1.write( f"\n  {current}  \n ") 
            index+=1
            current=nodes[index]
      file1.close()

    def print_sorting(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next

        nodes.sort(key=lambda node: node.get_total())

        file2=open('print_sorting.txt','a')
        current=nodes[0]
        index=0
        while index<self.length():
                file2.write( f"\n  {current}  \n ") 
                index+=1
                current=nodes[index]
        file2.close()
                
 