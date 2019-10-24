DIM = 8
clicker = [[0 for x in range(DIM)] for y in range(DIM)]
check_list = list()
score1 = 0
score2 = 0

def create_board():
	clicker[3][3] = 1
	clicker[4][4] = 1
	clicker[3][4] = 2
	clicker[4][3] = 2
	
	
def print_board():
	global clicker
	l=0
	print("     0", "", "1", "", "2" , "" ,"3", "", "4", "", "5" , "", "6" ,"", "7")
	print("----------------------------------------------------------------")
	for i in range(DIM):
		print(l, "|", end='')
		for j in range(DIM):
			print (" ", clicker[i][j],  end='')
		l = l + 1
		print()	
	print("----------------------------------------------------------------")
	
def check_count_up(x,y,player):
	global check_list
	global clicker
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	if (y!=0):
		for j in range(y-1,0,-1):
			if (player != clicker[x][j] and clicker[x][j] != 0):
				temp_check_list.append([x , j])
			elif(clicker[x][j] != 0):
				if (temp_check_list != []):
					check_list.append(temp_check_list)
					break
			else:
				break
	
def check_count_down(x,y,player):
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	if (y!=DIM):
		for j in range(y+1,DIM):
			if (j > 7):
				break
			if (player != clicker[x][j] and clicker[x][j] != 0):
				temp_check_list.append([x , j])
			elif(clicker[x][j] != 0):
				if (temp_check_list != []):
					check_list.append(temp_check_list)
					break
			else:
				break
				
def check_count_left(x,y,player):
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	if (x!=0):
		for i in range(x-1,0,-1):
			if (player != clicker[i][y] and clicker[i][y] != 0):
				temp_check_list.append([i , y])
			elif(clicker[i][y] != 0):
				if (temp_check_list != []):
					check_list.append(temp_check_list)
					break
			else:
				break
				
def check_count_right(x,y,player):
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	if (x!=DIM):
		for i in range(x+1,DIM):
			if (i > 7):
				break
			if (player != clicker[i][y] and clicker[i][y] != 0):
				temp_check_list.append([i,y])
			elif(clicker[i][y] != 0):
				if (temp_check_list != []):
					check_list.append(temp_check_list)
					break
			else:
				break
				
def check_count_upleft(x,y,player):	
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	i = x
	if (y!=0):
		if (x!=0):
			for j in range(y-1,0,-1):
				i = i - 1
				if (player != clicker[i][j] and clicker[i][j] != 0):
					temp_check_list.append([i ,  j])
				elif(clicker[i][j] != 0):
					if (temp_check_list != []):
						check_list.append(temp_check_list)
						break
				else:
					break
					
def check_count_downleft(x,y,player):	
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	i = x
	if (y!=DIM):
		if (x!=0):
			for j in range(y+1,DIM):
				i = i - 1
				if (j > 7 or i > 7):
					break
				if (player != clicker[i][j] and clicker[i][j] != 0):
					temp_check_list.append([i , j])
				elif(clicker[i][j] != 0):
					if (temp_check_list != []):
						check_list.append(temp_check_list)
						break
				else:
					break	

def check_count_upright(x,y,player):
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	i = x
	if (y!=0):
		if (x!=DIM):
			for j in range(y-1,0,-1):
				i = i + 1
				if (j > 7 or i > 7):
					break
				if (player != clicker[i][j] and clicker[i][j] != 0):
					temp_check_list.append([i , j])
				elif(clicker[i][j] != 0):
					if (temp_check_list != []):
						check_list.append(temp_check_list)
						break
				else:
					break
					
def check_count_downright(x,y,player):
	global clicker
	global check_list
	temp_check_list = list()
	if (clicker[x][y] != 0): return
	i = x
	if (y!=DIM):
		if (x!=DIM):
			for j in range(y+1,DIM):
				i = i + 1
				if (j > 7 or i > 7):
					break
				if (player != clicker[i][j] and clicker[i][j] != 0):
					temp_check_list.append([i , j])
				elif(clicker[i][j] != 0):
					if (temp_check_list != []):
						check_list.append(temp_check_list)
						break
				else:
					break
					
def check_count(x,y,player):
	global check_list
	global clicker
	check_count_up(x,y,player)
	check_count_down(x,y,player)
	check_count_left(x,y,player)
	check_count_right(x,y,player)
	check_count_upright(x,y,player)
	check_count_upleft(x,y,player)
	check_count_downright(x,y,player)
	check_count_downleft(x,y,player)
	return len(check_list)
	
	
def Checker_counts(player):
	global check_list
	B = [[0 for x in range(DIM)] for y in range(DIM)]
	for i in range(DIM):
		for j in range(DIM):
			B[i][j] = check_count(i,j,player)	
			check_list = list()		
	return B
	
def add_checker(x,y,player):
	global clicker
	global check_list
	clicker[x][y] = player
	for element in check_list:
		if element != None:
			clicker[element[0][0]][element[0][1]] = player
	check_list = list()	
		
def human_play(player):
	global check_list
	B = Checker_counts(player)
	clickervailable_flag = False
	Choice_flag = False
	for i in range(DIM):
		for j in range(DIM):
			if (B[i][j] > 0):
				clickervailable_flag = True
	if (clickervailable_flag):
		while (True):
			print("There is at least one available move. Give the coordinates of your choice!")
			var1 = int(input("Please enter y: "))
			var2 = int(input("Please enter x: "))
			if (B[var1][var2] > 0):
				check_count(var1,var2,player)
				add_checker(var1,var2,player)
				Choice_flag = True
			if(Choice_flag):
				break
			print("Not a valid choice. Try again!")			
	return clickervailable_flag	
	
	
def print_score():
	global clicker
	global score1 
	global score2 
	score1 = 0
	score2 = 0
	for i in range(DIM):
		for j in range(DIM):
			if (clicker[i][j] == 1):
				score1 = score1 + 10
			if (clicker[i][j] == 2):
				score2 = score2 + 10
	print("Score for player1 is: ", score1,"Score for player2 is: ", score2)	

print("OTHELLO GclickerME...")

create_board()
print_board()

print("Welcome to the game ")
a = int(input("Press 1 to start the game First player(1) will place their token and then player(2) will place their token and then alternatively "))
if (a == 1):
	while(True):
		move = human_play(1)
		if (move == False):
			break
		print_board()	
		print_score()
		move = human_play(2)
		if (move == False):
			break
		print_board()	
		print_score()
