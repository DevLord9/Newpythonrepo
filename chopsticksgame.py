import random

print(
    "Welcome to Chopsticks! You will be against a computer. The rules will be in the code. Good Luck!!!!!"
)

list = ["l", "r"]
personhands = [1, 1]
#------------------#
computerhands = [1, 1]



print("Game is starting now!")
while True:

  print()

  if (personhands[0] == 0):
    userInput1 = "r"
  elif (personhands[1] == 0):
    userInput = "l"
  else: 
    userInput1 = input("Which hand would you like to use? ").lower()


  userInput2 = input("Which hand would you like to use on your opposites's hand? ").lower()

  if (userInput2 == "l" and computerhands[0] == 0):
    userInput2 = "r"
  elif (userInput2 == "r" and computerhands[1] == 0):
    userInput2 = "l"
  

  if userInput1 == "l" and userInput2 == "l":
    computerhands[0] += personhands[0]
  elif userInput1 == "l" and userInput2 == "r":
    computerhands[1] += personhands[0]
  elif userInput1 == "r" and userInput2 == "r":
    computerhands[1] += personhands[1]
  elif userInput1 == "r" and userInput2 == "l":
    computerhands[0] += personhands[1]

  comInput1 = list[random.randint(0, 1)]
  comInput2 = list[random.randint(0, 1)]

  if (personhands[0] + computerhands[0] == 5):
    comInput1 = "l"
    comInput2 = "l"
  if (personhands[1] + computerhands[0] == 5):
    comInput1 = "l"
    comInput2 = "r"
  if (personhands[0] + computerhands[1] == 5):
    comInput1 = "r"
    comInput2 = "l"
  if (personhands[1] + computerhands[1] == 5):
    comInput1 = "r"
    comInput2 = "r"

  if (comInput2 == "l" and personhands[0] == 0):
    comInput2 = "r"
  elif (comInput2 == "r" and personhands[1] == 0):
    comInput2 = "l"

  if comInput1 == "l" and comInput2 == "l":
    personhands[0] += computerhands[0]
    print("\nThe computer pick their left and your left\n")

  elif comInput1 == "l" and comInput2 == "r":
    personhands[1] += computerhands[0]
    print("\nThe computer pick their left and your right\n")
  elif comInput1 == "r" and comInput2 == "r":
    personhands[1] += computerhands[1]
    print("\nThe computer pick their right and your right\n")
  elif comInput1 == "r" and comInput2 == "l":
    personhands[0] += computerhands[1]
    print("\nThe computer pick their right and your left\n")

  if (personhands[0] >= 5):
    personhands[0] %= 5
  if (personhands[1] >= 5):
    personhands[1] %= 5
  if (computerhands[0] >= 5):
    computerhands[0] %= 5 
  if (computerhands[1] >= 5):
    computerhands[1] %= 5 

  print("You have (", personhands[0], ", ", personhands[1]," )")
  print("Computer has (", computerhands[0], ", ", computerhands[1]," )")

  if (personhands[0] == 0 and personhands[1] == 0):
    personhands[0] = 1
    personhands[1] = 1
    #------------------#
    computerhands[0] = 1
    computerhands[1] = 1    
    temp = input("You lost! Press enter to continue..")

  elif (computerhands[0] == 0 and computerhands[1] == 0):
    personhands[0] = 1
    personhands[1] = 1
    #------------------#
    computerhands[0] = 1
    computerhands[1] = 1    
    temp = input("Congratulations, you won! Press enter to continue..")
