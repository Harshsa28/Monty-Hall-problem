import random
no_switch = 0
switch= 0

'''
for i in range(10000):
    car_loc = random.randint(1,3) #obviously random
    my_choice = random.randint(1,3) #obviously random
    host = [1,2,3]
    host.remove(car_loc)
    if my_choice in host:
        host.remove(my_choice)
    host = random.choice(host)
    options = [1,2,3]
    options.remove(host)
    if car_loc == my_choice:
        no_switch += 1
    else:
        options.remove(my_choice)
        my_choice = options[0]
        if car_loc == my_choice:
            switch += 1
'''
# you can use both implementations: the above one and the below one
#above one is how the game is played actually
#below one is what actually goes on in the game

for i in range(10000):
    car_loc = random.randint(1,3)
    #my_choice = random.randint(1,3)
    my_choice = 1
    if my_choice == car_loc:
        no_switch += 1
    else:
        switch += 1

print(no_switch, " vs ", switch)
