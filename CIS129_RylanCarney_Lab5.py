##Rylan Carney
##CIS 129 LAB 5
##03-13-2024
##This program collects total bottles collected and total payout earned /
##from bottles over 7 day period 


#This variables are constants

#This is for days
NBR_OF_DAYS = 7

#This is for payout calculation
PAY_PER_BTL = 0.10


#These are our delcared variables
total_bottles = 0

counter = 0

today_bottles = 0

total_payout = float(0)

#Our condition check variable
keep_going = 'y'

#Set our first while condition to loop when input is 'y'
while keep_going == 'y':

    total_bottles = 0

    counter = 0

    today_bottles = 0

    total_payout = float(0)

# set our second while statement to operate within our constant DAYS
    while counter < NBR_OF_DAYS:

        print('Enter number of bottles for day #', counter)

#Formula for collecting today's bottle count
        today_bottles = int(input())

#Day counter increase formula
        counter += 1

#Formula for counting total bottles within 7 day period
        total_bottles += today_bottles

#Formula for calculating total payout of all bottles
        total_payout = total_bottles * PAY_PER_BTL


#To display total numbers of bottles and payout to user
    print('The total number of bottles collected is', total_bottles)

    print(f'The total paid out is $,', total_payout)

    print()
    print()

    print('Do you want to enter another week\'s worth of data?')

#Our user input to repeat/end program
    keep_going = input('(Enter y or n)')

#Our conditional statement to repeat/end program
    if keep_going != 'y':
        break

    



    
         


    
    


