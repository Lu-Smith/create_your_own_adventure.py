name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You wake up in the middle of nowhere. Which way would you like to go (Type: Left/Right)? ").lower()

if answer == "left":
    answer = input("You were walking for hours and you found a river, you can walk around it or swim across it (Type: Around/Across)? ").lower()

    if answer == "around":
        answer = input("You walk for hours, you are are hungry and thirsty. You see the boat. You can take the boat to cross the river (maybe to catch the fish), or you can set up a camping and rest (Type: Cross/Camp)? ").lower()

        if answer == "cross":
            answer = input("You decided to cross the river by boat and catch a fish with a net. You got lucky, and got a fish. You can set up camping on the other side of the river or you can eat a raw fish (sushi style) and keep moving  (Type: Walk/Camp)? ").lower()
            if answer == "walk":
                print("The raw fish didn't agree with you, you got diarrhoea for hours and died")
            elif answer == "camp":
                answer = input("You decide to camp, cooked the fish, boiled some water, and camp for the night. In the morning you were well rested and you can decide to take the boat and go with the flow of the river or leave the boat behind and keep walking (Type: River/Walk)").lower()
                if answer == "river":
                    answer = input("The raw fish didn't agree with you, you got diarrhoea for hours and died").lower()
                elif answer == "walk":
                    answer = input("You walk for hours and came across a desert. You can go across it or go back (Type: Across/Back)").lower()
                    if answer == "across":
                        print("The desert was endless, you died from thirst within 12h.")
                    elif answer == "back":
                        print("On the way back to the river, the mama bear attacked you and ate you.")
                    else:
                        print("Not a valid option. You lost.")
                else:
                    print("Not a valid option. You lost.")
            else:
                print("Not a valid option. You lost.")
        elif answer =="camp":
            print("You set up camp, cooked some food, drank water, and rested. In the morning, you can take the boat to cross the river, or you can explore the area.")
            next_action = input("What would you like to do in the morning? (Type: Cross/Explore) ").lower()
    
            if next_action == "cross":
                print("You pack up your camp, prepare to cross the river, and embark on the journey.")
                decision = input("As you approach the river, you notice the water is flowing fast. Do you still want to cross it? (Type: Yes/No) ").lower()
                
                if decision == "yes":
                    print("You cautiously enter the water and start crossing. The current is strong, but you manage to reach the other side safely.")
                    decision = input("You were exhausted, You can walk along the river or head towards the mountains you can see at the horizon? (Type: River/Mountains) ").lower()
                    if decision == "river":
                        decision = input("You have been walking for hours, you can set up camp, try to catch some fish or keep walking? (Type: Camp/Walk) ").lower()
                        if decision == "camp":
                            decision = input("You just started the fire, when two big bears appeared acrossed the river? You can run away, or stay at the camp. (Type: Run/Stay) ").lower()
                            if decision == "run":
                                print("You started to run away from the river and bears. You didn't noticed that you are running towards a mamma bear. She had no choice but to protect her cub. You didn't have any chance. You died.) ").lower()
                            elif decision == "stay":
                                print("You decided to stay and watch what bear will do. They stared at you and charged across the river, you didn't have any chance. You died.")
                            else:
                                print("Not a valid option. You lost.")
                        elif decision == "walk":
                            print("You kept walking for days, you became weak and confused, you saw a wolf, you try to run, but you couldn't. Yoy felt into the river and drown.")
                        else:
                            print("Not a valid option. You lost.")
                    elif decision == "mountains":
                        print("You kept walking for days, but you never reached the mountains, you died from thirst.")
                    else:
                        print("Not a valid option. You lost.")
                elif decision == "no":
                    print("You decide it's too risky to cross the river at this point. You return to your camp to rest and reconsider your options.")
                    decision = input("You decided to walk along the river. You came across a stranger? You can talk to him. (Type: Yes/No) ").lower()
                    if decision == "yes":
                        print("The stranger was a bad man. He shot you and throw your body into the river, You died").lower()
                    elif decision == "no":
                        print("You were to afraid to ask about help and kept walking until you died from the exhaustion.")
                    else:
                        print("Not a valid option. You lost.")
                else:
                    print("Not a valid option. You lost.")
            elif next_action == "explore":
                print("You decide to explore the area around your camp. You find some interesting landmarks and gather useful resources.")
                # Add more code here for the exploration scenario
            else:
                print("Not a valid option. You lost.")
        else:
            print("Not valid option. You lost")
    elif answer =="across":
        answer = input("After hours of walking you see a forest, you can walk around it or go through the forest (Type: Around/Forest)? ").lower()
    else:
        print("Not valid option. You lost")
elif answer =="right":
    answer = input("After hours of walking you see a forest, you can walk around it or go through the forest (Type: Around/Forest)? ").lower()
    
    if answer == "around":
        answer = input("Is getting dark. Tou are tired, thirsty and hungry. You can set up the camp or continue walking (Type: Camp/Walk)").lower()
        if answer == "camp":
            answer = input("You set up a camp and you fell asleep. In the morning you wake up to a playful bird song. You can try to catch the bird ans eat it or enter the forest (Type: Bird/Forest)")
            if answer == "bird":
                answer = input("You cought the bird, eat your breakfast and continue walking. There is a storm coming. You can enter the forest for safety, you can try to collect the water? (Type: Forest/Water) ")
                if answer == "forest":
                    print("You walk into the forest. As you delve deeper, you start to feel overwhelmed by the strange sounds of the trees swaying in the strong wind. The atmosphere becomes eerie, and soon, a thick mist envelops the entire forest, obscuring your vision.")
                    print("Surprisingly, the mist carries a familiar smell of coffee and toast, which comforts you amidst the uncertainty of your surroundings.")
                    print("Suddenly, as if in a blink of an eye, you find yourself at home, sitting at your dining table, enjoying a hearty breakfast. The events in the forest feel like a distant memory, leaving you wondering if it was all just a surreal dream.")
                elif answer == "water":
                    print("You decided to collect and drink some water. At first, it was a great relief from thirst. But suddenly, the calm atmosphere shifts, and dark clouds gather overhead. The gentle breeze turns into a fierce wind, and before you know it, the storm intensifies into a tornado.")
                    print("You try to find shelter, but the tornado sucks you in with its powerful force. The world spins around you, and you lose consciousness.")
                    print("When you wake up, you find yourself lying in your bed, safe and sound. It seems like it was all just a vivid dream.")
                else:
                    print("Not a valid option. You lost.")
            elif answer == "forest":
                answer = input("You enter the dense forest and you cam across berries. You can eat them or continue looke for another food (Type: Berries/Walk)").lower()
                if answer == "berries":
                    print("You ate poison berries, you felt aslep and never wake up")
                elif answer == "walk":
                    answer = input("You walk few miles and came across a big moose. You can try to avoid it, you can try to make it your pet (Type: Avoid/Pet)").lower()
                    if answer == "avoid":
                        answer = input("You went around the mighty beast and came across the spring. You can drink the water or you can keep walking (Type: Drink/Walk)").lower()
                        if answer == "drink":
                            answer = input("The water was delicious and refreshing. You decide to stay and camp. You can set up a campfire, you can just fall asleep without the fire (Type: Fire/No Fire)").lower()
                            if answer == "fire":
                                answer = input("You set up the campfire. The night was very cold, but the fire kept you alive. In the morning you decide to stay, or to keep moving (Type: Stay/Walk)").lower()
                                if answer == "stay":
                                    print("You were not able to find enough food, the days become colder and you died starvation and hypotermia.")
                                elif answer == "move":
                                    answer = input("You kept walking, the forest beacame more clear and you found a tiny house. You can try to check it out, you keep walking (Type: Check/Walk)").lower()
                                    if answer == "check":
                                        answer = input("You knock, and an old witch welcome you and invited you in. You can go in or politely say no (Type: Yes/No)").lower()
                                        if answer == "yes":
                                            print("You accepted the invitation, you started to help the old witch with home repairs and as a reward she help you to go back home.")
                                        elif answer == "no":
                                            print("You ofenden the witch and she punished you by turnig you into a crow.")
                                        else:
                                            print("Not a valid option. You lost.")
                                    elif answer == "walk":
                                        print("You kept walking in the circle and died from thirst.")
                                    else:
                                        print("Not a valid option. You lost.")
                                else:
                                    print("Not a valid option. You lost.")
                            elif answer == "no fire":
                                print("You frozed to death and died.")
                            else:
                                print("Not a valid option. You lost.")
                        elif answer == "walk":
                            print("You kept walking for another 9h and died from thirst.")
                        else:
                            print("Not a valid option. You lost.")
                    elif answer == "pet":
                        print("You mad the mighty moose angry, he charged at you and kill you.")
                    else:
                        print("Not a valid option. You lost.")
                else:
                    print("Not a valid option. You lost.")
            else:
                print("Not a valid option. You lost.")
        elif answer == "walk":
            answer = input("You decide it's too risky to cross the river at this point. You return to your camp to rest and reconsider your options.")
            # Add more code here for what happens if the player decides not to cross the river
        else:
            print("Not a valid option. You lost.")
    elif answer == "Forest":
        answer = input("You decide it's too risky to cross the river at this point. You return to your camp to rest and reconsider your options.")
        # Add more code here for what happens if the player decides not to cross the river
    else:
        print("Not a valid option. You lost.")
else:
    print("Not valid option. You lost")

print("Thank you for playing", name,"Have a wonderful day")