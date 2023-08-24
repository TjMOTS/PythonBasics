#This line creates a variable called first_name and set's it equal to an input. Python is smart enough to ask the user for a prompt when the instruction "input" is called.
#It also gives the user some context of what to input with a string denoted by quotes. It's kind of like a print with an expected response that gets placed into the first_name variable.
#Note that the space after ? and before the " is intentional. If it's not there you'd end up with something like name?Frank unless the user adds their own space.
first_name = input("What is your first name? ")

#Prints your name! Or at least whatever you put in the input. The machine can't tell when you're lying so it doesn't "know" your name.
print("Hello,", first_name)

#So this line compares what you've enetered as the input and if it equals Frank exactly then it procedes tp the next line. "if/else" statements have to have ":" at the end of the line for some odd reason.
#Probably because, you know, computer reasons. Usually if/else statements also must have an "==" a simple "=" just won't do. Why? Computer reasons.
if first_name == "Frank":
  
  #So you if you passed the first gate by having the name Frank or have the input you typed in be Frank then this next line will be the first thing that executes. Notice how you can slap your variable
  #into a print statement along with the sting? It'll still work this way and is pretty neat. Note that you can have either the comma seperation or the plus sepration like the line after this one, both are
  #considered viable. However, be careful with "+" as something like print(2+2) will actually print 4 instead of 2+2.
  print(first_name, "is learning Python!")

  #If you're lucky enough to have the first name Frank congrats! You're the best. Sorry frank's you're not allowed though as the capital letter is important.
  print(first_name + " is the best!")

#If you don't happen to have the honor of being named Frank but do still happen to be named max then this next line applies to you. The instruction elif is the combination of else and if. 
elif first_name == "Max":
  
  #He sure is, probably. You go Max.
  print(first_name + " is learning Python with the community.")

#If you don't have the name Frank or Max then the last option here is what applies when it looks in the variable first_name
else:
  
  #This line asks you for your age, and places it in a new variable called "age". Notice the int(input( this is asking for an intiger input.
  age = int(input("How old are you? "))

  #OC,"just in case have a younger user who can't read." I'm 28 and I can't read! I can write though. This line compares the number in the age variable instead of a name.
  if age <= 6 :

    #Prints a sick burn to our younger coders. (That they probably can't read.)
    print("Maybe you should learn to read first!")

  #If your age is above 6 congrats you can move on to the else catagory.  
  else :

    #This was something I didn't know. Apparently, the .format() will place whatever is in the variable into the curly brackets in the string. I suppose this is maybe an easier
    #way of putting something in the string witout writing out "" + first_name. I'm not really sure what the value is in doing this as adding more than one {} to the statement causes
    #the program to fail. I was thinking you could maybe fill in multiple gaps at the same time without the need to write out first_name each time, but that doesn't seem to be the case.
    print("You should totally learn Python {}".format(first_name))

#No YOU have a great day!
print("Have a great day {}".format(first_name))