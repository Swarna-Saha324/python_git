print("Hello world")
name = "Alice"
print(f"Hello {name}")
print("This is my name is "+ name)
print("This is my name is ",name)
print("This is my name is {}".format(name))
print(type(name))
val = int(input("Enter your name: "))  # type casting
print(type(val))
sal=int (input("Enter your salary: "))
tax=sal*(0.1,0.2)[sal>50000]  #Cleaver IF
print("Your tax is: ", tax)
a= 10
b=2
print(a>=b) # greater than or equal to
print(a**b) # exponentiation power
print(a*b)  
po="""This is a multi-line comment"""
pu="""This is a single-line comment"""
print(po+pu) 
y=10
x=25.5 
print(x/y)
print(x//y) # floor division
print(x%y) # modulu
peri=input("Enter the perimeter of the rectangle: ")
print("The perimeter of the rectangle is: ", peri)
#implicit conversion variable type not needed  
# not>and>or 
color=input("Enter your color: ")
if color=="red":
    print("Stop")
elif color=="green":
    print("Go")
elif color=="yellow":
    print("Wait") #case sensitive
else:
    print("Invalid color")
    # relational operators return boolean values (True/False)
# conversion automatic
# type casting manual num = int("10")
