#!/usr/bin/python

# This script is to practice OOP(objected-oriented programming)
# MAIN POINTS/CONCEPTS are  Class, Object, Methods, Attributes, Constructor(__init__)  




class Country :   # define a class
  count=0       # define a class variable 'CLASS VARIABLE=GLOBAL VARIABLE'
   

  def __init__(self,name,gdp) : 
#defining a method is simiar as function, except the first argument must be 'self'    
     self.name=name
     self.gdp =gdp    # self maps to object, '.' is dot operator to access the attibutes of an object. 
     Country.count+=1  # Class variable
  def display(self)  :
     print 'the name is ',self.name


emp1=Country('CC','$1000')
emp2=Country('KK','$200')


emp1.display()     # call the display method
print 'the total country number is ', Country.count  # access the class variable




class Family : pass   # pass means "move along, noting to see here", a good placeholder.

my_family=Family()    # here, my_family is class. address and income is class varaibe.
my_family.address='Shandong' 
my_family.number='3'
print my_family.address
print my_family.number  



math_list=[]
class Exam :
   'to calculate the score'
   student_number=0  # define a class variable
   math_average=0    # another class variable
   def __init__(self, name,math, physics) : # contructor and attributes
      self.name=name
      self.math=math
      math_list.append(math)
      self.physics=physics
      Exam.student_number+=1
   def display(self) :  #define abstract METHOD,means it can apply to any object AND ONLY AFFECT OBJECTS.
      print 'name is ',self.name
      print 'math score', self.math
   
def calculate_math_average() :  # define a function
      Exam.math_average=sum(math_list)/len(math_list)
         
student1=Exam('Alice',90, 70)
student2=Exam('Bob',  80,82)


student1.display() # call the METHOD
student2.display()

calculate_math_average() # call the function
print 'the math average is ',Exam.math_average






   
