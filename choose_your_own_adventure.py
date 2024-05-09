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
                print("The raw fish didn't agree with you, you got diarrhea for hours and died.")
            elif answer == "camp":
                answer = input("You decided to camp, cooked the fish, boiled some water, and camp for the night. In the morning you were well rested and you can decide to take the boat and go with the flow of the river or leave the boat behind and keep walking (Type: River/Walk)").lower()
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
                    print("You decided it's too risky to cross the river at this point. You return to your camp to rest and reconsider your options.")
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
                print("You decide to explore the area around your camp. You find some interesting landmarks and gather useful resources as wood for campfire and mushrooms.")
                answer = input("You are really hungry and you decided to cook dinner. You can make a mushrooms soup or try to hunt (Type: Soup/Hunt)? ").lower()
                if answer == "hunt":
                    print("You didn't catch anything. Exhausted from your efforts, you find a comfortable spot to rest and soon drift off to sleep.")
                    print("You awaken to the sensation of raindrops falling gently against your cheeks. Opening your eyes, you find yourself back in your own bed.")
                    print("As you slowly come to your senses, you realize that your faithful dog, Max, is licking your face with enthusiasm, welcoming you back from your adventure.")
                elif answer == "soup":
                    print("The soup was filled with magic mushrooms. As you take a sip, a wave of warmth and euphoria washes over you, and your senses become heightened.")
                    print("In a flash, your mind is flooded with incredible visions, revealing insights on how to improve the world and find your way home.")
                    print("The mushrooms seem to unlock hidden wisdom within you, guiding you towards newfound clarity and purpose.")
                else:
                    print("Not a valid option. You lost.")
            else:
                print("Not a valid option. You lost.")
        else:
            print("Not valid option. You lost")
    elif answer =="across":
        answer = input("After hours of walking you see a forest, you can walk around it or go through the forest (Type: Around/Forest)? ").lower()
        if answer == "around":
            answer = input("Is getting dark. You are tired, thirsty and hungry. You came across a wolf. You can run into a forest or stay (Type: Forest/Stay)").lower()
            if answer == "stay":
                print("The wolf was not alone, you got surrounded and became a dinner")
            elif answer == "forest":
                print("You walk into the forest. As you venture deeper, the forest seems to come alive with strange sounds, and you start to feel a sense of enchantment surrounding you.")
                print("After a while, the sky above you begins to dance with vibrant colors, casting an ethereal glow over the trees. The northern lights shimmer and swirl in mesmerizing patterns, creating a spectacle unlike anything you've ever seen.")
                print("Suddenly, a figure emerges from the shadows, moving with grace and confidence. As he steps into the light, you catch a glimpse of a handsome goblin, his emerald eyes gleaming with mischief.")
                print("He beckons you to follow him deeper into the forest, his charming smile inviting you on an adventure.")
                print("As you walk together, the air is filled with laughter and the promise of discovery.")
                print("Before you know it, you find yourself back at home, sitting by the fireplace with a cup of tea in hand. The memory of your encounter with the handsome goblin fills you with a sense of wonder and excitement, leaving you eager for more adventures in the enchanted forest.")
            else:
                print("Not a valid option. You lost.")
        elif answer == "forest":
            print("You walk into the forest. As you venture deeper, the forest seems to come alive with strange sounds, and you start to feel a sense of enchantment surrounding you.")
            print("After a while, a gentle mist begins to form, swirling around you in delicate wisps. Suddenly, a soft glow emerges from within the mist, and you catch a glimpse of a figure flitting gracefully between the trees.")
            print("Before you can fully comprehend what's happening, the figure reveals itself to be a forest fairy, with shimmering wings and a mischievous twinkle in her eyes.")
            print("She beckons you to follow her deeper into the forest, and as you do, you feel a sense of warmth and wonder washing over you.")
            print("After what feels like both moments and an eternity, you find yourself back at home, sitting by the fireplace with a cup of tea in hand. The memory of your encounter with the forest fairy lingers in your mind, filling you with a sense of magic and possibility.")
        else:
            print("Not a valid option. You lost.")
    else:
        print("Not valid option. You lost")
elif answer =="right":
    answer = input("After hours of walking you see a forest, you can walk around it or go through the forest (Type: Around/Forest)? ").lower()
    
    if answer == "around":
        answer = input("Is getting dark. You are tired, thirsty and hungry. You can set up the camp or continue walking (Type: Camp/Walk)").lower()
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
                    print("You ate poison berries, you felt asleep and never woke up.")
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
                                print("You froze to death and died.")
                            else:
                                print("Not a valid option. You lost.")
                        elif answer == "walk":
                            print("You kept walking for another 9h and died from thirst.")
                        else:
                            print("Not a valid option. You lost.")
                    elif answer == "pet":
                        print("You made the mighty moose angry, he charged at you and killed you.")
                    else:
                        print("Not a valid option. You lost.")
                else:
                    print("Not a valid option. You lost.")
            else:
                print("Not a valid option. You lost.")
        elif answer == "walk":
            print("You walk for days and died from exhaustion.")
        else:
            print("Not a valid option. You lost.")
    elif answer == "Forest":
        print("You walk into the forest. As you delve deeper, you start to feel overwhelmed by the strange sounds of the trees swaying in the strong wind. The atmosphere becomes eerie, and soon, a thick mist envelops the entire forest, obscuring your vision.")
        print("Surprisingly, the mist carries a familiar smell of coffee and toast, which comforts you amidst the uncertainty of your surroundings.")
        print("Suddenly, as if in a blink of an eye, you find yourself at home, sitting at your dining table, enjoying a hearty breakfast. The events in the forest feel like a distant memory, leaving you wondering if it was all just a surreal dream.")
    else:
        print("Not a valid option. You lost.")
else:
    print("Not valid option. You lost")

print("Thank you for playing", name,"Have a wonderful day")