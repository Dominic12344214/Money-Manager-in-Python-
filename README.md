A Personal Savings Tracker
Nest is a simple command-line application for managing your personal finances. It allows you to track savings, spending, and goal-oriented saving in a straightforward, interactive way. All your financial data is stored in a JSON file for persistence between sessions.

🛠 Features
🔹 Track three types of balances:

Savings

Spending

Goal Wallet

🔹 Set and monitor a financial goal with progress tracking

🔹 Add or remove money from any wallet

🔹 Split added funds by percentage between the three categories

🔹 Persistent data storage using a local nest_data.json file

🚀 Getting Started
Prerequisites
Python 3.x

Installation
Clone the repo or download the script:

bash
Copy
Edit
git clone https://github.com/yourusername/nest-tracker.git
cd nest-tracker
Run the program:

bash
Copy
Edit
python nest_tracker.py
📘 How It Works
When you launch the app, you'll be greeted with your current balances. From there, you can:

Add Money
Choose to add to savings, spending, goals, or split the amount among all three.

Remove Money
Take funds out of savings, goal wallet, or spending.

Set or View a Goal
Set a savings goal and track your progress toward it.

Exit
Your data is automatically saved when you exit the app.

🧠 Example Usage
pgsql
Copy
Edit
SELECT FUNCTION
1. Add money
2. Remove money
3. Goal
4. Exit
Selecting 1 (Add money) gives options to add to specific balances or split by percentage.

🗃 Data Persistence
All data is stored in nest_data.json in the same directory as the script. This ensures your progress and balances are saved between sessions.

📂 File Structure
pgsql
Copy
Edit
nest_tracker.py
nest_data.json (created after first run)
🔐 Notes
All input is validated to prevent negative amounts or invalid entries.

Make sure nest_data.json is in a writable location.

🙌 Contributions
Feel free to fork the project and submit pull requests! Whether it’s feature suggestions or bug fixes, your input is welcome.

📄 License
MIT License — do whatever you want, just don't blame me if it goes wrong. 😉
