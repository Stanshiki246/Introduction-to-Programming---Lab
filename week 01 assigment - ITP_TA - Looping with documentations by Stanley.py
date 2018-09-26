num=int(input("Enter number: ")) #this code is used to input number for looping.
# this code is used for triangle-shaped looping on bottom-left side.
for g in range(0,num): # g is for columns.
    for h in range(0,g+1): # h is for printing "*".
        print("*",end="") # 'end=""' is used for making columns.
    print() # this code is used for making another rows.
# this code is used for triangle-shaped looping on bottom-right side.
for m in range(0,num): # m is for columns.
    for n in range(0,num-m):  # n is for spacings.
        print(" ",end="")
    for o in range(0,m+1): # o is for printing "*".
        print("*",end="") # 'end=""' is used for making columns.
    print() # this code is used for making another rows.
# this code is used for triangle-shaped looping on top-left side.
for i in range(0,num): # i is for columns.
    for j in range(0,num-i): # j is for printing "*".
        print("*",end="") # 'end=""' is used for making columns.
    print() # this code is used for making another rows.
# this code is used for triangle-shaped looping on top-right side.
for x in range(0,num):         # x is for columns.
    for z in range(0,x+1):   # z is for spacings.
        print(" ",end="")    # 'end=""' is used for making columns.
    for y in range(0,num-x):   # y is for printing "*".
        print("*",end="") # this code is used for making another rows.
    print() # this code is used for making another column.
# this code is used for pyramid-shaped looping.
for a in range (1,num):        # a is for columns.
    for b in range(1,num-a):   # b is for spacings.
        print(" ",end="")     # 'end=""' is used for making columns.
    for c in range(a*2-1,0,-1):  # c is for printing "*".
        print("*",end="") # this code is used for making another rows.
    print() # this code is for making another column.
#this code is used for diamond-shaped looping.
for d in range (1,num):    # d is for columns. # this code is used for pyramid-shaped looping.
    for e in range(1,num-d): # e is for spacings.
        print(" ",end="") # 'end=""' is used for making columns.
    for f in range(d*2-1,0,-1): # f is for printing "*".
        print("*",end="")
    print() # this is for making another column.
for d in range (1,num-1): #this code is used for reversal pyramid-shaped looping.
    for e in range(1,d+1):
        print(" ",end="")
    for f in range(((num-1)*2-1)-d*2,0,-1):
        print("*",end="")
    print() # this code is for making another rows.
