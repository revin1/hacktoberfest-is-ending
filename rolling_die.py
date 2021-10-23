import random
from time import sleep

print('Rolling... 🎲')
sleep(1)
usr_score = random.randint(1,6)
print('You got a', usr_score)
print()
print('CPU turn. Rolling... 🎲')
cpu_score = random.randint(1,6)
sleep(1)
print('CPU got a', cpu_score)
print()
if usr_score > cpu_score:
    print('😄 Congratulations! You won!')
elif usr_score < cpu_score:
    print('🥺 What a shame, you lost. Better luck next time!')
else:
    print('😮 It\'s a tie!')
