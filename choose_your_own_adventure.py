name = input("Type  your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are an a dirt road, it has come to the end. Which way would you like to go (Type: Left/Right)? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across (Type: Around/Across)? ").lower()

    if answer == "around":
        answer = input("You walk for hours, you are are hungry and thirsty. You see the boat. You can take the boat to cross the river (maybe to catch the fish), or you can set up a camping and rest (Type: Cross/Camp)? ")

        if answer == "cross":
            answer = input("You decided to cross the river by boat and catch a fish with a net. You got lucky, and got a fish. You can set up camping on the other side of the river or you can eat a raw fish (sushi style) and keep moving  (Type: Walk/Camp)? ")
        elif answer =="camp":
            print("You set up camp, cooked some food, drank water, and rested. In the morning, you can take the boat to cross the river, or you can explore the area.")
            next_action = input("What would you like to do in the morning? (Type: Cross/Explore) ").lower()
    
            if next_action == "cross":
                print("You pack up your camp, prepare to cross the river, and embark on the journey.")
                decision = input("As you approach the river, you notice the water is flowing fast. Do you still want to cross it? (Type: Yes/No) ").lower()
                
                if decision == "yes":
                    print("You cautiously enter the water and start crossing. The current is strong, but you manage to reach the other side safely.")
                    # Add more code here for what happens after crossing the river successfully
                elif decision == "no":
                    print("You decide it's too risky to cross the river at this point. You return to your camp to rest and reconsider your options.")
                    # Add more code here for what happens if the player decides not to cross the river
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
        answer = input("You come to a forest, you can walk around it or go through a path in the forest (Type: Walk around/Choose Path)? ")
    else:
        print("Not valid option. You lost")
elif answer =="right":
    answer = input("You come to a forest, you can walk around it or go through a path in the forest (Type: Walk around/Choose Path)? ")
else:
    print("Not valid option. You lost")
