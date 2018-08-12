import gameOver
import utils
 
array = [['X',' ',' '],[' ','X',' '],[' ',' ','X']]
def startGame():
	utils.print_game(array)
	print (gameOver.gameOver(array,'X'))




def handle_user_input(position):
	x=(position - 1) / 3
	y=(position - 1) % 3
	return x,y


if __name__ == "__main__":
    startGame()