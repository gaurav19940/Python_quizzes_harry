import numpy as np
a = np.random.randint(34,75)
print('Guess the number in 10 attempts\n')
for i in range(10):
    b = int(input("Guess the number "))
    if b<a:
        print('you are low, Try again!\n')
    elif a<b:
        print("you crossed , Try again!\n")
    elif a==b:
        print("Congratsss ! \n Yoou got it ")
        print('with {} guesses'.format(i+1))
        break
    print((9-i),"guesses left")
else:
    print("\nYou lose!! , Game Over")
