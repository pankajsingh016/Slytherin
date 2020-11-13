#Tossing a coin and user can compare with his wish he want 
import random
a =input('Enter What you want-:')

b = random.randint(0,1)
if b==0:
    print('Your choice\n',a)
    print('Coins Comes with Heads\n')
    if a=='Heads'or a=='heads':
        print('Hurray! Lucky Day')
    else:
        print('Better Luck Next Time')
else:
    print('Your choice\n',a)
    print('Coin Comes with Tail\n')
    if a=='Tails'or a=='tails':
        print('Hurray! Lucky Day')
    else:
        print('Better Luck Next Time')
