##check if a player wins
def gameOver(Mat,player):
    for i in range(3):
        if(Mat[i][0]==player and Mat[i][1]==player and Mat[i][2]==player ):
            print ("1")
            return True
        elif(Mat[0][i]==player and Mat[1][i]==player and Mat[2][i]==player ):
            print ("2")
            return True
    if(Mat[1][1]==player and Mat[2][2]==player and Mat[0][0]==player ):
        print ("3")
        return True
    if Mat[0][2]==player and Mat[1][1]==player and Mat[2][0]==player :
        return True
    return False
    
# ##check if the matrix is full with no vectory
# def gameOver(Mat):
#     for i in range(2):
#         for j in range(2):
#             if(Mat[i][j]==''):
#                 return False
    
#     return True
        




    