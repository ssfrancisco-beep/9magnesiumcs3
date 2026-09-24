class MagnesiumStudent:

    def __init__(self, name, dorm, alpClub, romanCatholic):
        self.name = name
        self.dorm = dorm
        self.alpClub = alpClub
        self.__romanCatholic = romanCatholic

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

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

print("\nBEFORE RELATIONSHIP")
print("\nAdviser:", adviser.name)
print("Unit:", adviser.unit)
print("Years of Service:", adviser.yearsOfService)

print("\nStudent 1:", student1.name)
print("Student 2:", student2.name)
print("Student 3:", student3.name)

print("\nBUILDING RELATIONSHIP")
print("Adding students to adviser")

adviser.addStudent(student1)
adviser.addStudent(student2)
adviser.addStudent(student3)

print("\nAFTER RELATIONSHIP")
print("Adviser:", adviser.name)
print("Students under adviser:")

for student in adviser.students:
    print("-", student.name)

print("\nACCESSING DATA THROUGH RELATIONSHIP")
for student in adviser.students:
    print(
        f"{student.name} is in Dorm {student.dorm}"
        f" and belongs to {student.alpClub}."
    )