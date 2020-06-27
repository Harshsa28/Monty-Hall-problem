import random

no_switch = 0
switch = 0

for i in range(100000):
    my_choice = 1
    car_loc = random.randint(1,4)
    if my_choice == car_loc:
        no_switch += 1
    else:
        switch += 1

print("no_switch = ", no_switch)
print("switch = ", switch)
print("switch / possibilities = ", switch/2)
