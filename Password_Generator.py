#Password Generator

import random
import pyperclip
from termcolor import colored
from os import system

print('''             ######                                                          
            #     #    ##     ####    ####   #    #   ####   #####   #####  
            #     #   #  #   #       #       #    #  #    #  #    #  #    # 
            ######   #    #   ####    ####   #    #  #    #  #    #  #    # 
            #        ######       #       #  # ## #  #    #  #####   #    # 
            #        #    #  #    #  #    #  ##  ##  #    #  #   #   #    # 
            #        #    #   ####    ####   #    #   ####   #    #  #####    ''')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!#@$%~'

number = int(input('How many do you want ? '))

length = int(input('Please enter the password length : '))

if __name__ == '__main__':
    try:
        system('cls')
    except KeyboardInterrupt as e:
        print('Good Bye')



for i in range(number):
    
    password = ''

    for c in range(length):

        password += random.choice(chars)
        pyperclip.copy(password)
        

    print(colored(f'{i+1} : {password}','blue'))   




        