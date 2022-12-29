print('performing basic calculator code:')
print('addition')
print('subtraction')
print('multiplication')
print('division')

choice=input('enter your choice:')
num1=int(input('enter your number1:'))
num2=int(input('enter your number2:'))
if choice=='1':
    print(num1+num2)
elif choice=='2':
    print(num1-num2)
elif choice=='3':
    print(num2/num1)
elif choice=='4':
    print(num1*num2)
else:
    print('your choice is wrong')    



