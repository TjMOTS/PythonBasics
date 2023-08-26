import math

_exit = False
invalid_trigger = False

def split_check(num_people, total):
  if num_people <= 1:
    raise ValueError("More than one person is required to split the check ")
  return math.ceil(total / num_people)

def Exit_Test():
      exit_inp = (input("Exit Y/N? "))
      if exit_inp == "Y":
          print("Goodbye!")
          return True
      elif exit_inp == "N":
          return False
      else:
          print("not recognized. Try again!")
          return exit_inp

while _exit != True:
    if _exit != False:
        _exit = Exit_Test()
    else:
        try:
          total_due = float(input("What is the total? "))
          total_people = int(input("How many people? "))
          amount_due = split_check(total_people, total_due)
        except ValueError as err:
          print("Oh no! That's not a valid value.")
          print("{}".format(err))
        else:
          print("Each person owes ${}".format(amount_due))
          _exit = Exit_Test()
      
