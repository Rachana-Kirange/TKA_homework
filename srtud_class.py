class student:
    def __init__(self, nm, r, sub):
        self.Name = nm
        self.Roll = r
        self.subject = sub 
        
    def display(self):
        total_marks = sum(self.subject.values())
        num_subjects = len(self.subject)
        percentage = (total_marks / (num_subjects * 100)) * 100
        print("Information of student :->" )
        print("Name :",self.Name)
        print("Roll No :",self.Roll)
        print("subjects and marks :", self.subject)
        print("Percentage :",percentage)

d = {"Math" : 90, "Python" : 99, "Java" : 100, "OS" : 95, "Data_Structure" : 90}
s = student("Rachana", 10, d)
s.display()
d1 = {"Math" : 81, "Python" : 90, "Java" : 87, "OS" : 85, "Data_Structure" : 90}
s1 = student("Dimpal", 11, d1)
s1.display()
d2 = {"Math" : 70, "Python" : 90, "Java" : 89, "OS" : 90, "Data_Structure" : 80}
s2 = student("Ujwal", 12, d2)
s2.display()
d3 = {"Math" : 88, "Python" : 93, "Java" : 90, "OS" : 77, "Data_Structure" : 82}
s3 = student("Dipti", 13, d3)
s3.display()
d4 = {"Math" : 60, "Python" : 78, "Java" : 76, "OS" : 85, "Data_Structure" : 56}
s4 = student("Kulashree" , 14, d4)
s4.display()


'''
OUTPUT :->
Information of student :->
Name : Rachana
Roll No : 10
subjects and marks : {'Math': 90, 'Python': 99, 'Java': 100, 'OS': 95, 'Data_Structure': 90}
Percentage : 94.8
Information of student :->
Name : Dimpal
Roll No : 11
subjects and marks : {'Math': 81, 'Python': 90, 'Java': 87, 'OS': 85, 'Data_Structure': 90}
Percentage : 86.6
Information of student :->
Name : Ujwal
Roll No : 12
subjects and marks : {'Math': 70, 'Python': 90, 'Java': 89, 'OS': 90, 'Data_Structure': 80}
Percentage : 83.8
Information of student :->
Name : Dipti
Roll No : 13
subjects and marks : {'Math': 88, 'Python': 93, 'Java': 90, 'OS': 77, 'Data_Structure': 82}
Percentage : 86.0
Information of student :->
Name : Kulashree
Roll No : 14
subjects and marks : {'Math': 60, 'Python': 78, 'Java': 76, 'OS': 85, 'Data_Structure': 56}
Percentage : 71.0
'''