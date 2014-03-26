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
	WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
				   
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
			
	if EMPTY not in board:
		return TIE
		
	return None

def ask_number(question, low, high):
	response = None
	while response not in range(low, high):
		response = int(input(question))
	return response
	
def human_move(board, human):
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = ask_number('Where would you like to move? (0 - 8): ', 0, NUM_SQUARES)
		if move not in legal:
			print('\nThat square is occupied.  Choose another.\n')
	return move
	
def computer_move(board, computer, human):
	#board = board[:]
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
	print('I will now make my move.')
	legal = legal_moves(board)
	
	#if computer can when, make the winning move
	for move in legal:
		board[move] = computer
		if winner(board) == computer:
			print('Choosing %s' % move)
			return move
		board[move] = EMPTY
	
	#if human can when, block that move
	for move in legal:
		board[move] = human
		if winner(board) == human:
			print('Choosing %s' % move)
			return move
		board[move] = EMPTY
	
	#else take the next best move
	for move in BEST_MOVES:
		if move in legal:
			print('Choosing %s' % move)
			return move
		
def main():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		
	input('Press any key to continue.')
	
main()

			