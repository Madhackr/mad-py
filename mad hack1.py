import os
import time
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
        
        
os.system("clear")

slowprint('''\033[91m
           __  __           _   _   _            _
          |  \/  | __ _  __| | | | | | __ _  ___| | ___ __
          | |\/| |/ _` |/ _` | | |_| |/ _` |/ __| |/ / '__|
          | |  | | (_| | (_| | |  _  | (_| | (__|   <| |
          |_|  |_|\__,_|\__,_| |_| |_|\__,_|\___|_|\_\_|
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 100)

slowprint('''\033[95m
            +--------------------------------------+
            | This Tool Install All Basic Packages |
            +--------------------------------------+
            | Coded By Mad Hackr | version :  2.0  |
            +--------------------------------------+''')

print ("                                            ")
choice = input("\033[93mDo You Want to Nexphisher [N/Y] : ")
if choice == 'N' : os.system ("exit")
if choice == 'Y' : os.system ("python mad hack2.py")