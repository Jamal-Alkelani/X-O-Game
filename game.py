import gameOver
import utils
 
array = [['X',' ',' '],[' ','X',' '],[' ',' ','X']]
def startGame():
	utils.print_game(array)
	print (gameOver.gameOver(array,'X'))

if __name__ == "__main__":
    startGame()