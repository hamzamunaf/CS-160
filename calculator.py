mode = 'i'
while mode != 'q' :
	mode=str(input("Choose Programmer (p) or scientifc (s) mode or quit the program(q): "))
	if mode == 'p':
		decimal=(input("what is the number in decimal?"))
		number1=int(decimal)
		x = ""
		while number1 > 0:
			x=str(number1 % 2) + x
			number1=number1 //2
			print("The binary number is : ", x)
		print("")
	elif mode== 's': 
		calmode = str(input("Please choose one of the following operators : +,-,*,/ or **: "))
		number1 =float(input("Please enter your first number"))
		number2 =float(input("please enter your Second number"))
		if (calmode == '/') and (number2 == 0 ):
			print("Error: Can not be divided by zero")
		elif calmode== '+' :
			print(number1+number2)
		elif calmode== '-' :
			print(number1-number2)
		elif calmode== '*':	
			print(number1*number2)
		elif calmode== '/' :
			#if num2 == '0'	:
			#	print("Error cannot be divided by zero")	
			print(number1/number2)
		elif calmode== '**':
			print(number1**number2)
		else:
			print("Please choose a valid calmode")
	else:
		print("Please choose a valid Calculator mode")
	proc=str(input("Do you like to perform another calculator? (yes or no?): "))
	if proc == 'yes' :
		mode = 'i' 
	else:
		mode  = 'q'
