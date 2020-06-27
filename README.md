# Monty-Hall-problem
Used python to show generalized monty hall problem for 'n' doors

Redult in as expected: You should always switch

In case of n > 3, switch to any different door. The probability of winning on any other door than yours is higher

This is shown in the python implementation


P(not switching) = 1/n

P(switching) = (n-1)/((n)(n-2))

therefore P(switching) > P(not switching)


These numbers are also 'almost' confirmed in the python implementation

There are 2 versions to write code to implement MH problem

First one is to create list/dict representing the options

Then choose one

Then remove one [host removes one]

Then see whether you are correct or not

This is what happenns in the game when you play it


Second one is what actually happens inside the game

You randomly select from [1,n]

the car is randomly in [1,n]

host will remove door acc to problem, but we don't need to worry about it

if your option = car location, you win

otherwise, whatever happens, you should switch. Wherever the car is, that doesn't matter. It's not at your guess. So, switch

This implementation gives fast answers to the probabiity of switching and not switching


Math for the generalized version:

Without loss of generality, assume you choose door. Again, without loss of generality, assume host takes down 'n'-th door

Now, car can be from [1, n-1]

ci represents that car is in door i

hi represents host took down door i

xi represents you chose door i

since we chose door 1, P(x1) = 1

since host took down door 'n', P(hn) = 1

P(c1 | hn, x1) = P(c1, hn, x1) / P(hn, x1) = P(hn | c1, x1) * P(c1,x1) / P(hn | x1) = (1/(n-1)) * (1/n) / (1/(n-1)) = 1/n

for 2 <= j <= n-1

P(cj | hn, x1) = P(cj, hn, x1) / P(hn, x1) = P(hn | cj, x1) * P(cj, x1) / P(hn | x1) = (1/(n-2)) * (1/n) / (1/(n-1)) = (n-1)/(n(n-2))

If n < 3, the question becomes obsolete

Therefore P(cj | hn,x1) > P(c1 | hn, x1) for all n >= 3

Therefore, you should always switch
