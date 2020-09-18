import random
random_number = random.randint(0, 100)

print(random_number)

name = input('Enter your name\n')
print('Hello, ', name, '!', sep="")

guess_number = 999

def random_number_guess():
  global guess_numbers

  while guess_number != random_number:
    guess_number = input('Try to guess random number between 0 and 100\n')
    guess_number = int(guess_number)
    if guess_number > random_number:
      print('Too high')
    elif guess_number < random_number:
      print('Too low')
    else:
      print('Just right')

random_number_guess()