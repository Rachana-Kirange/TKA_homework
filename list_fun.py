l = ["Rachana",29,29.07,True,"Kirange","July",1057]
print(type(l),l)
print(l.pop())
print(l)
#l.pop(29)    #IndexError: pop index out of range
l.pop(1)
print(l)
#print(l.remove())      #TypeError: list.remove() takes exactly one argument (0 given)
#print(l.remove(1))      #ValueError: list.remove(x): x not in list
l.remove(29.07)
print(l)