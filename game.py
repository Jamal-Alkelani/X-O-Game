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


if __name__ == "__main__":
    startGame()