# 100 password hashing

from threading import Thread
import time

def Timer(name, delay, repeat):
    print("Timer:: "+ name )
    while repeat >0:
        time.sleep(delay)
        print(name + ":" + str(time.ctime(time.time())))
        repeat -= 1
    print("Timer "+ name)

def Main():
    t1 = Thread(target=Timer, args=("Timer1", 1, 4))
    t1.start()
Main()
