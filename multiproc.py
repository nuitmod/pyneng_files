#!/usr/bin/python3

import time, os
import pexpect, subprocess
import multiprocessing

def i_pr1():
    i=1
    while i<=8:
        idat=pexpect.run('pwd').rstrip()
        print("1p : i={} _ {}".format(i,idat))
        time.sleep(0.8)
        i+=1

def i_pr2():
    v=1
    while v<=8:
        idat=subprocess.run('uptime')
        print("2p : v={} _ {}".format(v,idat))
        time.sleep(1.2)
        v+=1

def iproc():
    p1=multiprocessing.Process(target=i_pr1, name="p1")
    p2=multiprocessing.Process(target=i_pr2, name="p2")
    print("1 process:")
    p1.start()
    time.sleep(1)
    print("2 process:")
    p2.start()
    p1.join()
    p2.join()
    print("process end!")

#i_pr1()
#i_pr_2()

iproc()
