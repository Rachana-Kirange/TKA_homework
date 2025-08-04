l = [10, 20, 30, 40]
l1 = ["Rachana", "Dimpal", "Ujwal", 50,60]
t = (1,2,3,4)
t1 = ("Rachu", "Dipti", "Sidhhesh", 10, 20)
s = {12, 13, 14, 15}
s1 = {"Kulu", "Roshani", "Saurabh",77, 66}
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
d1 = {"Flower":"Rose", "Fruit":"Mango","4": 55}
d2 = {"1" : 29, "2" : 25, "3" : 7}
r1 = range(5)
r2 = range(3)

print("Performing + operator in all types of datatype :-")
print("Adding list to list",l+l1)
# print(l+t)  #TypeError: can only concatenate list (not "tuple") to list
# print(l+s)    #TypeError: can only concatenate list (not "set") to list
print("Adding tuple to tuple",t+t1)
# print(t+s)     #TypeError: can only concatenate tuple (not "set") to tuple
# print(s + s1)    #TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(fs1+fs2)   #TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
# print(d1 + d2)   #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
# print(l+d1)      #TypeError: can only concatenate list (not "dict") to list
print("Range to List +:", list(r1) + list(r2))
print("Range to List * 2:", list(r1) * 2)


print("Performing - operator in all types of datatype :-")
# print("Range to List -:", list(r1) - list(r2))  #TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(l - l1)   #TypeError: unsupported operand type(s) for -: 'list' and 'list'
# print(t - t1)     #TypeError: unsupported operand type(s) for -: 'tuple' and 'tuple'
print("substracting set from set",s - s1)      
print("substracting set 's' from set 's1'",s1 - s)       
#print(d1 - d2)      #TypeError: unsupported operand type(s) for -: 'dict' and 'dict'
# print(l - s)      #TypeError: unsupported operand type(s) for -: 'list' and 'set'
print("substracting frozenset from frozenset",fs1 - fs2)    
print("substracting frozenset from frozenset",fs2 - fs1)    
# print(r1 - r2)    #TypeError: unsupported operand type(s) for -: 'range' and 'range'


print("Performing * operator in all types of datatype :-")
# print(l * l1)    #TypeError: can't multiply sequence by non-int of type 'list'
print("Multiplying list to 2",l * 2)   
print("Multiplying list to 2",l1 * 2)  
print("Multiplying tuple to 2",t * 2)  
print("Multiplying tuple to 2",t1 * 2) 
# print(s * 2)  #{TypeError: unsupported operand type(s) for *: 'set' and 'int'
# print(s1 * s)   #TypeError: unsupported operand type(s) for *: 'set' and 'set'
# print(d1 * d2 )  #TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
# print(d1 * 2)   #TypeError: unsupported operand type(s) for *: 'dict' and 'int'