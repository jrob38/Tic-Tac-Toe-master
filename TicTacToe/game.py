X = 'X'
O = 'O'
EMPTY = ' '
TIE = 'TIE'
NUM_SQUARES = 9

def display_instruct():
	print(
		"""
		Moves will be made by entering a number, 0 - 8.  
		The number corresponds to the board position as 
		illustrated:
	
					0 | 1 | 2
					----------
					3 | 4 | 5
					----------
					6 | 7 | 8
						
		\n
		"""
		)
		
def ask_yes_no(question):
	response = None
	while response not in ('y', 'n'):
		response = input(question).lower()
		if response == 'yes':
			response = 'y'
		if response == 'no':
			response = 'n'
	return response

def pieces():
	go_first = ask_yes_no('Would you like to go first? (y/n): ')
	if go_first == 'y':
		print('\nYou have the first move.')
		human = X
		computer = O
	else:
		print('\nI will go first.')
		computer = X
		human = O
	return computer, human

def main():
	display_instruct()
	computer, human = pieces()
	input('Press any key to continue.')
	
main()

			