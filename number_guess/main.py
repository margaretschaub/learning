
from random import seed
from random import randint

import  time

seed(int(time.time()))


def number_generator():  #can put  upper  limit  in  ()
	value = randint(0,  100)  # can change  100 to upper  limit
	return value


def get_input():
	while True:
		try:
			prompt = "Please enter your guess between 1 and 100:"
			guess_int = int(input(prompt))
			assert 0 < guess_int < 101
			return guess_int
		except(ValueError, AssertionError):
			print("you are bad")


def compete(x, y):
	if x == y:
		return 0

	if x < y:
		return -1
	else:
		return 1


def main():
	y = number_generator()
	done = False
	guess_count = 0
	while not done:
		x = get_input()
		outcome = compete(x, y)
		guess_count +=1

		if outcome == 0:
			print(f"You win. Your guess count was {guess_count}")
			done = True
		elif outcome == -1:
			print("Try again. Guess higher")
		else:
			print("Try again. Guess lower")





main()

# def main():
#
# 	outcome = None
# 	while outcome != 0:
# 		outcome = compete_with_values()

