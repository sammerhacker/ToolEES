import os
import sys
import time
import cowsay

os.system("clear")
print ("\033[01;30m")
cowsay.milk("developer sayser EIEI[EES]")
def hack():
            start=input("\033[01;31mtool\033[01;37m/\033[01;34mcmd \033[01;37m: \033[01;31m")
            if start == "tool":
               os.system("python tool.py")
            if start == "cmd":
                print ("")
            else:
                 out=input ("\033[01;32mexit\033[01;37m? : \033[01;32my\033[01;37m/\033[01;31mn \033[01;37m=\033[01;31m: \033[01;32m")
                 if out == "y":
                    exit(0)
                 else:
                      hack()
hack()
os.system("clear")
help="""
\033[01;32mDEVELOPER \033[01;31mE E \033[01;33mS \033[01;32mCMD
\033[01;37m---------------------------------------------
\033[01;31m$\033[01;37msms \033[01;31m: \033[01;31mspem\033[01;33msms \033[01;37m50\033[01;31mapi
\033[01;31m$\033[01;37mcall \033[01;31m: \033[01;37mspem\033[01;31m call \033[01;37m1\033[01;31mapi
\033[01;31m$\033[01;37micon \033[01;31m: \033[01;37micon \033[01;31mEE\033[01;33mS
\033[01;31m$\033[01;37mddos \033[01;31m: \033[01;37mddos \033[01;31mhttp \033[01;37m- \033[01;31min \033[01;36mpython
\033[01;31m$\033[01;37mddosup \033[01;31m: \033[01;37m-
\033[01;31m$\033[01;37minstall \033[01;31m: \033[01;37minstall package
\033[01;31m$\033[01;37mcr \033[01;31m: \033[01;37mname \033[01;31madmin \033[01;31m(\033[01;37mMPCK\033[01;31m(\033[01;37m4\033[01;31m))
\033[01;31m$\033[01;37mkex password \033[01;31m: \033[01;37mpassword EES
\033[01;31m$\033[01;37mtool \033[01;31m: \033[01;37mtool \033[01;31mhack ee\033[01;37ms
\033[01;31m$\033[01;37mexit \033[01;31m: \033[01;37mexit \033[01;31m, \033[01;37mout
\033[01;37m---------------------------------------------
"""
no="\033[01;31m[*]\033[01;37m"
yes="\033[01;32m[*]\033[01;37m"
passx="""
\033[01;31mpassword\033[01;37m-\033[01;31mspem\033[01;33msms \033[01;37m: \033[01;31mEE\033[01;33mS
\033[01;31mddos \033[01;37m& \033[01;31mcall \033[01;37m& \033[01;37minstall \033[01;37m: \033[01;31mno password
"""
print(help)
try:
    while True:
           cmd=input("\033[01;32mDeveloper\033[01;37m@\033[01;31mEE\033[01;33mS\033[01;37m~\033[01;31m# \033[01;32m")
           if cmd == "help":
              print (" ")
              print (yes,cmd)
              time.sleep(0.2)
              print (help)
           if cmd == "cr":
              print (yes,cmd)
              time.sleep(0.2)
              print ("""
\033[01;32mBY \033[01;37m: \033[01;31mMPCK \033[01;37m- \033[01;31mEE\033[01;33mS
\033[01;37m-------------------------------------

\033[01;31mM \033[01;37m= \033[01;31mMING   \033[01;36mFB \033[01;31m: \033[01;37mรัฐภูมิ ฯ.
\033[01;31mP \033[01;37m= \033[01;31mPO     \033[01;36mFB \033[01;31m: \033[01;37mปี.โป้'ป นะค้าบ'บบ
\033[01;31mC \033[01;37m= \033[01;31mCUNG   \033[01;36mFB \033[01;31m: \033[01;37mIbtisam Jehkhong
\033[01;31mK \033[01;37m= \033[01;31msayser \033[01;36mFB \033[01;31m: \033[01;37mКороль Девсайсероль \033[01;31mand \033[01;37mКопытокопыт Галоп
""")
           if cmd == "sms":
              print (yes,cmd)
              time.sleep(0.2) 
              os.system("python upspy.py")
           if cmd == "call":
              print (yes,cmd)
              time.sleep(0.2)
              os.system("python call.py")
           if cmd == "ddos":
              print (yes,cmd)
              time.sleep(0.2)
              os.system ("python ddos.py")
           if cmd == "install":
              os.system ("sh install.sh")
           if cmd == "ls":
              print (yes,cmd)
              time.sleep(0.2)
              print ("\033[01;34m")
              os.system("ls")
           if cmd == "kex password":
              print (yes,cmd)
              time.sleep(0.2)
              print (passx)
           if cmd == "icon":
              os.system ("python ees.py")
           if cmd == "tool":
              os.system("python tool.py")
           if cmd == "exit":
              exit(0)
except:
       print ("^_^ thank you [exit good buy]")
