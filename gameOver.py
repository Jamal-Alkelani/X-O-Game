##check if a player wins
def gameOver(Mat,player):
    for i in range(2):
        if(Mat[i][0]==player and Mat[i][1]==player and Mat[i][2]==player ):
            return True
        elif(Mat[0][i]==player and Mat[1][i]==player and Mat[2][i]==player ):
            return True
        elif(Mat[i][i]==player and Mat[i][i]==player and Mat[i][i]==player ):
            return True
        elif((i+j)==2 and Mat[i][j]==player and Mat[i][j]==player and Mat[i][j]==player ):
            return True
    return False
    
##check if the matrix is full with no vectory
def gameOver(Mat):
    for i in range(2):
        for j in range(2):
            if(Mat[i][j]==''):
                return False
    
    return True
        




    