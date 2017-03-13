import time

timer = int(input("Countdown timer: How many seconds ? \n"))

for i in range (timer, 0, -1):
    print i,
    for i in range (0, i):
        print '*',
    time.sleep(1)
    print
print "BLAST OFF!"
