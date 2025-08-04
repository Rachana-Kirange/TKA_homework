class A:
    def add(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Addition = ",a,"+",b,"=",a+b)
class B(A):
    def sub(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Substraction = ",a,"-",b,"=",a-b)
class C(A):
    def mult(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Multiplication = ",a,"*",b,"=",a*b)
class D:
    def div(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Division = ",a,"/",b,"=",a/b)
class E(B):
    def mod(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Addition = ",a,"%",b,"=",a%b)
class F(C,D):
    def floor(self):
        a = eval(input("Enter the number :-"))
        b = eval(input("Enter the number :-"))
        print("Floor Division = ",a,"//",b,"=",a//b)
e = E()
f = F()
e.add()
e.sub()
e.mod()
f.add()
f.div()
f.floor()
f.mult()