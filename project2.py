question ="""This is __1__ blank and this is __2__ blank. make sure this is __1__ blank"""
blanks = ["__1__","__2__","__4__"]
answers = ["first","second","three"]

def blankMap(input,word,output):
	'''this function looks for blanks and returns correct answers. If there is no match it will return None.
	example: 
	question = """This is __1__ blank and this is __2__ blank"""
	blanks = ["__1__","__2__"]
	answers = ["first","second"]
	print blankMap(blanks,"__2__",answers) 
	It will return second
	'''
	if word in input:
		return output[input.index(word)]
	return None

def playGame(quiz):
	replaced=[]
	for word in quiz.split():
		replacement = blankMap(blanks,word,answers)
		if replacement != None:
			word = replacement
			replaced.append(word)
		else:
			replaced.append(word)
	replaced = " ".join(replaced)
	return question ,replaced

def userInput(message,output):
""" This function will take the user input, check if the input is correct."""
	input = raw_input(message: )



#print blankMap(blanks,"__4__",answers)


print playGame(question)