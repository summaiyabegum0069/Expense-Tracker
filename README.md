# Expense Tracker

A beginner-friendly Python command-line application for managing daily expenses. The application allows users to add, view, update, delete, and categorize expenses, with JSON-based file storage for data persistence.

## Features

* Add new expenses
* View all expenses
* Calculate total expenses
* View expenses by category
* Update existing expenses
* Delete expenses
* Save expenses to a JSON file
* Load saved expenses when the application starts
* Automatically records the expense date
* Input validation and error handling
* Prevents duplicate expense IDs

## Expense Categories

The application supports:

* Food
* Travel
* Shopping
* Entertainment
* Bills
* Education
* Other

## Technologies Used

* **Python**
* **JSON**
* **File Handling**
* **Exception Handling**
* **datetime**

## Python Concepts Demonstrated

* Variables and data types
* Lists
* Dictionaries
* Conditional statements
* Loops
* Functions
* Exception handling
* File handling
* JSON serialization and deserialization
* CRUD operations

## How to Run

### Prerequisites

Make sure Python is installed on your system.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/summaiyabegum0069/Expense-Tracker.git
```

2. Open the project folder:

```bash
cd Expense-Tracker
```

3. Run the application:

```bash
python main.py
```

## Data Storage

Expense data is stored locally in `expenses.json`.

The application automatically loads previously saved expenses when it starts.

The JSON file is excluded from the Git repository using `.gitignore` so personal expense data is not uploaded to GitHub.

## Project Structure

```text
Expense-Tracker/
│
├── main.py
├── README.md
└── .gitignore
```

## Future Improvements

Possible future enhancements include:

* Monthly and yearly expense summaries
* Expense search and filtering
* Sorting expenses by amount or date
* Data visualization using charts
* Database integration
* Graphical user interface
* Exporting expense reports

## Author

**Summaiya Begum**

B.Tech Information Technology Student
