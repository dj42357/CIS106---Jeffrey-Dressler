class Student:
  def __init__(self, first, last, district, credit):
    self.first = first
    self.last = last
    self.district = district
    self.credit = credit
    self.tuition = float(credit) * 250 if district == "I" else float(credit) * 500

stu1 = Student('Jeff','Dressler','I',12)
stu2 = Student('John','Doe','O',5)

#In district test
print("")
print("-Student 1-")
print("First name:",stu1.first)
print("Last name:",stu1.last)
print("District (I/O):",stu1.district)
print("# of credits:",stu1.credit)
print("Tuition cost: ${}".format(stu1.tuition))

#Out of district test
print("")
print("-Student 2-")
print("First name:",stu2.first)
print("Last name:",stu2.last)
print("District (I/O):",stu2.district)
print("# of credits:",stu2.credit)
print("Tuition cost: ${}".format(stu2.tuition))