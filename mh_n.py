import random

for n in range(3,20):
    no_switch = 0
    switch = 0
    for i in range(100000):
        my_choice = 1
        car_loc = random.randint(1,n)
        if my_choice == car_loc:
            no_switch += 1
        else:
            switch += 1
    print("n is :" , n)
    print("no_switch = ", no_switch)
    print("switch = ", switch)
    print("switch / possibilities = ", switch/(n-2))
