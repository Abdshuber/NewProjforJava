# This student class with node class
class Student:
    
    def __init__(self, id, firstName, lastName, midExam,finalExam):
             
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.midExam = midExam
        self.finalExam=finalExam

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

# Node class for binary tree
class Node:
    def __init__(self, student):
        self.student = student
        self.left = None
        self.right = None

# Binary Tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, student):
        new_node = Node(student)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                total_score = student.get_total()
                if total_score <= current.student.get_total():
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def display_inorder(self, node):
        
        if node:
            self.display_inorder(node.left)
            # print(f"ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}")
            file2=open('print_inorder.txt','a')
            file2.write(f"\n ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}") 
            file2.close()
            self.display_inorder(node.right)
            
    def display_preorder(self,node):
        
        if node:
            # print(f"ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}")
            
            file2=open('print_preorder.txt','a')
            file2.write(f"\n ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}") 
            file2.close()
            
            self.display_preorder(node.left)
            self.display_preorder(node.right)

    def display_postorder(self,node):
        if node:
            self.display_postorder(node.left)
            self.display_postorder(node.right)
            
            file2=open('print_postorder.txt','a')
            file2.write(f"\n ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}") 
            file2.close()
            # print(f"ID: {node.student.id}, Name: {node.student.firstName} {node.student.lastName}, Total Score: {node.student.get_total()}")
    
    def delete(self, student):
        self.root = self._delete_recursive(self.root, student)

    def _delete_recursive(self, node, student):
        if node is None:
            return None

        if student.get_total() < node.student.get_total():
            node.left = self._delete_recursive(node.left, student)
        elif student.get_total() > node.student.get_total():
            node.right = self._delete_recursive(node.right, student)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.student = successor.student
                node.right = self._delete_recursive(node.right, successor.student)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current       
  