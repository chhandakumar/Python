from random import randrange
import time

def gen_number():
	low = 1
	high = 100
	number = randrange(low, high)
	return int(number)


#The below method guesses if the number is equal to the guess or greater or lesser than the number and gives hint to the user
# based on the match.
def is_guessed_correctly(guess,number,numOfTries,guessedList):
	guess=int(guess)
	number=int(number)
	while guess != number:
		if guess > number:
			print("Guess #{} : {} - Higher!".format(numOfTries, guess))
			guess,numOfTries = get_input(numOfTries,guessedList)
		if guess < number:
			print("Guess #{} : {} - Lower!".format(numOfTries, guess))
			guess,numOfTries = get_input(numOfTries,guessedList)

	# let the user know they guess correct
	return right_guess(numOfTries,guess)



# function to get input and validate whether the input is an Integer between 1 to 100 otherwise ask user to re-enter
def get_input(numOfTries, guessedList):

	if(numOfTries==10):
		print("You have Lost the Game!")
		time.sleep(2)
		start_guessing()
	# check to make sure user input is a valid number otherwise ask the user to guess again
	while (numOfTries!=10):
		try:
			numOfTries = numOfTries + 1
			guess = int(input("Enter guess #"+str(numOfTries)+" between 1 and 100: "))

			if(guess>=1 and guess <=100 and guess not in guessedList):
				guessedList.append(guess)
				return guess,numOfTries

			else:
				if(guess<1 or guess>100):
					numOfTries = numOfTries - 1
					print("*** Incorrect Input: Must be in range from 1 to 100...")
					continue
				elif(guess in guessedList):
					numOfTries = numOfTries - 1
					print("*** You have Guessed this Number Already.")
					continue

		except ValueError:
			print("*** Invalid Input : Please try again...")
			numOfTries = numOfTries - 1
			continue

	# return guess if it is a valid number and number of attemps user took
	return guess,numOfTries

#The below method runs if the user guessed the right number and lets the user know he won the game and restart's the Game.
def right_guess(numOfTries,guess):
	print("Guess #"+str(numOfTries)+" : "+str(guess)+"- CORRECT!")
	print("YOU WIN!")
	print("Number Guessing Game ---------------- ")
	start_guessing()

#The below method, first generates the random input and gets the input from user,validates it, If any error an exception is throw
#otherwise if the number is guessed correctly the user Win's.
def start_guessing():

	guessedList=[]
	number = gen_number()
	print(number)
	print("Number Guessing Game ---------------- ")
	numOfTries=0
	guess,numOfTries = get_input(numOfTries, guessedList)
	is_guessed_correctly(guess,number,numOfTries,guessedList)

def main():
	start_guessing()

# Main program
main()
