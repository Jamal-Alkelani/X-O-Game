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

if __name__ == "__main__":
    startGame()