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

def main():
	display_instruct()
	input('Press any key to continue.')
	
main()

			