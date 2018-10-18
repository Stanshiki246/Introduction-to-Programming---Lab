# Group 5 - Pasha, Stanley,Naufal, Wely
#Upside down pythagorean triangle
x= int(input("Enter the number of row(s):\n"))
#Variable for asterisk symbol
aster="*"
#Start triangle looping
for i in range(0,x+1):
    print( aster*(x-i)+" "*i)
