#Logical operstors are either true or false
# equal to                      ==
# not equal to                  !=
# less than                     >
# greater than                  >            
# less than and equal to        <=
# greater than and equal to     >= 



print(4==4)
print(4!=4)
print(4>3)
print(3<4)
print(3<=5)
print(5>=3)

# Applications of logical operators
x_age=4
school_age_requirement=5
print(x_age==school_age_requirement)

# input function and logical operator
school_age_requirement=5
x_age=input("What is your age=" ) #input function
x_age=int(x_age) # to convert string to integer
print(type(x_age))
print(x_age==school_age_requirement) # logical operator
