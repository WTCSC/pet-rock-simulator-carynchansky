print("Welcome to Pet Rock Simulator")
happiness = 5
hunger = 5
thirst = 5
pet_name = input("Name your pet: ")
print(f"--- Your Pet Rock, {pet_name} ---")
print("( 0.0 )")
print(f"Happiness: {happiness}/10")
print(f"Hunger: {hunger}/10")
print(f"Thirst: {thirst}/10")
while True:
    print("\nWhat you want to do next?")
    print("1. Give food")
    print("2. Play")
    print("3. Do nothing")
    print("4. Bathe your pet")
    print("5. Give water")
    print("6. Exit game")
    input1 = input("What do you want (type a number): ")
    if input1 == '1': 
        if thirst == 0:
            print("Your pet died of thirst!")
            break
        if hunger == 10:
            print("I'm full. I can't eat anymore!!!")
            continue
        hunger = min(10, hunger + 2)
        thirst = max(0, thirst - 2)
        happiness = min(10, happiness + 1)
        print("Very delicious. Thank you!")
    elif input1 == '2':
        if thirst == 0 or hunger == 0:
            print("Your pet died from exhaustion!")
            break
        happiness = min(10, happiness + 2)
        hunger = max(0, hunger - 2)
        thirst = max(0, thirst - 2)
        print("That was fun!")
    elif input1 == '3': 
        if happiness == 0:
            print("Your pet is so sad. DO SOMETHING!!")
        else:
            happiness = max(0, happiness - 1)
            hunger = max(0, hunger - 1)
            thirst = max(0, thirst - 1)
            print("Your pet is just chilling...")
    elif input1 == '4': 
        if happiness < 10:
            happiness = min(10, happiness + 1)
            print("Splash splash! Your pet feels fresh.")
        else:
            print("Your pet is already super happy!")
    elif input1 == '5': 
        if thirst == 10:
            print("I can't drink anymore!")
        else:
            thirst = min(10, thirst + 3)
            happiness = min(10, happiness + 1)
            print("Ahhh, refreshing!")
    elif input1 == '6': 
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
print(f"\n--- Your Pet Rock, {pet_name} ---")
print("( 0.0 )")
print(f"Happiness: {happiness}/10")
print(f"Hunger: {hunger}/10")
print(f"Thirst: {thirst}/10")
	
