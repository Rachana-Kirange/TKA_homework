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
f.add()
f.div()
f.floor()
f.mult()


'''
OUTPUT :-
Enter the number :- 12
Enter the number :- 3
Addition =  12 + 3 = 15
Enter the number :- 123
Enter the number :- 34
Substraction =  123 - 34 = 89
Enter the number :- 34
Enter the number :- 4
Addition =  34 % 4 = 2
Enter the number :- 56
Enter the number :- 3
Addition =  56 + 3 = 59
Enter the number :- 456
Enter the number :- 4 
Division =  456 / 4 = 114.0
Enter the number :-42 
Enter the number :- 3
Floor Division =  42 // 3 = 14
Enter the number :-40 
Enter the number :- 4
Multiplication =  40 * 4 = 160
'''
