import gameOver
import utils
 
array = [['X',' ',' '],[' ','X',' '],[' ',' ','X']]
player = 'X'
def startGame():
	utils.print_game(array)
	while True:
		if gameOver.gameOver(array,player):
			win()
			break

def read_input():
	a = raw_input("input here: ")
	return a
def win(player):
	print()




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