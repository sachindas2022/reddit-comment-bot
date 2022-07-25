from io import StringIO as SIO


# num = int(input("enter a number"))
#
# n = num
#
# while n > 10:
#
#     n = n // 10
#     if n==0:
#         print("{} is the first digit of {}".format(n,num))
#     else:
#         print("{} is the first digit of {}".format(n, num))
class A:
    def AA(self):
        print("Welcome To Suchitra")
    def BB(self):
        print("Welcome To Hyderabad")
    def CC(self):
        print("Welcome to Telangana")
class B:
    def AA(self):
        print("Welcome To Jaleswar")
    def BB(self):
        print("Welcome to Balasore")
    def CC(self):
        print("Welcome to Odisha")
class C(A):
    def AA(self):
        print("Welcome to Bhubaneswar")
class D(C):
    def BB(self):
        print("Overriding of Class C to class D")
class E():
    str1_1='Hello Welcome to Python'
    file1=SIO(str1_1)
    file1.read()
    print(file1)
# obj_A=A()
# obj_B=B()
obj_C=C()
obj_D=D()
obj_E=E()
for Persion in (obj_C,obj_D):
    Persion.AA()
    Persion.BB()
    Persion.CC()
