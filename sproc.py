import os, time, pexpect
import subprocess as sp

ires=sp.run('ls -la | grep .py', shell=1, stdout=sp.PIPE)

while 1:
    print(ires.stdout.rstrip())
    print(ires.returncode)
    time.sleep(1)
    print(pexpect.run('uptime').rstrip())
    time.sleep(0.9)
    sp.run('pwd')
    time.sleep(0.8)

