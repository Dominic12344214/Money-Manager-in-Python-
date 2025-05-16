
import json
import os

DATA_FILE = "nest_data.json"

# Default values
data = {
    #defalt wallets
    "balance": 0.00,
    "spending_balance": 0.00,
    "goal_wallet": 0.00,

    #goal data
    "goal": "",
    "goal_price": 0.00,

    #wallet slots
    "wallet_slot_one": "empty slot one",
    "wallet_slot_two": "empty slot two",
    "wallet_slot_three": "empty slot three",

    #slot ballences
    "slot_one_balance": 0.00,
    "slot_two_balance": 0.00,
    "slot_three_balance": 0.00

}


# Load from JSON if exists
if os.path.exists(DATA_FILE):

    with open(DATA_FILE, "r") as file:
        data = json.load(file)

# Helper to save data to JSON
def save_data():

    with open(DATA_FILE, "w") as file:
        json.dump(data, file)

# Input validation functions
def get_valid_float(prompt):

    while True:

        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")

            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a number.")

def get_valid_selection(prompt, valid_options):

    while True:
        selection = input(prompt).strip()

        if selection in valid_options:
            return selection

        else:
            print("Invalid selection. Please try again.")




# Main Loop
while True:
    # start page
    print("\n==============================")
    print(f"Your savings balance is: ${data['balance']:.2f}")
    print(f"Your spending balance is: ${data['spending_balance']:.2f}")
    print(f"Your goal balance is: ${data['goal_wallet']:.2f}")

    if data["wallet_slot_one"] != "empty slot one":
        print("")
        print(data["wallet_slot_one"] + " balance $" + f"{data['slot_one_balance']:.2f}")

    if data["wallet_slot_two"] != "empty slot two":
        if data["wallet_slot_one"] == "empty slot one":
            print("")
        print(data["wallet_slot_two"] + " balance $" + f"{data['slot_two_balance']:.2f}")

    if data["wallet_slot_three"] != "empty slot three":
        if data["wallet_slot_one"] == "empty slot one" and data["wallet_slot_two"] == "empty slot two":
            print("")
        print(data["wallet_slot_three"] + " balance $" + f"{data['slot_three_balance']:.2f}")

    print("==============================\n")

    print("""SELECT FUNCTION
1. Add money
2. Remove money
3. transfer money
4. Create/Remove wallets
5. Goal
6. Exit
""")


    selection = get_valid_selection("Enter number corresponding with function: ", ["1", "2", "3", "4", "5", "6"])

    # Add money
    if selection == "1":
        print("""
1. Add to savings
2. Add to spending
3. Add to goals
4. Add to custom wallet
5. Split
""")

        selection_c = get_valid_selection("Choose an option: ", ["1", "2", "3", "4", "5"])
        #savings
        if selection_c == "1":
            amount = get_valid_float("Add money: $")
            data["balance"] += amount

            print(f"Your new balance is: ${data['balance']:.2f}")

        #spending
        elif selection_c == "2":
            amount = get_valid_float("Add money: $")
            data["spending_balance"] += amount

            print(f"Your new spending balance is: ${data['spending_balance']:.2f}")

        #goals
        elif selection_c == "3":
            amount = get_valid_float("Add money: $")
            data["goal_wallet"] += amount

            print(f"Your new goal balance is: ${data['goal_wallet']:.2f}")

        #custom wallet
        elif selection_c == "4":
            print("Choose a wallet")
            print("1. " + data["wallet_slot_one"])
            print("2. " + data["wallet_slot_two"])
            print("3. " + data["wallet_slot_three"])

            selection_l = get_valid_selection("choose an option:  ", ["1", "2", "3"])

            #slot one
            if selection_l == "1":
                if data["wallet_slot_one"] == "empty slot one":
                    print("slot not in use")

                    input("enter to continue")

                else:
                    to_slot_one = get_valid_float("How much: ")

                    data["slot_one_balance"] += to_slot_one

                    print(f"your new balance is: ${data["slot_one_balance"]:.2f}")

            #slot two
            elif selection_l == "2":
                if data["wallet_slot_two"] == "empty slot two":
                    print("slot not in use")

                    input("enter to continue")

                else:
                    to_slot_two = get_valid_float("how much: ")

                    data["slot_two_balance"] += to_slot_two

                    print(f"your new balance is: ${data["slot_two_balance"]:.2f}")

            #slot three
            else:
                if data["wallet_slot_three"] == "empty slot three":
                    print("slot not in use")

                    input("enter to continue")

                else:
                    to_slot_three = get_valid_float("how much: ")

                    data["slot_three_balance"] += to_slot_three

                    print(f"your new balance is: ${data["slot_three_balance"]:.2f}")

        #split
        elif selection_c == "5":
            print("\nThe following percentages must add up to 100.\n")

            try:
                saving_split = float(input("Percent to savings: "))
                junk_split = float(input("Percent to spending: "))
                goal_split = float(input("Percent to goals: "))

                total = saving_split + junk_split + goal_split

                if total != 100:
                    print("The percentages must add up to 100.")

                else:
                    amount = get_valid_float("Add money: $")

                    data["balance"] += amount * (saving_split / 100)
                    data["spending_balance"] += amount * (junk_split / 100)
                    data["goal_wallet"] += amount * (goal_split / 100)

                    print(f"Your new savings balance is: ${data['balance']:.2f}")
                    print(f"Your new spending balance is: ${data['spending_balance']:.2f}")
                    print(f"Your new goal balance is: ${data['goal_wallet']:.2f}")

            except ValueError:
                print("Invalid percentage input.")

        save_data()
        input("Press Enter to continue...")


    # Remove money
    #TODO: add custom wallets
    elif selection == "2":
        print("""
1. Remove from savings
2. Remove from goal wallet
3. Remove from spending
4. Custom wallet
""")

        selection_b = get_valid_selection("Choose an option: ", ["1", "2", "3", "4"])

        amount = get_valid_float("Remove money: $")

        if selection_b == "1":

            if amount > data["balance"]:
                print("Insufficient funds.")

            else:
                data["balance"] -= amount
                print(f"Your new savings balance is: ${data['balance']:.2f}")

        elif selection_b == "2":
            if amount > data["goal_wallet"]:
                print("Insufficient funds.")

            else:
                data["goal_wallet"] -= amount
                print(f"Your new goal balance is: ${data['goal_wallet']:.2f}")

        elif selection_b == "3":

            if amount > data["spending_balance"]:
                print("Insufficient funds.")

            else:
                data["spending_balance"] -= amount
                print(f"Your new spending balance is: ${data['spending_balance']:.2f}")

        else:
            print("Choose a wallet")
            print("1. " + data["wallet_slot_one"])
            print("2. " + data["wallet_slot_two"])
            print("3. " + data["wallet_slot_three"])

            selection_m = get_valid_selection("choose an option: ", ["1", "2", "3"])

            if selection_m == "1":
                if data["wallet_slot_one"] == "empty slot one":
                    print("slot not in use")

                    input("enter to continue")

                else:
                    if amount > data["slot_one_balance"]:
                        print("insufficient funds")

                    else:
                        data["slot_one_balance"] -= amount

                        print(f"your new balance is: {data["slot_one_balance"]:.2f}")

            elif selection_m == "2":
                if data["wallet_slot_two"] == "empty slot two":
                    print("slot is not in use")

                else:
                    if amount > data["slot_two_balance"]:
                        print("insufisint funds")

                    else:
                        data["slot_two_balance"] -= amount

                        print(f"your new balnce is: :{data["slot_two_balance"]:.2f}")

            else:
                if data["wallet_slot_three"] == "empty slot three":
                    print("slot not in use")

                else:
                    if amount > data["slot_three_balance"]:
                        data["slot_three_balance"] -= amount

                        print(f"your new balance is: ${data["slot_three_balance"]:.2f}")


        save_data()
        input("Press Enter to continue...")


    #transfer money
    elif selection == "3":
        print("""
        1. transfer from savings 
        2. transfer from spending 
        3. transfer from goal
        """)

        selection_e =  get_valid_selection("choose an option: ", ["1", "2", "3"])

        #from savings
        if selection_e == "1":
            print("""
            1. Transfer to spending 
            2. Transfer to goal
            """)
            
            selection_f = get_valid_selection("choose an option: ", ["1", "2"])

            #saving to spending
            if selection_f == "1":
                amount = get_valid_float("move from savings to spending: $")

                if amount > data["balance"]:
                    print("Insufficient funds.")

                else:
                    data["balance"] -= amount
                    data["spending_balance"] += amount

                    print(f"Your new balance is: ${data['balance']:.2f}")
                    print(f"Your new spending balance is: ${data['spending_balance']:.2f}")

                    save_data()
                    input("enter to continue")

            elif selection_f == "2":
                amount = get_valid_float("Move from saving to spending: $")

                if amount > data["balance"]:
                    print("Insufficient funds")

                else:
                    data["balance"] -= amount
                    data["goal_wallet"] += amount

                    print(f"your new balance is: ${data["balance"]:.2f}")
                    print (f"your new goal balance is: ${data["goal_wallet"]:.2f}")

                    save_data()
                    input("enter to continue")

        #from spending
        elif selection_e == "2":
            print("""
            1. Transfer to saving 
            2. Transfer to goal
            """)

            selection_g = get_valid_selection("choose an option", ["1", "2"])

            #spending to saving
            if selection_g == "1":
                amount = get_valid_float("move from spending to saving: $")

                if amount > data["spending_balance"]:
                    print("Insufficient funds")
                    
                else:
                    data["spending_balance"] -= amount
                    data["balance"] += amount
                    
                    print(f"your new spending balance is: ${data["spending_balance"]:.2f}")
                    print(f"your new saving balance is: ${data["balance"]:.2f}")

                    save_data()
                    input("enter to continue")
                    
            #spending to goals
            elif selection_g == "2":
                amount = get_valid_float("move from spending to goals: $")
                
                if amount > data["spending_balance"]:
                    print("Insufficient funds")
                
                else:
                    data["spending_balance"] -= amount
                    data["goal_wallet"] += amount
                    
                    print(f"your new spending balance is: ${data["spending_balance"]:.2f}")
                    print(f"your new goal balance is: ${data["goal_wallet"]:.2f}")

                    save_data()
                    input("enter to continue")
                
        #from goals
        elif selection_e == "3":
            print("""
            1. Transfer to saving
            2. Transfer to spending
            """)
            
            selection_h = get_valid_selection("choose an option",["1", "2"])
            
            #goal to savings
            if selection_h == "1":
                amount = get_valid_float("move from goals to savings")
                
                if amount > data["goal_wallet"]:
                    print("Insufficient funds")
                    
                else:
                    data["goal_wallet"] -= amount
                    data["balance"] += amount
                    
                    print(f"your new goal balance is: ${data["goal_wallet"]:.2f}")
                    print(f"your new savings balance is: ${data["balance"]:.2f}")

                    save_data()
                    input("enter to continue")
                    
            #goal to spending
            elif selection_h == "2":
                amount = get_valid_float("move from goals to spending: $")
                
                if amount > data["goal_wallet"]:
                    print("Insufficient funds")
                    
                else:
                    data["goal_wallet"] -= amount
                    data["spending_balance"] += amount
                    
                    print(f"your new goal balance is: ${data["goal_wallet"]:.f2}")
                    print(f"your new spending balance is: ${data["spending_balance"]:.f2}")

                    save_data()
                    input("enter to continue")


    #Wallet slots
    elif selection == "4":
        print("""
1. Create Wallet
2. Remove wallet
""")
        selection_i = get_valid_selection("choose an option: ", ["1", "2"])

        #create slot
        if selection_i == "1":
            print("")
            print("1. " + data["wallet_slot_one"])
            print("2. " + data["wallet_slot_two"])
            print("3. " + data["wallet_slot_three"]) 
            print("")

            selection_j = get_valid_selection("choose an option: ", ["1", "2", "3"])

            #slot one
            if selection_j == "1":
                data["wallet_slot_one"] = input("Name slot: ")
                
                print("new slot named " + data["wallet_slot_one"] + " has been created")

                save_data()

                #slot two
            elif selection_j == "2":
                data["wallet_slot_two"] = input("Name slot: ")

                print("new slot named " + data["wallet_slot_two"] + " has been created")

                save_data()

            #slot three
            else:
                data["wallet_slot_three"] = input("Name Slot: ")

                print("new slot named " + data["wallet_slot_three"] + " has been created")

                save_data()

        #remove slot
        else:
            print("")
            print("1. " + data["wallet_slot_one"])
            print("2. " + data["wallet_slot_two"])
            print("3. " + data["wallet_slot_three"])
            print("")

            selection_k = get_valid_selection("choose an option: ", ["1", "2", "3"])

            #slot one
            if selection_k == "1":
                if data["wallet_slot_one"] == "empty slot one":
                    print("slot is empty")

                else:
                    #comfermation
                    print("are you sure you want to delete " + data["wallet_slot_one"] + "?")
                    print("""
1. Yes
2. No
""")
                    confirm = get_valid_selection("confirmation: ", ["1", "2"])

                    if confirm == "1":
                        data["wallet_slot_one"] = "empty slot one"

                        data["balance"] += data["slot_one_balance"]
                        data["slot_one_balance"] -= data["slot_one_balance"]

                        print("slot one deleted")

                        save_data()
                        
                    else:
                        input("Enter to continue")

            #slot two
            elif selection_k == "2":
                if data["wallet_slot_two"] == "empty slot two":
                    print("slot is empty")

                else:
                   print("are you sure you want to delete " + data["wallet_slot_two"] + "?")
                   print("""
1. yes
2. no                                      
                   """)
                   #comfermation
                   confirm = get_valid_selection("confirmation: ", ["1", "2"])

                   if confirm == "1":
                        data["wallet_slot_two"] = "empty slot two"

                        data["balance"] += data["slot_two_balance"]
                        data["slot_two_balance"] -= data["slot_two_balance"]

                        print("slot two deleted")

                        save_data()

            #slot three
            else:
                if data["wallet_slot_three"] == "empty slot three":
                    print("slot is empty")

                else:
                    #comfermation
                    print("are you sure you want to delete " + data["wallet_slot_three"] + "?")
                    print("""
1. yes
2. no                   
                    """)
                    confirm = get_valid_selection("confirmation: ", ["1", "2"])

                    if confirm == "1":
                        data["wallet_slot_three"] = "empty slot three"

                        data["balance"] += data["slot_three_balance"]
                        data["slot_three_balance"] -= data["slot_three_balance"]

                        print("slot three deleted")

                        save_data()

                    else:
                        input("Enter to continue")


    # Goal
    elif selection == "5":
        print("""
1. Set Goal
2. View Goal
""")
        selection_d = get_valid_selection("Choose an option: ", ["1", "2"])

        if selection_d == "1":
            data["goal"] = input("Goal name: ")
            data["goal_price"] = get_valid_float("Price: $")

            print(f"Your goal is '{data['goal']}' and it will cost ${data['goal_price']:.2f}")
            print(f"Your goal balance is: ${data['goal_wallet']:.2f}")

        else:

            if data["goal_price"] == 0:
                print("You need to set a goal first.")

            else:
                progress = (data["goal_wallet"] / data["goal_price"]) * 100
                
                print(f"Progress toward '{data['goal']}': {progress:.2f}%")
                print(f"Your goal balance is: ${data['goal_wallet']:.2f}")

                if data["goal_wallet"] >= data["goal_price"]:
                    print("GOAL MET!!! 🎉")

        save_data()
        input("Press Enter to continue...")


    # Exit
    elif selection == "6":
        save_data()
        break
