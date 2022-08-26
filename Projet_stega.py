
import sys
import os
from time import sleep

def banner():
    print("""███████╗████████╗███████╗ ██████╗  █████╗     ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗
██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝
███████╗   ██║   █████╗  ██║  ███╗███████║    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║   
╚════██║   ██║   ██╔══╝  ██║   ██║██╔══██║    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║   
███████║   ██║   ███████╗╚██████╔╝██║  ██║    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║   
╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝   """)




cl = 'cls' if sys.platform == 'win32' else 'clear'
while True:
    try:
        sleep(1)
        os.system(cl)
        banner()
        print('1.stega low security')
        print('2.stega medium security')
        if sys.platform == 'win32':
            print('3.stega high security windows')
        else:
            print('3.stega high security linux')
        print()
        print(' ###')
        print()
        print('4.decrypt 1 and 2')
        print('5.decrypt 3')
        a = int(input())
        if a == 1:
            from encrypt.stega1 import stega
            os.system(cl)
            stega()
        elif a == 2:
            from encrypt.stega2 import stega
            os.system(cl)
            stega()
        elif a == 3:
            if sys.platform == 'win32':
                from encrypt.stega3_win import stega
                os.system(cl)
                stega()
            else:
                from encrypt.stega3_lin import stega
                os.system(cl)
                stega()
        elif a == 4:
            from decrypt.decrypt1_2 import stega
            os.system(cl)
            stega()
        elif a == 5:
            if sys.platform == 'win32':
                from decrypt.decrypt3_win import stega
                os.system(cl)
                stega()
            else:
                from decrypt.decrypt3_lin import stega
                os.system(cl)
                stega()
    except KeyboardInterrupt:
        sys.exit('Good bye')