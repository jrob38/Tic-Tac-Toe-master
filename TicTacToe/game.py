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
	
def new_board():
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board
	
def display_board(board):
	print('\n\t %s | %s | %s' % (board[0], board[1], board[2]))
	print('\t ---------')
	print('\n\t %s | %s | %s' % (board[3], board[4], board[5]))
	print('\t ---------')
	print('\n\t %s | %s | %s \n' % (board[6], board[7], board[8]))
	
def legal_moves(board):
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
		return moves
		
def winner(board):
	WAYS_TO_WIN = ((0,1,2),
				   (3,4,5),
				   (6,7,8),
				   (0,3,6),
				   (1,4,7),
				   (2,5,8),
				   (0,4,8),
				   (2,4,6))
				   
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
			
		if EMPTY not in board:
			return TIE
		return None

def main():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	input('Press any key to continue.')
	
main()

			