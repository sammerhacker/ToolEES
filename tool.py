import os
import sys
import time
import cowsay
os.system("clear")
help="""
\033[01;32mDEVELOPER \033[01;31mE E \033[01;33mS \033[01;36mTOOL
\033[01;37m---------------------------------------------
\033[01;31m[\033[01;37m1\033[01;31m] \033[01;37msms \033[01;31m     : \033[01;31mspem\033[01;33msms \033[01;37m50\033[01;31mapi
\033[01;31m[\033[01;37m2\033[01;31m] \033[01;37mcall \033[01;31m    : \033[01;37mspem\033[01;31m call \033[01;37m1\033[01;31mapi
\033[01;31m[\033[01;37m3\033[01;31m] \033[01;37micon \033[01;31m    : \033[01;37micon \033[01;31mEE\033[01;33mS
\033[01;31m[\033[01;37m4\033[01;31m] \033[01;37mddos \033[01;31m    : \033[01;37mddos \033[01;31mhttp \033[01;37m- \033[01;31min \033[01;36mpython
\033[01;31m[\033[01;37m5\033[01;31m] \033[01;37mddosup \033[01;31m  : \033[01;37m-
\033[01;31m[\033[01;37m6\033[01;31m] \033[01;37minstall \033[01;31m : \033[01;37minstall package
\033[01;31m[\033[01;37m0\033[01;31m] \033[01;37mexit \033[01;31m    : \033[01;37mexit \033[01;31m& \033[01;37mout
\033[01;37m---------------------------------------------
\033[01;31mpass \033[01;37m= \033[01;31mEE\033[01;33mS
"""
def tool():
          os.system("clear")
          print (help)
          nam=input ("\033[01;31m[\033[01;32m•\033[01;31m]EE\033[01;33mS\033[01;31m>>>>> \033[01;32m")
          if nam == "1":
             os.system("python upspy.py")
          if nam == "2":
             os.system("python call.py")
          if nam == "3":
             os.system ("python ees.py")
             lou=input ("\033[01;37mb = baack =: ")
          if nam == "4":
             os.system ("python ddos.py")
          if nam == "6":
             os.system ("sh install.sh")
          if nam == "0":
             exit(0)
          else:
               tool()
tool()
