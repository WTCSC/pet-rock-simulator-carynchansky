print("Welcome to Pet Rock Simulator")
happiness = 5
hunger = 5
thirst = 5
pet_name = input("Name your pet: ")
print(f"--- Your Pet Rock, {pet_name} ---")
print("( 0.0 )")    
print(f"Happines: {happiness}/10")
print(f"Hunger: {hunger}/10")
print(f"Thirst: {thirst}/10")
while True:
      print("What you what to do next?")
      print("1. Give a food")
      print("2. Play")
      print("3. Do nothing")
      print("4. Bathing a pet")
      print("5. Give a water")
      input1 = input("What do you want(type a number): ")
      if input1 == '1':
            if hunger == 9:
                  hunger += 1
            if thirst == 1:
                  thirst -= 1                        
            if thirst > 1:
                  thirst -= 2
            if hunger <= 8:
                  hunger += 2
            
            happines += 1
            print(f"--- Your Pet Rock, {pet_name} ---")
            print(f"Happines: {happiness}/10")
            print(f"Hunger: {hunger}/10")
            print(f"Thirst: {thirst}/10")
            if thirst == 0:
                  print("Your pet is dead")
                  break
            print("Very delicious. Thank you!")
            if hunger == 10:
                  print("I'm full. I can't eat anymore!!!")
      elif input1 == '2':
            if happiness == 9:
                  happines += 1
            if happiness <= 8:
                  happines += 2
            if hunger == 1:
                  hunger -= 1
            if hunger > 1:
                  hunger -= 2
            if thirst == 1:
                  thirst -= 1
            if thirst > 1:
                  thirst -= 2
            if thirst or hunger == 0:
                        
            
            
      elif input1 == '3':
      elif input1 == '4':
      elif input1 == '5':
      
      else:
            print("Invalid input. Please try again")        