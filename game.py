import gameOver
import utils
 
array = [['X',' ',' '],[' ','X',' '],[' ',' ','X']]
player = 'X'
def startGame():
	utils.print_game(array)
	while True:
		player_input = read_input(player)
		x,y = handle_user_input(player_input)
		update_array(x,y,player)
		if gameOver.gameOver(array,player):
			win()
			break


def read_input(player):
	a = raw_input("player " + player + ">> ")
	return a
def win(player):
	print("Player "+ player +" WON!!")




def handle_user_input(position):
	x=(position - 1) / 3
	y=(position - 1) % 3
	return x,y

def is_input_valid(input_data):
	if(input_data.isdigit()):
		if(input_data>='0' and input_data<='9'):
			return True
		else:
			return False
	else:
		return False



if __name__ == "__main__":
    startGame()