import sys
import getpass
def hangman():
	print("Get ready to play Hangman!")
	word=getpass.getpass("Player 1, Please enter your word and click enter: ").lower()
#turns the user inputted word into a lower case in one line
	print('\n'*20)
#Spaces out the inputted word
	start_game(word)
#calls back the function start_game
def start_game(word):
	player_lives = 6
	used_letters =[]
	number_dashes=["_" for i in range(len(word))]
#Using list compression, set number_dashes to - - -....
	print(visuals(player_lives))
	print("")
	print("")
	print(" ".join(number_dashes))
#using join function, turns '-','-' to  - -
	while player_lives == player_lives:
#loops forever
		input_letter =input("Player 2, input your letter guess: ")
		print('\n'*20)
		if len(input_letter) > 1:
#checks if the letter in imutted is more than 2 letters
			player_lives-= 1
			print(visuals(player_lives))
			print(input_letter,"is not \'a letter\'!")
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
#takes away a life and prints visuals, progress, and used letters
		elif input_letter  not in used_letters and input_letter in word:
#Checks if the letter is in the word, and not used already
			print(visuals(player_lives))
			print("Correct,",input_letter,"is in the word!")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
# prints new visuals, progress, and used letters
		elif input_letter not in word :
#Checks if the letter guessed is not in the word
			player_lives-=1
			print(visuals(player_lives))
			print("Incorrect,",input_letter,"is not in the word")
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
#takes away a life and prints new visuals, progress, and used letters
		elif input_letter in used_letters:
#Finally checks if the letter is already used
			player_lives-=1
			print(visuals(player_lives))
			print("You already guessed",input_letter)
			if input_letter not in used_letters:
				used_letters.append(str(input_letter))
			else:
				pass
			print("Used letters:"," ".join(used_letters))
			print((updated_dashes(word,input_letter,number_dashes,)),'')
# takes away a life and prints new visuals, progress, and used letters
		if player_lives == 0:
			you_lose(player_lives,word)
#Checks if the player loses, then calls back function: you_lose
		elif word == "".join(number_dashes):
			you_win(player_lives,word)
#Checks if the player wins, then calls back function: you_win
def updated_dashes(word,input_letter,number_dashes):
#everytime the player guesses a letter, it calls back thi function
	for i in range(len(word)):
#loops based on length of word
		if input_letter == word[i]:
#checks if the letter is equal to each letter individualy
			number_dashes[i] = input_letter
#if so, sets the position in "- - -" to the inputted leter
	return (" ".join(number_dashes))
#returns the updated progress "- - a" for example
def you_lose(player_lives,word):
#function is called back when player loses
	print("The guesser loses!","The word was",word)
	sys.exit()
#prints what the word was then exits the program
def you_win(player_lives,word):
#function is called back when player wins
	print("**************** Congratulations !***********")
	print("You win !","The word was: ",word)
	print("*********************************************")
	sys.exit()
#prints what the word was then exits the program
def visuals(player_lives):
#This function is used to print the progress through visuals
	if player_lives == 6:
		return"""
		_______
		|     |
		|     
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 5:
		return"""
		_______
		|     |
		|     O
		|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 4:
		return"""
		_______
		|     |
		|     O
		|   --|
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 3:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|
		|
		|
		|________
		|        |
		"""
	elif player_lives == 2:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    |
		|
		|________
		|        |
		"""
	elif player_lives == 1:
		return"""
		_______
		|     |
		|     O
		|   --|--
		|     |
		|    | |
		|
		|________
		|        |
		"""
	elif player_lives == 0:
		return"""
		_______
		|     |
		|     l0
		|    |||
		|     |
		|    | |
		|
		|________
		| D E A D|
		"""	
hangman()
#start of the code
