# repInterval.py
from microbit import *

while True:
    seconds = int(input("Enter a time in seconds: "))
    reps = int(input("Enter a number of reps: "))
    
    while(reps > 0):
        counter=seconds
        print("Reps left: "+ str(reps) + "\n")
        
        while(counter>=0):
            print(str(counter))
            counter-=1
            sleep(1000)
        reps-=1
        print("\n")
