required_age_at_school=5
x_age=input("Tell your age: ")
x_age=int(x_age)
#Question: can x goto school?
if x_age==required_age_at_school:
    print("Cngratulations! x can join the school")
elif (x_age>required_age_at_school):
    print("x should join higher secondary school")
else:
    print("x cannot join the school")
