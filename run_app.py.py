from flask import Flask, render_template,request
from flask import redirect, url_for
import sqlite3
import os

def get_database_path(database_filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_directory, database_filename)
    return database_path

app = Flask(__name__)

database_filename = "books_database.db"
database_path = get_database_path(database_filename)

def dbConnection():
    try:
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print("SQLite Error:", e)
        return None

def get_table_names(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

@app.route('/')
def createMain():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name}'
    book_data = conn.execute(query).fetchall()

    return render_template("index.html", book_data = book_data, table_name = table_name)

@app.route('/about')
def about():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[1]

    query = f'SELECT * FROM {table_name}'
    feature_data = conn.execute(query).fetchall()

    return render_template("about.html", feature_data = feature_data, table_name = table_name)
    
@app.route('/about_me')
def about_us():
    return render_template("about_us.html")  # Update the template name accordingly
@app.route('/add_book', methods=['POST'])
def add_book():
    if request.method == 'POST':
        book_name = request.form['bookName']
        upc = request.form['upc']
        product_type = request.form['productType']
        price_excl_tax = request.form['priceExclTax']
        price_incl_tax = request.form['priceInclTax']
        tax = request.form['Tax']
        availability = request.form['availability']
        description = request.form['description']
        review = request.form['review']

        conn = dbConnection()
        cursor = conn.cursor()

        # Assuming you have a 'books' table with appropriate columns
        cursor.execute("""
            INSERT INTO books_table (Title, UPC, Product_Type, Price_excl_tax, Price_incl_tax,Tax,Availability, Description, Reviews)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)
        """, (book_name, upc, product_type, price_excl_tax, price_incl_tax, tax,availability, description, review))

        conn.commit()
        conn.close()

        # Redirect to the main page after adding the book
        return redirect(url_for('createMain'))
        
@app.route('/delete_book/<string:book_title>')
def delete_book(book_title):
    conn = dbConnection()
    cursor = conn.cursor()

    # Assuming your books table has an 'id' column as the primary key
    cursor.execute("DELETE FROM books_table WHERE Title=?", (book_title,))


    conn.commit()
    conn.close()

    # Redirect to the main page after deleting the book
    return redirect(url_for('createMain'))

if __name__ == '__main__':
    app.run(debug=True)