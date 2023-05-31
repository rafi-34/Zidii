#coding=utf-8

import os, sys, platform

os.system('https://chat.whatsapp.com/IAXLQFSJokUK70XtZzeH5D')

try:

    if sys.argv[1]=='update':

        os.system('rm -rf JUTT64.cpython-311.so JUTT32.cpython-311.so')

except:

    pass

os.system('rm -rf JUTT64.cpython-311.so KRS32.cpython-311.so')

os.system('git pull')

bit = platform.architecture()[0]

if bit == '64bit':

    if not os.path.isfile('JUTT64.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-JUTT/DATA/main/JUTT64.cpython-311.so > JUTT64.cpython-311.so') 

        os.system("chmod 777 JUTT64*")

        import JUTT64

    else:

        import JUTT64

elif bit == '32bit':

    if not os.path.isfile('JUTT32.cpython-311.so'):

        os.system('curl https://raw.githubusercontent.com/TEAM-JUTT/DATA/main/JUTT32.cpython-311.so > JUTT32.cpython-311.so')

        os.system("chmod 777 JUTT32*")

        import JUTT32

    else:

        import JUTT32

