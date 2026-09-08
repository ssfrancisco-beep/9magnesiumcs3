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

student1 = MagnesiumStudent("Shelsy", 2, "Arab Adab", True)
student2 = MagnesiumStudent("Basty", 1, "Sports Club", True)

print("FROM THIS")
print(f"Student 1: {student1.name} | {student1.dorm} | {student1.alpClub}")
print(f"Student 2: {student2.name} | {student2.dorm} | {student2.alpClub}")

club = input("Enter the new club you want to join: ")
student1.joinClub(club)

print("TO THIS")
print(f"Student 1: {student1.name} | {student1.dorm} | {student1.alpClub}")
print(f"Student 2: {student2.name} | {student2.dorm} | {student2.alpClub}")
