import random          #for randomize the numbers we get from dice
min=1
max=6
roll_again='yes'
while roll_again=='yes':
    print("Rolling the dice....")
    print("If you want to roll the dice again then type yes.")    
    print(random.randint(min,max))
    roll_again=input("Do you want to roll again? yes")
print("Thanks for play...")