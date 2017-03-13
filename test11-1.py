import time

timer = int(input("Countdown timer: How many seconds ? \n"))

for i in range (timer, 0, -1):
    print i
    time.sleep(1)
print "BLAST OFF!"
