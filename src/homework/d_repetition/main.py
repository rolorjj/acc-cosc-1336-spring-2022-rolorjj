import repetition

choice = int(input('Homwework 3 Menu\n1-Factorial\n2-Sum odd numbers\n3-Exit'))

if(choice == 1):
    input = int(input('Enter a number between 1 and 10: '))
    if (input < 0 or input > 10):
        print('Enter a compatible number')
    else:
        print('Your factorial is ' + str(repetition.get_factorial(input)))
        
if(choice == 2):
    input = int(input('Enter a number between 1 and 100:'))
    if(input < 0 or input > 100):
        print('Enter a compatible number')
    else:
        print('Your total is ' + str(repetition.sum_odd_numbers(input)))
        
if(choice == 3):
    print('You are now exiting the menu.')
    
                  