import sqlite3
from prettytable import PrettyTable

# create database
db = sqlite3.connect('ebookstore.db')

# get cursor object
cursor = db.cursor()

novels = [(3001, "A Tale of Two Cities", "Charles Dickens", 30),
         (3002, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", 40), 
         (3003, "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", "C.S. Lewis", 25), 
         (3004, "The Lord of the Rings", "J.R.R. Tolkien", 37), 
         (3005, "Alice in Wonderland", "Lewis Carroll", 12)]

# create and populate table, unless already created
try: 
    cursor.execute('CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT, Quantity INTEGER')
    cursor.executemany('INSERT INTO books(id, Title, Author, Quantity) VALUES (?,?,?,?)', novels)
except:
    pass

#############
# functions #
#############

def display(results):
    '''This function displays the table results in a user-friendly format'''

    col_names = ['id', 'Title', 'Author', 'Quantity']
    x = PrettyTable(col_names)

    for result in results:
        x.add_row(result)

    print(x)
    
def enter_book():
    '''This function allows the user to enter a new book into the database'''

    # generate id automatically as highest ID num + 1
    cursor.execute(f'SELECT MAX(id) FROM books')
    id_new = cursor.fetchone()[0] + 1

    # ask user for remaining input
    title_new = input('\nPlease enter the book title: ')
    author_new = input('Please enter the author name: ')
    # need quantity input to be valid integer
    while True:
        quant = input('Please enter the quantity of books: ')
        try:
            quant_int = int(quant)
            break
        except:
            print('Invalid quantity.\n')
    
    while True:
        # confirm with user if they want to add this entry
        confirm = input(f'\nInput the following data?\n\nTitle:\t\t{title_new}\nAuthor:\t\t{author_new}\nQuantity:\t{quant_int}\n\nPlease select an option (Y/N): ')
        if confirm.lower() == "y":
    # input new entry into database
            cursor.execute('INSERT INTO books(id, Title, Author, Quantity) VALUES (?,?,?,?)', (id_new, title_new, author_new, quant_int))
            db.commit()
            print("\nNew entry added to the database.")
            break
        elif confirm.lower() == 'n':
            print("\nEntry not added. Back to main menu\n")
            break
        else:
            print("Please enter a valid option.\n")

def update_book():
    '''This function allows the user to update a book by entering its ID'''

    # display book by id
    while True:
        id_update = input("Please select a book by entering its ID: ")
        try:
            id_update_int = int(id_update)
            cursor.execute(f'SELECT * FROM books WHERE id = {id_update_int}')
            results = cursor.fetchall()
            if results == []:
                print("No record with that ID exists in the database.\n")
            else:
                display(results)
                break
        except:
            print("Please enter a valid ID.\n")

    while True:
        edit_choice = input("""What would you like to update?

        1. Title
        2. Author
        3. Quantity
        0. Cancel

    """)
        choice = ["1", "2", "3", "4"]
        if edit_choice in choice:
            break
        else:
            print("Please select a valid option.\n ")
    if edit_choice == "1":
        new_title = input("Please enter the new title: ")
        cursor.execute(f'UPDATE books SET Title = {new_title} WHERE id = {id_update}')
        db.commit()
        print(f"Title has been updated to '{new_title}'.\n")
    elif edit_choice == "2":
        new_author = input("Please enter the new author name: ")
        cursor.execute(f'UPDATE books SET Author = {new_author} WHERE id = {id_update}')
        db.commit()
        print(f"Author name has been updated to '{new_author}'.\n")
    elif edit_choice == "3":
        while True:
            new_quant = input("Please enter the new quantity: ")
            try:
                new_quant_int = int(new_quant)
                break
            except:
                print("Please enter a valid quantity.")
        cursor.execute(f'UPDATE books SET Quantity = {new_quant_int} WHERE id = {id_update}')
        db.commit()
        print(f"Quantity has been updated to {new_quant}.\n")
    elif edit_choice == "4":
        print("Back to main menu.\n")
    return

def del_book():
    '''This function allows the user to delete a book by entering its ID'''

    # ask for id and display book
    while True:
        id_del = input("\nPlease select a book to delete by entering its ID: ")
        try:
            id_del_int = int(id_del)
            cursor.execute(f'SELECT id, Title, Author, Quantity FROM books WHERE id = {id_del_int}')
            results = cursor.fetchall()
            if results == []:
                print("No record with that ID exists in the database.\n")
            else:
                display(results)
                break
        except:
            print("Please enter a valid ID.\n")
    
    # confirm with user if they want to delete it
    while True:
        confirm = input("Are you sure you want to delete this entry? (Y/N)\n")
        if confirm.lower() == "y":
            cursor.execute(f'DELETE FROM books WHERE id = {id_del_int}')
            db.commit()
            print("This entry has been deleted.\n")
            break
        elif confirm.lower() == "n":
            print("Entry not deleted. Back to main menu\n")
            break
        else:
            print("Please enter a valid option.\n")

def search():
    '''This function allows a user to search for a record by ID, Title, or Author'''

    while True:
        search_by = input("""\nWhat would you like to search by?

        1. ID
        2. Title
        3. Author
        0. Cancel
        
        """)
        search_options = ["1", "2", "3", "0"]
        if search_by in search_options:
            break
        else:
            print("Please select a valid option.\n ")

    # search by ID number
    if search_by == "1":
        id_search = input("Please enter an ID number: ")
        try:
            id_search_int = int(id_search)
            cursor.execute(f'SELECT * FROM books WHERE id = {id_search_int}')
            results = cursor.fetchall()
            if results == []:
                print("No record with that ID exists in the database.\n")
            else:
                display(results)
        except:
            print("Please enter a valid ID number.\n\n")

    # search by title
    if search_by == "2":
        title_search = input("Please enter a title: ")
        cursor.execute('SELECT * FROM books WHERE Title LIKE ?', ('%'+title_search+'%',))
        results = cursor.fetchall()
        if results == []:
            print("No books by that title exist in the database.\n\n")
        else:
            display(results)

    # search by author
    elif search_by == "3":
        author_search = input("Please enter an author: ")
        cursor.execute('SELECT * FROM books WHERE Author LIKE ?', ('%'+author_search+'%',))
        results = cursor.fetchall()
        if results == []:
            print("No books by that author exist in the database.\n\n")
        else:
            display(results)
        
    elif search_by == "4":
        print("Back to main menu.\n\n")


def options():
    '''This function allows the user to select an option for the programme'''

    choice = input("""
    MAIN MENU

    Please select an option by entering a number:

    1. Enter book
    2. Update book
    3. Delete book
    4. Search books
    5. View entire database
    0. Exit
    
    """)
    choices = ["1","2","3","4","5","0"]
    if choice in choices:
        return choice
    else:
        print("Invalid option.")
        options()

##################
# main programme #
##################

while True:
    option = options()  
    if option == "1":
        enter_book()
    elif option == "2":
       update_book()
    elif option == "3":
        del_book()
    elif option == "4":
        search()
    elif option == "5":
        cursor.execute('SELECT * FROM books')
        whole_table = cursor.fetchall()
        display(whole_table)    
    elif option == "0":
        print("Goodbye!")
        exit()
    