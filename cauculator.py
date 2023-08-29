print('===================================================Welcome to Mind mending math=================================\
=================================')
while True:
    num1 = input('1st number')
    num2 = input('2nd number')
    opp = input('operation,1=+,2=-,3=x,4=division')

    if opp == '1':
        print("It is:", int(num1) + int(num2))
    elif opp == '2':
        print("It is:", int(num1) - int(num2))
    elif opp == '3':
        print("It is:", int(num1) * int(num2))
    elif opp == '4':
        print("It is:", int(num1) / int(num2))
    print('===========New eqation===============')
'''
This takes num1 and num2 and opp.
then the if statement looks at the value of opp and looks at what it stores 1,2,3 or 4.
1 = +, 2 = -, 3 = X, 4 = division.

'''
