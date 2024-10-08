#Vacuum Cleaner: Dinesh kumar G - 1BM22CS091

def vacuum_world():
    # Initializing goal_state
    goal_state = {'A': '0', 'B': '0'}  # 0 = Clean, 1 = Dirty
    cost = 0
    
    # Get user input
    location_input = input("Enter Location of Vacuum (A or B): ").upper()
    status_input = input("Enter status of Room " + location_input + " (0 for Clean, 1 for Dirty): ")
    status_input_complement = input("Enter status of the other room (0 for Clean, 1 for Dirty): ")
    
    print("\nInitial Room Condition: " + str(goal_state))
    
    # Vacuum in location A
    if location_input == 'A':
        print("Vacuum is placed in Location A.")
        
        # If A is dirty, clean it
        if status_input == '1':
            print("Location A is Dirty. Cleaning A...")
            goal_state['A'] = '0'
            cost += 1
            print("Cost for cleaning A: " + str(cost))
        
        else:
            print("Location A is already clean.")
        
        # Check room B
        if status_input_complement == '1':
            print("Location B is Dirty. Moving to B...")
            cost += 1  # cost for moving to B
            print("Cost for moving to B: " + str(cost))
            
            print("Cleaning B...")
            goal_state['B'] = '0'
            cost += 1
            print("Cost for cleaning B: " + str(cost))
        else:
            print("Location B is already clean.")
    
    # Vacuum in location B
    elif location_input == 'B':
        print("Vacuum is placed in Location B.")
        
        # If B is dirty, clean it
        if status_input == '1':
            print("Location B is Dirty. Cleaning B...")
            goal_state['B'] = '0'
            cost += 1
            print("Cost for cleaning B: " + str(cost))
        
        else:
            print("Location B is already clean.")
        
        # Check room A
        if status_input_complement == '1':
            print("Location A is Dirty. Moving to A...")
            cost += 1  # cost for moving to A
            print("Cost for moving to A: " + str(cost))
            
            print("Cleaning A...")
            goal_state['A'] = '0'
            cost += 1
            print("Cost for cleaning A: " + str(cost))
        else:
            print("Location A is already clean.")
    
    # Output goal state and performance
    print("\nFinal Room Condition: " + str(goal_state))
    print("Performance Measurement (Total Cost): " + str(cost))

# Run the vacuum world problem
vacuum_world()
