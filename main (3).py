#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import system, name
import itertools
import threading
import time
import sys
import datetime
from base64 import b64decode,b64encode
from datetime import date

expirydate = datetime.date(2022, 9, 24)
#expirydate = datetime.date(2021, 12, 30)
today=date.today()
green="\106"
neon="\106"
nc="\106"
purple="\106"
yellow="\106"
violet="\106"
def hero():
    def chalo():
        done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', 
'/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rhacking in the winzO.mobi server for next colour--------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

 
        time.sleep(0.1)
        done = True

    def chalo1():
         done = False
        #here is the animation
        def animate():
            for c in itertools.cycle(['|', 
'/', '-', '\\']):
                if done:
                    break
                sys.stdout.write('\rgetting the colour wait --------- ' + c)
                sys.stdout.flush()
                time.sleep(0.1)
            sys.stdout.write('\rDone!     ')

        t = threading.Thread(target=animate)
        t.start()

        #long process here
        time.sleep(0.1)
        done = True
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
    def getSum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum
    clear()
    y=1
    newperiod=period
    banner='Detection'
    numbers=[]
    while(y):
        clear()
        system(banner)
        print(f"{red}winzO.mobi hack                                                                                                    
verson 11.7")
        print(f"{yellow}Enter
",newperiod," parity price :")
        current=input()
        current=int(current)
        chalo()
        print("\n---------Successfully hacked the winzO server-----------")
        chalo1()
        print("\n---------Successfully got the colour -------------")
        print('\n')
        last2=str(current)[-2:]
         if(newperiod%2==0):
             sum=getSum(current)
             if(sum%2==0):
                 print(newperiod+1,:
   🔴,RED")
             else:
                 print(newperiod+1," : 
🟢,GREEN")
       else:
           sum=getSum(current)
           if(sum%2==0):
               print(newperiod+1," :
🔴,RED")
           else:
               print(newperiod+1," :
🟢,GREEN")
       newperiod+=1
       numbers.append(current)
       y=input("Do you want to Play :
press 1 and 0 to exit \n")
        if(y==0):
            y=False
        if (len(numbers)>11):
            clear()
            system('figlet Thank you!!')
            print("Play on next specified time!!")
            print("-----------Current Time UP----------")
            sys.exit(" \n \n \n
            #print(numbers)