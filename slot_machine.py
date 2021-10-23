import random
from time import sleep

symbols = ['🍋','🍒','7️']
print('Starting slot machine... 🎰')
for i in range(3):
    print(symbols[random.randint(0,2)], end = '')
    sleep(1)
