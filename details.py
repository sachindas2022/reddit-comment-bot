class A:
    def __init__(self):
        print("Welcome")
    def Home(self,N,A,S):
        self.Name=N
        self.Area=A
        self.State=S
    def Drint(self):
        print("Name :",self.Name)
        print("Area",self.Area)
        print("State",self.State)
A1=A().Home(N=input("Enter Your Name :"),A=input("Enter Your Area :"),S=input("Enter Your State Name :"))
AA=A().Drint()