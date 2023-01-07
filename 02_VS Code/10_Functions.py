# Define function 
#1 way
def print_my_name():
    print("Arslan Ahmad")

print_my_name()

# 2 way 
def print_my_name():
    text="Muhammad Arslan Ahmad"
    print(text)

print_my_name()

# 3 way
def print_my_name(text):
    print(text)
print_my_name("Muhammad Arsla Ahmad")

# 4 way 
#  Defining a function with if elif and else statements
def school_age_calculator(age):
    if age==5:
        print("X can join the school")
    else:
        print("X cannot join the school")
school_age_calculator(5)

# Defining a function of future age 
def future_age(age):
    new_age=age+20
    return(new_age)
print(future_age(18))

