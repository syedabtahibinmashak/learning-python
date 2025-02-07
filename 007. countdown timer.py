import math
import time
print("")
print("******************** Welcome to Python Countdown Timer ********************")
print("")
my_time = int(input("Input Time in Seconds: "))
print("")
for x in range(my_time,0,-1):
    hours = math.floor(x / 3600)
    minutes = math.floor(x / 60) % 60
    seconds = x % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("00:00:00")
print("")
print("******************************** Time's Up! *******************************")
