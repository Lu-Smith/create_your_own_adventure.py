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
            answer = input("You set up the fire, boiled some water, try fishing ( but you didn't catch anything), and go to sleep. In the morning, you can take a boat to cross the river, or you can go fishing and back to your camp (Type: Cross/Fish)")
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
