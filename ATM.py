print('STATE BANK OF INDIA')
print('WELCOME')
print('please insert your card')
user='akhila chedri'
password=1924
user_name=input('please enter your username: ')  
pass_word=int(input('enter your password: '))
while True:
    if user_name==user and pass_word==password:
        amount=30000
        d='''
         1.DEPOSIT
         2.WITHDRAWAL
         3.TOTAL BALANCE
         4.EXIST
         '''
        print(d)
        print('please select your options')
        option=int(input('enter your option: '))
        if option==1:
            amount=30000
            deposit_amount=int(input('enter your amount: '))
            print('total amount:',deposit_amount+amount)
        elif option==2:
            withdrawal_amount=int(input('enter your amount:'))
            print('total amount:',amount-withdrawal_amount)
        elif option==3:
            print('total balance:',amount)
        elif option==4:
            break

    else:
        print(' invalid')


        