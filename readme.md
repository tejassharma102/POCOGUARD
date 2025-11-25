# PocketGuard - Student Expense Management System

# 1. Project Overview
Greetings. PocketGuard is a desktop-based financial management application designed specifically to address the needs of university students. It is often observed that students living in hostels or shared accommodations struggle to keep track of their daily discretionary spending—such as tea, snacks, travel, and stationery. This lack of monitoring often leads to financial constraints before the month concludes.

PocketGuard solves this problem by providing a simple, digital, and user-friendly platform to record daily transactions. The primary objective is to allow users to set a personal budget limit and receive immediate feedback on their spending status, thereby promoting better financial discipline.

# 2. Key Features
The application has been engineered with the following specific capabilities to ensure utility and ease of use:

Interactive User Interface (GUI):* Unlike complex command-line tools, this application features a visual window with clear text boxes and buttons, making it accessible even to those with no programming knowledge.
Dynamic Budget Setting:* A dedicated feature allows the user to define their own monthly limit (e.g., Rs. 5000). This limit is saved permanently and can be updated at any time.
Persistent Data Storage:* The system utilizes a CSV (Comma Separated Values) file system to store every transaction. This ensures that your data remains safe even after you close the application or restart your computer.
Real-Time Analytics:* With a single click, the system calculates the sum of all expenses, compares it against your set budget, and provides a status report (e.g., "Safe" or "Over Budget").
Input Validation:* The system is designed to handle errors gracefully; for instance, if a user attempts to submit an empty form, it will politely request the necessary details.

# 3. Technologies & Tools Used
I have selected standard and reliable tools to build this project, ensuring it is lightweight and easy to run on any computer:

Python (Version 3.x):** The core logic is written in Python due to its readability and robust standard library.
Tkinter: I utilized Python’s built-in GUI library to create the windows, buttons, and input fields without requiring external downloads.
 CSV Module: Used for the database layer to read and write expense records in a structured format that can also be opened in Microsoft Excel.
 OS Module: Used to handle file path verifications to prevent the application from crashing if files are missing.

# 4. Project File Structure
To adhere to the principles of modular programming, the code is organized into five distinct files, each with a specific responsibility:

*main.py*: The entry point of the application. Running this file initializes the entire program.
*interface.py*: The "Presentation Layer." It contains all the code related to the window layout, labels, and button interactions.
*logic.py*: The "Application Layer." It handles the mathematics (summing totals) and the decision-making logic (comparing totals vs. budget).
*database.py*: The "Data Layer." It is responsible for all file operations—saving new records to the CSV and reading them back.
*settings.py*: A configuration file that stores global variables such as file names and window titles, making the code easier to maintain.

# 5. Detailed Installation Instructions
Please follow these steps carefully to set up the application on your system:

1.  Verify Python Installation:
    * Open your command prompt or terminal.
    * Type python --version. If a version number appears, you are ready to proceed.
2.  Download the Project:
    * Download the PocketGuard_GUI folder to your Desktop or preferred location.
    * Ensure all 5 Python files (main.py, interface.py, etc.) are present inside.
3.  Open in Editor:
    * Right-click the folder and select "Open with VS Code".
4.  Execute the Program:
    * Open the terminal inside VS Code.
    * Run the command:
        bash
        python main.py
        

# 6. Testing Guide
To verify the functionality of the software, you may perform the following test scenarios:
Scenario A: Setting a Budget
     Action: Click the orange "Set Budget" button and enter 1000.
     Expected Result: A popup confirms "Budget Updated," and a file named budget.txt is created.
Scenario B: Adding an Item
     Action: Enter "Textbook" in the Item Name box and 500 in the Price box. Click "Add Item".
     Expected Result: Fields clear automatically, and the data is appended to expenses.csv.
Scenario C: Checking Status
     Action: Click "Check Total".
     Expected Result: The report should show "Total Spent: 500" and Status: "Safe (Remaining: 500)".
Scenario D: Validation Test
     Action: Leave the boxes empty and click "Add Item".
     Expected Result: An error message appears saying "type something," preventing invalid data entry.

# 7. Future Enhancements
While the current version meets all primary requirements, I have identified areas for future improvement:
* Category Analysis: Adding a dropdown menu to categorize expenses (Food, Travel, etc.) for better insights.
* Delete Functionality: Implementing a feature to remove specific entries in case of mistakes.
* Graphical Charts: integrating matplotlib to show a pie chart of spending habits.

---
*Submitted by:*Tejas Sharma 
