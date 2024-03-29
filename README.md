# Capstone Projects
This repository contains some of the Capstone projects I completed during my Data Science bootcamp. All programmes have been written in Python.

## Contents
- T21 / **Capstone II** - Task Manager
  - Installation
  - Usage
  - Additional notes
- T36 / **Capstone IV** - Exploratory Data Analysis
  - Installation
  - Usage
- T39 / **Capstone V** - Databases (SQLite)
  - Installation
  - Usage
- T51 / **Capstone VII** - Unsupervised Machine Learning & Principal Component Analysis
  - Installation
  - Usage
- Acknowledgements

## Task 21 (Capstone II)
The programme is a task manager, which allows users to "sign in" and use the programme to view their tasks, mark them as read, and add new tasks. For the admin user, there is the additional functionality of registering new users, viewing all tasks, and generating reports, and displaying task/user statistics. The programme's "internal" data is stored, read from, and written to .txt files.

### Installation
Navigate to the master branch, open folder **T21/Capstone_II** and download its contents. 

### Usage
Open the file **task_manager.py** in a suitable IDE and run the programme, ensuring that the downloaded .txt files are also in the working directory. 

![](https://github.com/victoriadw/CapstoneProjects/blob/364de590b1315d23e3c184be83684165d3c8a2f7/T53/imgs/T21_login.png)

You can use the login details of the "admin" user to access the programme (username: admin, password: adm1n). The username and password details for users on the programme are stored in the text file **user.txt**. You will now be able to access the rest of the programme. Navigate through the programme by entering the relevant options as displayed on the terminal. 

![](https://github.com/victoriadw/CapstoneProjects/blob/dc89c97a4f264e04655d2c71cfeff89e9b093360/T53/imgs/T21_menu.png)

As an example, users can view their tasks by entering `vm` into the terminal.

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T21_view_tasks.png)

The user can then select one of their tasks and choose to mark the task as completed.

Another example of the programme's functionality is to view the task and user statistics by entering `ds`.

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T21_display_statistics.png)

This functionality is only available to the admin user, as is the "register new user" function, and "generate reports" function.

### Additional notes
This programme was substantially based on a template provided by HyperionDev, and modified to eliminate bugs and add additional functionality.

## Task 36 (Capstone IV)
This project is an exploratory data analysis on the [Forbes Richest Athletes dataset](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T36/Capstone_IV/fra.csv). 

### Installation
Navigate to the master branch, open folder **T36/Capstone_IV** and download its contents. Using a suitable code editor that supports .ipynb files (e.g. VS Code), open up Capstone_VII.ipynb. Ensure that the downloaded files are in the working directory, and check that you have installed all of the necessary libraries imported in the first kernel. You should now be able to run the file and make any changes as necessary.

### Usage
You can view the complete analysis by simply opening [Capstone IV - Atheletes.ipynb](https://github.com/victoriadw/CapstoneProjects/blob/master/T36/Capstone_IV/Capstone%20IV%20-%20Athletes.ipynb) on github. Furthermore, there is a written report amongst the files called [EDA_Capstone_IV](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T36/Capstone_IV/EDA_Capstone_IV.pdf), containing a detailed review of the analysis. However, if you would like to make changes to the code, simply follow the installation instructions above and edit the code as you wish. 


## Task 39 (Capstone V)
This project is a database designed to be used by a bootstore clerk. The user can add new books to the database, update book information (name, author, or quantity), delete books, search for a book, and to view the entire database. This programme was made using the sqlite3 Python module. 

### Installation
Navigate to the master branch, open folder **T39/Capstone_V** and download its contents.

### Usage
Open the file **Capstone Project V.py** in a suitable IDE and run the programme, ensuring that **ebookstore.db** is also in the working directory. Run the programme. You will be confronted with the main menu, as below:

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T39_main_menu.png)

The contents of the entire database can be viewed by entering `5` into the terminal:

![](https://github.com/victoriadw/CapstoneProjects/blob/27cd751efeeb3c8a8d03cfb905f5d577f2f28813/T53/imgs/T39_whole_database.png)

The user can add a book to the database by entering `1`, entering the details as prompted, and then confirming whether they would like to add the book.

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T39_add_book.png)

The database can also be searched, by book ID, title, or author. In this example the user enters "Dahl" and all books by authors containing that name appear in the search results.

![](https://github.com/victoriadw/CapstoneProjects/blob/master/T53/imgs/T39_search_book.png)

A book can be deleted from the database by entering the book ID, which the user can find out by accessing the database information using one of the functions above. The user is prompted to enter the ID, and then confirm whether they would like to delete the record.

![](https://github.com/victoriadw/CapstoneProjects/blob/master/T53/imgs/T39_delete_book.png)


## Task 51 (Capstone VII)
This project is an analysis on the [USArrests dataset](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T51/Capstone_VII/UsArrests.csv), using Principal Components Analysis (PCA) and machine learning methods (hierarchical clustering, *k*-means clustering). 

### Installation
Navigate to the master branch, open folder **T51/Capstone_VII** and download its contents. Using a suitable code editor that supports .ipynb files (e.g. VS Code), open up Capstone_VII.ipynb. Ensure that the downloaded files are in the working directory, and check that you have installed all of the necessary libraries imported in the first kernel. You should now be able to run the file and make any changes as necessary.

### Usage
You can view the complete analysis by simply opening [Capstone_VII.ipynb](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T51/Capstone_VII/Capstone_VII.ipynb) on github. However, if you would like to make changes to the code, simply follow the installation instructions above and edit the code as you wish.

## Acknowledgements
This project was created by Victoria Daramy-Williams, using the resources provided by HyperionDev.
