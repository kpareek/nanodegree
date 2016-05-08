

#--------
#name = raw_input("Enter a file name: ")
#if fname[0:2] == "~/": #Check to see if it starts with a ~ and a slash
##If it doesn't start with the ~/, then
##the user could be referring to a valid file
##like "~.py" (I checked: it is possible.)
##notice below replace is valid on Mac OSX only (and not a good approach overall, cause not porta fname = fname.replace(#'~',"/Users/"+raw_input("Enter your short user name: "),1)
#workingfname = fname.replace("\\",'') #This for proper escaping of a valid folder named '~' as '\~', you #go back to normal program now
#handle = open(workingfname,'r') # . . .
#for line in handle:
#print line
#print "\n"+("That was "+fname+".").center(40)
#--------------

def userInput(input):
    prompt = """Choose what type of question you want to answer:
                easy normal hard"""
    check1 = ["easy", "normal", "hard"]         
    input = raw_input(prompt,":")
    if input not in check1:
        return "Invalid choice try again:"
    return input

print userInput("jump")
print userInput("normal")

