tank = float (input("Size of tank: "))
percent = float(input("percent full: "))
percent = percent /100

print("km per liter : 10")

total = tank * percent * 10
print("You can go another ",total," km")
print("The next gas station is 200km away")
if total >= 205:
    print("You can wait for the next station.")
elif total < 205:
    print("get gas now!")
