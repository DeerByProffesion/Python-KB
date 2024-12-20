# Treasure Island

# This project should consist below:

# 1. Print Welcome message with ASCII art
# 2. Create decisions for the user inputs
# 2.1 Decision one, go right or left, if right Game over
# 2.2 Decision swim or wait, if swim Game over
# 2.3 Decision Red, Blue or Yellow, If Red, Game Over, if Blue, Game Over, If yellow, Win, if enaything else, Game Over.

firstDecision = input('''
                                              :. ,..
                                            .' :~.':_.,
                                          .'   ::.::'.'
                                         :     ::'  .:
                                       `.:    .:  .:/
                                        `::--.:'.::'
                                          |. _:===-'
                                         / /
                        ,---.---.    __,','
                       (~`.  \   )   )','.,---..
                        `v`\ | ,' .-'.:,'_____   `.
                            )|/.-~.--~~--.   ~~~-. \\
                          _/-'_.-~        ""---.._`.|
                     _.-~~_.-~                    ""'
              _..--~~_.(~~
   __...---~~~_..--~~
,'___...---~~~\n
Welcome To treasure Island!
Start your joruney!
You land on the beach, you can choose to go left along the shore or left, what do you choose?\n''')

if firstDecision.lower() == "right":
    print("You fell into the moving sands! Death is coming! Game Over")
elif firstDecision.lower() == "left":
    secondDecision = input("You see that the shore is breaking and overflowing with water, there is still time to swim through it, or you can wait it off\nSo, wait or swim?\n")
    if secondDecision.lower() == "wait":
        print("Your lack of good decision making made cannibals find you, You have been eaten! Game over!")
    elif secondDecision.lower() == "swim":
        thirdDecision = input("During the swim something took you under the island and three fishes are in front of you.\nYou hear the voice 'Only one of us will save you, but we won't tell you which, choose carefully', Your death is nearing, The luck will estimate your survival chances! Choose fish color! Red, blue or yellow!\n")
        if thirdDecision.lower() == "red":
            print("'I will eat you whole, you choose your death!' The fish screams and changes into the huge shark, your days are done. Game Over!")
        if thirdDecision.lower() == "blue":
            print("'I will eat you whole, you choose your death!' The fish screams and changes into the huge shark, your days are done. Game Over!")
        if thirdDecision.lower() == "yellow":
            print("Magically after choosing yellow fish, you were teleported back to your bed, you woke up, it was just strange dream.\nWake up Samurai, We got a city to burn!")
        else:
            print("Your lack of good decision making made you realize that the oxygen is not forever, You have drowned! Game over!")
    else:
        print("Your lack of good decision making made cannibals find you, You have been eaten! Game over!")
else:
    print("Your lack of good decision making made cannibals find you, You have been eaten! Game over!")