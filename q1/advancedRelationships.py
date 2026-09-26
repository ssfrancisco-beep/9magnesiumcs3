class Student:
    def __init__(self, name):
        self.name = name
    def study(self, subjec):
        print(f"{self.name} is studying {subject}.")

class Student: 
    def __init__(self, name): 
        self.name = name 

    def study(self, subject): 
        print(f"{self.name} is studying {subject}.") 


class MagnesiumStudent(Student): 
    def __init__(self, name, dorm, alpClub, romanCatholic): 
        super().__init__(name)
        self.dorm = dorm 
        self.alpClub = alpClub 
        self.__romanCatholic = romanCatholic 
 
    def joinClub(self, club): 
        self.alpClub = club 
 
    def getDorm(self): 
        return self.dorm 
 
    def setRomanCatholic(self, status): 
        self.__romanCatholic = status

class MagnesiumAdviser:

    def __init__(self, name, unit, yearsOfService):
        self.name = name
        self.unit = unit
        self.yearsOfService = yearsOfService
        self.students = []

    def conductClass(self, time):
        print(f"{self.name} is conducting class at {time}.")

    def contactParent(self, parent):
        print(f"{self.name} contacted {parent}.")

    def monitorAttendance(self):
        print(f"{self.name} is monitoring attendance.")

    def addStudent(self, student):
        self.students.append(student)

adviser = MagnesiumAdviser("Mr. Don", "Computer Science", 15)

student1 = MagnesiumStudent("Shelsy", 2, "Arab Adab", True)
student2 = MagnesiumStudent("Basty", 1, "Sports Club", True)
student3 = MagnesiumStudent("Nat", 1, "Filipino CLub", False)

#Test 1 | Inheritance

print("\nTEST 1 | INHERITANCE")

print("\nParent Class: Student")
print("Child Class: MagnesiumStudent")

print("\nParent attribute used by child: Name")
print("Student name:", student1.name)

print("\nParent method used by child: Study") 
student1.study("Math")

print("\nChild-specific attributes: Dorm, ALP Club, Roman Catholic")
print("Dorm:", student1.dorm)
print("ALP Club:", student1.alpClub)
print("Roman Catholic:", student1._MagnesiumStudent__romanCatholic)

#Test 2 | Aggregation

print("\nTEST 2 | AGGREGATION")

print("\nAdviser:", adviser.name)
print("Students under adviser:")

adviser.addStudent(student1)
adviser.addStudent(student2)
adviser.addStudent(student3)

for student in adviser.students:
    print(student.name)

print("\nStudents' information through adviser relationship:")

for student in adviser.students:
    print(
        f"{student.name} is in Dorm {student.dorm}"
        f" and belongs to {student.alpClub}."
    )

#Test 3 | Dependency

print("\nTEST 3 | DEPENDENCY")

print("\nAdviser contacting another parent is an example of using another object temporarily.")
adviser.contactParent(student1.name + "'s parent")