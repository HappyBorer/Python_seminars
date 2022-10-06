from write_data import imp
from export import exp
from logo import log
from new_data import input_data
from delet_data import delet
def ask_user():
    print('1.Import')
    print('2.Export')
    print('3.Delete data')
    print('4.Exit')
    choice = int(input('Select the mode of work with data: '))
    while True:
        if not(0 < choice < 5):
            print('1.Import')
            print('2.Export')
            print('3.Delete data')
            print('4.Exit')
            choice = int(input('Not correctly selected mode, repeat the choice!: '))
            continue
        elif choice == 1:
            log(imp(input_data(), input('The path to the file: ')), choice)
        elif choice == 2:
            log(exp(input('Data for export: '), input('The path to the file: ')), choice)
        elif choice == 3:
            log(delet(input('Data for removal: '), input('The path to the file: ')), choice)
        else:
            exit = input('Want to get out of the application(Y/N): ')
            if exit.upper() == 'Y':
                return
        print('1.Import')
        print('2.Export')
        print('3.Delete data')
        print('4.Exit')
        choice = int(input('Select the mode of work with data:'))
