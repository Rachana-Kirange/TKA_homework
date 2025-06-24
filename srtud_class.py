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


'''
OUTPUT :->
Information of student :->
Name : Rachana
Roll No : 10
subjects and marks : {'Math': 90, 'Python': 99, 'Java': 100, 'OS': 95, 'Data_Structure': 90}
Percentage : 94.8
'''