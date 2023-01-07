x=10            #Integer
y=10.5          #Float
z="Hello"       #STring

#Implicit type conversion
x=x*y
print(x, "Type of x is: " ,type(x))

#exlicit tye conversion
age=input("What is your age? ") #this age will be string not integer
age=int(age) #this will be integer
print(age, type(age))

#Name
name=input("What is your name? ")
print(name, type(str(name)))