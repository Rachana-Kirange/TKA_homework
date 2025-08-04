class employee:
    def __init__(self, name, salary, phone):
        self.name = name
        self.salary = salary
        self.phone = phone
        
    def display(self):
        print("****------------Displaying Information of an employee------------****")
        print("The name of an employee :->", self.name)
        print("The Salary of an employee :->", self.salary)
        self.phone.display_phone()

class phone:        
    def __init__(self, Mob_No, Email):
        self.Mob_No = Mob_No
        self.Email = Email
    def display_phone(self):
        print("The Mobile number of an employee :->", self.Mob_No)
        print("The Email of an employee :->", self.Email)

Name = input("Enter Your Name :-")
Salary = input("Enter Your Salary :-")
No = eval(input("Enter Your Mobile Number :-"))
email = input("Enter Your Email :-")

p = phone(No, email)
emp = employee(Name, Salary, p)
emp.display()


'''
OUTPUT :-
Enter Your Name :- Rachana Kirange
Enter Your Salary :- 50000
Enter Your Mobile Number :- 7635489298
Enter Your Email :- rmkirange28gmail.com             
****------------Displaying Information of an employee------------****
The name of an employee :->  Rachana Kirange
The Salary of an employee :->  50000
The Mobile number of an employee :-> 7635489298
The Email of an employee :->  rmkirange28gmail.com
'''