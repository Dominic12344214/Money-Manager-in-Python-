
import json
import os

DATA_FILE = "nest_data.json"

# Default values
data = {
    "balance": 0.00,
    "spending_balance": 0.00,
    "goal_wallet": 0.00,
    "goal": "",
    "goal_price": 0.00
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
    print("\n==============================")
    print(f"Your savings balance is: ${data['balance']:.2f}")
    print(f"Your spending balance is: ${data['spending_balance']:.2f}")
    print(f"Your goal balance is: ${data['goal_wallet']:.2f}")
    print("==============================\n")

    print("""
SELECT FUNCTION
1. Add money
2. Remove money
3. transfer money
4. Goal
5. Exit
""")

    selection = get_valid_selection("Enter number corresponding with function: ", ["1", "2", "3", "4", "5"])

    # Add money
    if selection == "1":
        print("""
1. Add to savings
2. Add to spending
3. Add to goals
4. Split
""")

        selection_c = get_valid_selection("Choose an option: ", ["1", "2", "3", "4"])

        if selection_c == "1":
            amount = get_valid_float("Add money: $")
            data["balance"] += amount

            print(f"Your new balance is: ${data['balance']:.2f}")


        elif selection_c == "2":
            amount = get_valid_float("Add money: $")
            data["spending_balance"] += amount

            print(f"Your new spending balance is: ${data['spending_balance']:.2f}")


        elif selection_c == "3":
            amount = get_valid_float("Add money: $")
            data["goal_wallet"] += amount

            print(f"Your new goal balance is: ${data['goal_wallet']:.2f}")


        elif selection_c == "4":
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
    elif selection == "2":
        print("""
1. Remove from savings
2. Remove from spending
3. Remove from goal wallet
""")

        selection_b = get_valid_selection("Choose an option: ", ["1", "2", "3"])
        amount = get_valid_float("Remove money: $")

        if selection_b == "1":

            if amount > data["balance"]:
                print("Insufficient funds.")

            else:
                data["balance"] -= amount
                print(f"Your new savings balance is: ${data['balance']:.2f}")

        elif selection_b == "3":
            if amount > data["goal_wallet"]:
                print("Insufficient funds.")

            else:
                data["goal_wallet"] -= amount
                print(f"Your new goal balance is: ${data['goal_wallet']:.2f}")

        elif selection_b == "2":

            if amount > data["spending_balance"]:
                print("Insufficient funds.")

            else:
                data["spending_balance"] -= amount
                print(f"Your new spending balance is: ${data['spending_balance']:.2f}")

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

                if data > ["balance"]:
                    print("Insufficient funds.")

                else:
                    data["balance"] -= amount
                    data["spending_balance"] += amount

                    print(f"Your new balance is: ${data['balance']:.2f}")
                    print(f"Your new spending balance is: ${data['spending_balance']:.2f}")

                    input("enter to continue")

            elif selection_f == "2":
                amount = get_valid_float("Move from saving to spending: $")

                if data > ["balance"]:
                    print("Insufficient funds")

                else:
                    data["balance"] -= amount
                    data["goal_wallet"] += amount

                    print(f"your new balance is: ${data["balance"]:.2f}")
                    print (f"your new goal balance is: ${data["goal_wallet"]:.2f}")

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

                if data > ["spending_balance"]:
                    print("Insufficient funds")
                    
                else:
                    data["spending_balance"] -= amount
                    data["balance"] += amount
                    
                    print(f"your new spending balance is: ${data["spending_balance"]:.2f}")
                    print(f"your new saving balance is: ${data["balance"]:.2f}")
                    
                    input("enter to continue")
                    
            #spending to goals
            elif selection_g == "2":
                amount = get_valid_float("move from spending to goals: $")
                
                if data > ["spending_balance"]:
                    print("Insufficient funds")
                
                else:
                    data["spending_balance"] -= amount
                    data["goal_wallet"] += amount
                    
                    print(f"your new spending balance is: ${data["spending_balance"]:.2f}")
                    print(f"your new goal balance is: ${data["goal_wallet"]:.2f}")
                    
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
                
                if data > ["goal_wallet"]:
                    print("Insufficient funds")
                    
                else:
                    data["goal_wallet"] -= amount
                    data["balance"] += amount
                    
                    print(f"your new goal balance is: ${data["goal_wallet"]:.2f}")
                    print(f"your new savings balance is: ${data["balance"]:.2f}")
                    
                    input("enter to continue")
                    
            #goal to spending
            elif selection_h == "2":
                amount = get_valid_float("move from goals to spending: $")
                
                if data > ["goal_wallet"]:
                    print("Insufficient funds")
                    
                else:
                    data["goal_wallet"] -= amount
                    data["spending_balance"] += amount
                    
                    print(f"your new goal balance is: ${data["goal_wallet"]:.f2}")
                    print(f"your new spending balance is: ${data["spending_balance"]:.f2}")
                    
                    input("enter to continue")
                    
    # Goal
    elif selection == "4":
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
    elif selection == "5":
        save_data()
        break
