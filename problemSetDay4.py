strength = 5
print('Your strength is 5!')
while strength <= 10:
    print(strength)
    strength += 1
print('You have grown too strong! Time for a new level!')
strength = 10
print('Your strength is 10!')
while strength >= 100:
    print(strength)
    strength -= 10
print('You have grown too weak! You must power up!')
mysteryNum = 5
guess = int('What is your guess?')
while(guess != mysteryNum):
    guess - int(input('Guess again!'))
print('Nice job! You got it!')