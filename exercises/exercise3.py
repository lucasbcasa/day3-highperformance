# Exercises for Day 3
#Numpy and inheritance

## 3. Examples on classes and inheritance in Python

#### a. Create a "Person" class which takes firstname and lastname as arguments to the constructor (```___init___```) and define a method that returns the full name of the person as a combined string.

class Person():
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def fullName(self): # Method that returns full name
        return self.firstname + " " + self.lastname
    
    def __str__(self): # Redefine str method so that when we ask 'print(person)' we get the full name
        return self.firstname + " " + self.lastname

#### b. Create a "Student" class which inherits from the "Person" class, takes the subject area as an additional argument to the constructor and define a method that prints the full name and the subject area of the student.

class Student(Person):
    def __init__(self, firstname, lastname, subject_area):
        Person.__init__(self, firstname, lastname)
        self.subject_area = subject_area
    def printNameSubject(self):
        print("Student: %s" % self.fullName())
        print("Subject Area: %s" % self.subject_area)

#### c. You should be able now to use your "Student" class like this:
# In [1]: from classroom import Student
# In [2]: me = Student('Benedikt', 'Daurer', 'physics') 
# In [3]: me.printNameSubject() 
# Benedikt Daurer, physics
if __name__ == "__main__":
    me = Student('Lucas', 'Baldo', 'physics')
    me.printNameSubject()

#### d. Create a "Teacher" class which also inherits from "Person", takes the name of the course (e.g. Python programming) as an argument and define a method that prints the full name of the teacher and the course he teaches. 

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        Person.__init__(self, firstname, lastname)
        self.course = course
        
    def printNameCourse(self):
        print("Teacher: %s" % self.fullName())
        print("Course Taught: %s" % self.course)