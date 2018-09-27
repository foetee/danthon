
import os

# open a file/create if exists.
# display all the dando #1-whatever.
# loop until quit. 
file = open('dando.txt', 'a+')

x = True
while x == True:
    os.system('clear')
    command = input('DANDO | Go - > ')

    if command[:1] == 'a':
        print('a')
        file.write(command[1:] + '/n')
    elif command == 'd':
        print('delete')
    elif command == 'q':
        print(exiting...)
        x = False
    else:
        print('nothing..')