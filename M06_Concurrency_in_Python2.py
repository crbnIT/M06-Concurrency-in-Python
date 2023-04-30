'''
Corbyn Eaker
M06_Concurrency_in_Python2.py
This program uses multiprocessing to create 3 processes that wait a random number of seconds and print the current time,
which is the problem assigned at the end of chapter 15 (15.1)
'''

# imports
import multiprocessing
from random import random
import time as t
from datetime import datetime

# function to be called when process are created, gets current time, formats and prints it
def randomthree():
    now = datetime.now()
    current_time = now.strftime('%H:%M:%S')
    print(current_time)

# interpreter entry point that calls to  function randomthree()
if __name__ == "__main__":
    # for loop to run it 3 times
    for n in range(3):
        # create process to call randomthree() function
        p = multiprocessing.Process(target=randomthree)
        p.start()
        # waits a random amount of time (between 0 and 1) before returning to the for loop
        t.sleep(random())

        