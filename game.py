import gameOver
import utils
 
array = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
player = 'X'
def startGame():
	while True:
		player_input = read_input(player)
		if not is_input_valid(player_input):
			print("Enter a valid position please!")
			continue
		x,y = handle_user_input(int(player_input))
		update_array(x,y,player)
		utils.print_game(array)
		if gameOver.gameOver(array,player):
			win(player)
			break
		if gameOver.isFull(array):
			failed()
			break

		swap_player()


def read_input(player):
	a = raw_input("player " + player + ">> ")
	return a
def win(player):
	print("Player "+ player +" WON!!")
def failed():
	print("NO ONE WON!!")

def handle_user_input(position):
	x=(position - 1) / 3
	y=(position - 1) % 3
	return x,y

def update_array(x,y,player):
	print x,y
	array[x][y]=player


def is_input_valid(input_data):
	if(input_data.isdigit()):
		if(input_data>='0' and input_data<='9'):
			return True
		else:
			return False
	else:
		return False

def swap_player():
	global player
	if player == 'X':
		player = 'O'
	else:
		player = 'X'


if __name__ == "__main__":
    startGame()