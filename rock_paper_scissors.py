import random
from time import sleep

symbols = ['🪨','🧻','✂️']

print('You are bout to start a rock-paper-scissors game. Make your choice.')
for i in range(3):
    print(i, symbols[i])
usr_play = int(input('Enter your choice'))
cpu_play = random.randint(0,2)


if usr_play ==  cpu_play:
    print(symbols[usr_play], "It's a tie!", symbols[cpu_play])
elif usr_play == 0:
    if cpu_play == 2:
        print(symbols[usr_play], 'Rock smashes scissors! You win!', symbols[cpu_play])
    else:
        print(symbols[usr_play], 'Paper covers rock! You lose.', symbols[cpu_play])
elif usr_play == 1:
    if cpu_play == 0:
        print(symbols[usr_play], 'Paper covers rock! You win!', symbols[cpu_play])
    else:
        print(symbols[usr_play], 'Scissors cuts paper! You lose.', symbols[cpu_play])
elif usr_play == 2:
    if cpu_play == 1:
        print(symbols[usr_play], 'Scissors cuts paper! You win!', symbols[cpu_play])
    else:
        print(symbols[usr_play], 'Rock smashes scissors! You lose.', symbols[cpu_play])
else:
    print('Incorrect option. Please, input 0, 1 or 2.')
