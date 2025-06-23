s = "  Hello, Rachana! 123 "
s2 = "coding is fun"
s3 = "12345"
s4 = "HELLO"
s5 = "hello"
s6 = "Hello Rachana"
s7 = "   "
s8 = "fruits, flowers, leafs"

# 1. Case Conversion
print("1. Case Conversion")
print(s2.upper())         
print(s4.lower())         
print(s6.title())         
print(s5.capitalize())    
print(s4.swapcase())      
print()

# 2. Searching & Finding
print("2. Searching & Finding")
print(s.find("Rachana"))    
print(s.rfind("l"))       
print(s.index("Rachana"))   
print(s.index("Python"))  # ValueError: substring not found
print(s.count("l"))       
print()

# 3. Checking Content
print("3. Checking Content")
print(s3.isdigit())       
print(s5.isalpha())       
print("abc123".isalnum()) 
print(s7.isspace())       
print(s4.isupper())       
print(s5.islower())       
print(s6.istitle())       
print()

# 4. Modifying Strings
print("4. Modifying Strings")
print(s.strip())          
print(s.lstrip())        
print(s.rstrip())      
print(s.replace("Rachana", "Rachu"))  
print("42".zfill(5))      
print("hello".center(10, "*"))  
print("hello".ljust(10, "-")) 
print("hello".rjust(10, "-"))  
print()

# 5. Splitting and Joining
print("5. Splitting and Joining")
print(s.split())     
print(s8.split(","))   
print("Line1\nLine2".splitlines())  
print("-".join(["A", "B", "C"]))   
print()

# 6. String Formatting
print("6. String Formatting")
name = "Rachana"
age = 20
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
print("Pi is %.2f" % 3.14159)  
print()

# 7. Encoding and Decoding
print("7. Encoding and Decoding")
encoded = "hello".encode("utf-8")
print(encoded)             
print(encoded.decode())   
