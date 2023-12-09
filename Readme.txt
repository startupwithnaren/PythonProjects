Project Name Technical Documentation

1. Folder Structure

1.1 Overview
The project structure is designed for clarity and organization:

instance: Configuration file (if applicable). This directory can be used for storing sensitive information like API keys or database connection details.
templates: Contains HTML templates used by the Flask application (index.html and about.html).

books_database: Stores the database files related to books.
python scrap: File responsible for web scraping to update the books_database.

run_app.py: The main backend file that initializes and runs the Flask application.

1.2 Example

plaintext
Copy code
/project_name
|-- instance
|   |-- config.py
|-- templates
|   |-- index.html
|   |-- about.html
|-- books_database
|   |-- books_database.db
|-- python scrap
|   |-- scrape_books.py
|-- run_app.py


2. Usage Instructions

2.1 Prerequisites

Ensure the following software is installed:

Python 3.x
Pip (Python package installer)
2.2 Database Initialization
Open a command prompt.

Navigate to the python scrap directory.

bash
Copy code
cd /path/to/project_name/python scrap
Execute the web scraping script to update the books_database.

bash
Copy code
python scrape_books.py
2.3 Running the Application
Open a command prompt.

Navigate to the project folder.

bash
Copy code
cd /path/to/project_name
Execute the Flask application.

bash
Copy code
python run_app.py
Open a web browser and go to http://localhost:5000 to access the application.

3. HTML Code
3.1 templates/index.html
(Your existing HTML code remains unchanged.)

4. Flask Code
4.1 run_app.py
(Your existing Flask code remains unchanged.)

5. Database Management
5.1 Scraping Data
To update the books_database, run the following command in the python scrap directory:

bash
Copy code
python scrape_books.py

5.2 Adding a Book
Visit the main page (http://localhost:5000).
Scroll down to the "Add a New Book" section.
Fill in the required details and click "Submit."

5.3 Deleting a Book
Navigate to the main page.
Each book entry includes a "Delete" button.
Click the "Delete" button to remove the corresponding book from the database.