#variable for 0-19.
tupp1=("one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen"
      ,"sixteen","seventeen","eighteen","nineteen")
#variable for twenty, thirty, fourty, fifty, sixty, seventy. eighty, and ninety.
tupp2=("twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
# variable for inputting 3 digits number.
x=input("Enter a three digit number: ")
if int(x) < 20: # numbers from 0 to 19.
    print(tupp1[int(x)-1]) # print number if it is lower than 20.
elif int(x) >= 20 and int(x) <= 99: # numbers from 20 to 99.
    y = int(x)/10 #to search the tens number like twenty, thirty, and other tens.
    z = int(x)%10 #to search the number unit number like one, two, and so on.
    print(tupp2[int(y)-2] + ' ' + tupp1[int(z)-1]) # print number if it is lower or equal to 99.
elif int(x) >= 100: # digits from 100 to 999.
    if int(x)%100 < 20 and int(x)%100 != 0: # checking if there is number between 1 and 19 in 3 digits.
        y = int(x)/100 #to search hundreds number.
        z = int(x)%100 #to search unit number between 1 and 19.
        # print number with hundreds number and unit number (between 1 and 19)
        print(tupp1[int(y)-1] + ' ' + 'hundred and' + ' ' + tupp1[int(z)-1])
    elif int(x)%100 == 0: # checking if there is hundreds number only.
        y = int(x)/100 #to search hundreds number.
        print(tupp1[int(y)-1]+ ' ' + 'hundred') # print number with hundreds number only.
    else:             # checking if the number exceeds 19 in  3 digits.
        y = int(x)/100 #to search hundreds number.
        z = int(x)%100 #to search tens and unit number.
        w = int(z)/10  #to search the tens number like twenty, thirty, and other tens.
        v = int(z)%10  #to search the number unit number like one, two, and so on.
        # print number with hundreds, tens, and unit number.
        print(tupp1[int(y)-1] + ' ' + 'hundred and' + ' ' +tupp2[int(w)-2] + ' ' +tupp1[int(v)-1])


