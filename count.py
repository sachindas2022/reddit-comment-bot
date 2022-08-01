class Student:
    co=0
    def __init__(self):
        Student.co=Student.co+1
for i in range(1000):
    s1=Student()
print("The Total Student capacity is\t : ",Student.co)