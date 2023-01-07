# while and for loops

#while loops
x=0
while (x<5):
    print(x)
    x=x+1

#for loops

for x in range(5,10):
    print(x)

# arrays
days=["Mon","Tues","Wed","Thurs","Fri","Sat","Sun"]
for i in (days):
    # if (i=="Fri"):break # break stops the loop
    if (i=="Fri"):continue # continue skips i
    print(i)

