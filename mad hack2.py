import os
import time
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
        
        
os.system("clear")

os.system("git clone git://github.com/htr-technexphisher.git")

os.system("cd nexphisher")
os.system(" bash setup")
os.system("bash tmux_setup")
os.system("bash nexphisher")


