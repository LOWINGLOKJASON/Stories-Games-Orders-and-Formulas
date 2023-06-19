#****************************************************************
#Name: Wing Lok LO
#Link: https://replit.com/join/bramcqhmky-lowinglokjason
#****************************************************************

# import time, random and statistics packages
import time
import random as random
import statistics

# ---Import the time package and put a 2 second pause in-between each answer below ---

#############
#Question #1
#############

# Store a list of nouns, verbs and adverbs
nouns = ["owls", "cats", "cars", "fishes", "humans"]
verbs = ["flew", "jumped", "ran", "swam", "walked"]
adverbs = ["quietly", "scarly", "loudly", "quickly", "happily"]

# When the program is run it should tell the user a unique story.
while True:
  print("Hi user! I am going to tell you an unique story.")

  # ask the user to add elements to the list  
  user_nouns = input("Please add a noun: ")
  user_verbs = input("Please add a verb: ")
  user_adverbs = input("Please add an adverb: ")

  # add the user's input to the lists  
  nouns.append(user_nouns)
  verbs.append(user_verbs)
  adverbs.append(user_adverbs)

  # randonly choose the elements from the lists
  ran_nouns = random.choice(nouns)
  ran_verbs = random.choice(verbs)
  ran_adverbs = random.choice(adverbs)

  # build the story
  story = f"Today, the {ran_nouns} {ran_verbs} to my room while I'm doing assignments, I {ran_adverbs} {ran_verbs} out of the room. I stopped on the front door as I saw there are more {ran_nouns} {ran_verbs} to my house {ran_adverbs}. When they were surrounding me, I woke from my dream. I found it was a dream...is it a dream? Why the {ran_nouns} were in my room..."

  # print the story
  print(story)

  # ask the user if they would like another unique story and then repeat printing the story
  
  again = input("Would you like to hear another unique story? Press any keys to continue or type 'q' if you want to quit.")

  # quit the story if 'q' is entered
  if again == 'q':
    break
  
print("Thank you, see you soon!")

# Sleep 2 seconds
time.sleep(2)

#############
#Question #2
#############

# Create two lists with playing cards from 2-10, Ace, King, Queen, and Jack, one for the player and one for the computer
player = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
computer = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Shuffle the cards
random.shuffle(player)
random.shuffle(computer)

# Set point counters
score_player = 0
score_computer = 0

# Play the game until one of the decks is empty
while True:
    
    # Draw a card from each deck
    card_player = player.pop(0)
    card_computer = computer.pop(0)
    print(f"Player: {card_player}   Computer: {card_computer}")
    
    # if player's card and computer's card are the same
    if card_player == card_computer:
      print("War!")
      
      if len(player) >= 4 and len(computer) >= 4:
        war_player = [player.pop(0) for i in range(3)]
        war_computer = [computer.pop(0) for i in range(3)]
        card_player = player.pop(0)
        card_computer = computer.pop(0)
        if card_player > card_computer:
          score_player += 1
        elif card_computer > card_player:
          score_computer += 1
      else:
        print("Not enough cards for war")
        break
    
    # if player's card is larger than computer's card
    if card_player > card_computer:
      score_player += 1
      print(f"Player wins with {card_player} vs {card_computer}")
    
    # if computer's card is larger than player's card
    elif card_computer > card_player:
      score_computer += 1
      print(f"Player wins with {card_computer} vs {card_player}")
  
    # Check if player's or computer's is empty
    if len(player) == 0:
      print("Player is out of cards")
      break
    if len(computer) == 0:
      print("Computer is out of cards")
      break

# Display final score
print(f"Final score: \nPlayer: {score_player}, Computer: {score_computer}")

# Sleep 2 seconds using time.sleep(2)
time.sleep(2)

#############
#Question #3
#############

# Pizzas prices:
small = 6.99
medium = 8.99 
large = 10.99

# Get the info(name, pizza's size and amount) from the customers
name = input("What is your name? ")
size = input("What sizes of pizzas would you like to have(small, medium, large)?  ")
amount = input("How many pizzas would you like to have? ")

# Calculate the price before tax
if size == "small":
  price = small * int(amount)
elif size == "medium":
  price = medium * int(amount)
else:
  price = large * int(amount)

# Calculate the tax and price after tax
tax = price * 0.13
total = price + tax

# Create an order
order = f"ORDER \nName: {name} \nPizza Size: {size} x {amount} \nTax: ${tax} \nTotal: ${total}"
print(order)

# Sleep 2 seconds
time.sleep(2)

#############
#Question #4
#############

# Create number of diners and total cost
num_diners = 0
total_cost = 0

# Add a while loop for asking the age of diners
while True:
  age = input("Please type your age here or type 'exit' to exit. ")
  if age == "exit":
    break
  
  age = int(age)
  # If the person is under 5, dinner is free
  if age < 5:
    price = 0
  # If the person is under 10, dinner is $5
  elif age < 10:
    price = 5
  # If the person is under 18, dinner is $10
  elif age < 18:
    price = 10
  # If the person is over 65, the dinner is $12  
  elif age > 65:
    price = 12
  # All other diners pay $15
  else:
    price = 15

  # Add it to the number of diners and print the cost for each diner
  num_diners += 1
  total_cost += price
  print(f"Total cost for each diner: ${price}")

# Average cost before tax
avg_cost = total_cost/num_diners
# Tax value
tax = total_cost * 0.08
# Total cost after tax
total_after_tax = total_cost + tax
# Average cost after tax
avg_cost_after_tax = total_after_tax/num_diners

print(f"Cumulative total cost for all diners before tax: ${total_cost}")
print(f"Average cost per diner before tax: ${avg_cost}")
print(f"Total tax for all diners: ${tax}")
print(f"Total number of diners: {num_diners}")
print(f"Cumulative total cost for all diners after tax: ${total_after_tax}")
print(f"Average cost per diner after tax: ${avg_cost_after_tax}")

# Sleep 2 seconds
time.sleep(2)

##############################
#Question #BOUNOS QUESTUIONS 1
##############################

# Create lists for player choice and computer selection
player = []
computer = []

active = True
while active:
  number = input("Please choose a number between 1 and 37 (or enter 'quit' to end the game): ")
  
  # The program should end when quit has been entered
  if number == "quit":
    print("The game is ended!")
    break

  # Remind player type the numbers within the range
  number = int(number)
  if number < 1 or number > 37:
    print("Invalid input. Please enter a number between 1 and 37: ")
    continue

  # Keep track of numbers from user responses in a list 
  player.append(number)
  # Have the computer pick a number between 1-37
  computer_choice = random.randint(1, 37)
  # Keep track of the numbers that the computer picked 
  computer.append(computer_choice)

  # 37 for both the computer and player should be displayed as printing the player picked 0 or the computer picked 0. 
  print("The computer picked:", computer_choice if computer_choice != 37 else 0)
  
  # Let the player know if they won or lost
  if number == computer_choice:
        print("Player won!")
  else:
        print("Player lost!")
    
  # Let the player know if their number matched low (1-18) or high (19-36)
  if 1 <= number <= 18:
    print("Player's number is low.")
  elif 19 <= number <= 36:
    print("Player's number is high.")
  else:
    print("Player's number is 0.")

  # After each result, display a summary of previous results (print the list)
  print("Player's picks:", player)
  print(f"The computer's picks: {computer}")
  # After each result, the program should also report the median number using the statistics.median() function
  print("Median of player's picks:", statistics.median(player))
  print(f"Median of computer's picks: {statistics.median(computer)}")

  # The program should end using an active variable after it runs ten times
  if len(player) >= 10:
    print("The game is ended!")
    active = False

  # Sleep for 2 seconds
  time.sleep(2)

##############################
#Question #BOUNOS QUESTUIONS 2
##############################

# four formulas with answers
print(10**2+3*60/8-3)

print(round((5**3*(6-2))/(61-3+4), 6))

print(int(2**(2+1)-4+64**(2**(2.25-1/4))))

print(round(((0.44*(1-0.44))/34)**(1/2), 8))
