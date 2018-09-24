# this code is used for triangle-shaped looping on top-right side.
for x in range(0,10):         # x is for columns.
    for z in range(0,x+1):   # z is for spacings.
        print(" ",end="")    # 'end=""' is used for making rows.
    for y in range(0,10-x):   # y is for printing "*".
        print("*",end="")
    print() # this function is used for making another column.
# this code is used for pyramid-shaped looping.
for a in range (1,10):        # a is for columns.
    for b in range(1,10-a):   # b is for spacings.
        print(" ",end="")     # 'end=""' is used for making rows.
    for c in range(a*2-1,0,-1):  # c is for printing "*".
        print("*",end="")
    print() # this is for making another column.
#this code is used for diamond-shaped looping.
for d in range (1,10):    # d is for columns. # this code is used for pyramid-shaped looping.
    for e in range(1,10-d): # e is for spacings.
        print(" ",end="") # 'end=""' is used for making rows.
    for f in range(d*2-1,0,-1): # f is for printing "*".
        print("*",end="")
    print() # this is for making another column.
for d in range (1,9): #this code is used for reversal pyramid-shaped looping.
    for e in range(1,d+1):
        print(" ",end="")
    for f in range((9*2-1)-d*2,0,-1):
        print("*",end="")
    print() # this is for making another column.
