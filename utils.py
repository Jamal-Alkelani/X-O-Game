def print_game(game_array):
		for i in range(len(game_array[0])):
				print (str(game_array[i][0]) + " | " + str(game_array[i][1]) + " | " + str(game_array[i][2]))
				if i != len(game_array[0])-1:
					print ("----------")
