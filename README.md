# Capstone Projects
This repository contains some of the Capstone projects I completed during my Data Science bootcamp with HyperionDev. Access the files by navigating to the [master](https://github.com/victoriadw/CapstoneProjects/tree/master) branch. All programmes have been written in Python.

## Contents
1. T21 / **Capstone II** - Lists, Functions, and String Handling
2. T36 / **Capstone IV** - Exploratory Data Analysis
3. T39 / **Capstone V** - Databases (SQLite)
4. T51 / **Capstone VII** - Unsupervised Machine Learning & Principal Component Analysis
5. Acknowledgements

## Task 21 (Capstone II)
The programme is a task manager, which allows users to "sign in" and use the programme to view their tasks, mark them as read, and add new tasks. For the admin user, there is the additional functionality of registering new users, viewing all tasks, and generating reports, and displaying task/user statistics. The programme's "internal" data is stored, read from, and written to .txt files.

### Installation instructions
Navigate to the master branch, open folder **T21/Capstone_II** and download its contents. 

### Usage
Open the file **task_manager.py** in a suitable IDE and run the programme, ensuring that the downloaded .txt files are also in the working directory. Run the programme.

![](https://github.com/victoriadw/CapstoneProjects/blob/364de590b1315d23e3c184be83684165d3c8a2f7/T53/imgs/T21_login.png)

You can use the login details of the "admin" user to access the programme (username: admin, password: adm1n). The username and password details for users on the programme are stored in the text file **user.txt**. You will now be able to access the rest of the programme. Navigate through the programme by entering the relevant options as displayed on the terminal. 

![](https://github.com/victoriadw/CapstoneProjects/blob/dc89c97a4f264e04655d2c71cfeff89e9b093360/T53/imgs/T21_menu.png)

As an example, users can view their tasks by entering `vm` into the terminal.

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T21_view_tasks.png)

The user can then select one of their tasks and choose to mark the task as completed.

Another example of the programme's functionality is to view the task and user statistics by entering `ds`.

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T21_display_statistics.png)

### Additional notes
This programme was substantially based on a template provided by HyperionDev, and modified to eliminate bugs and add additional functionality.

## Task 36 (Capstone IV)
This project is an exploratory data analysis on the [Forbes Richest Athletes dataset](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T36/Capstone_IV/fra.csv). 

### Installation instructions
Navigate to the master branch, open folder **T36/Capstone_IV** and download its contents. Using a suitable code editor that supports .ipynb files (e.g. VS Code), open up Capstone_VII.ipynb. Ensure that the downloaded files are in the working directory, and check that you have installed all of the necessary libraries imported in the first kernel. You should now be able to run the file and make any changes as necessary.

### Usage
You can view the complete analysis by simply opening [Capstone IV - Atheletes.ipynb](https://github.com/victoriadw/CapstoneProjects/blob/master/T36/Capstone_IV/Capstone%20IV%20-%20Athletes.ipynb) on github. Furthermore, there is a written report amongst the files called [EDA_Capstone_IV](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T36/Capstone_IV/EDA_Capstone_IV.pdf), containing a detailed review of the analysis. However, if you would like to make changes to the code, simply follow the installation instructions above and edit the code as you wish. 


## Task 39 (Capstone V)
This project is a database designed to be used by a bootstore clerk. The user can add new books to the database, update book information, delete books, search for a book, and to view the entire database. This programme was made using the sqlite3 Python module. 

### Installation instructions
Navigate to the master branch, open folder **T39/Capstone_V** and download its contents.

### Usage

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T39_main_menu.png)

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T39_full_database.png)

![](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T53/imgs/T39_add_book.png)

![](https://github.com/victoriadw/CapstoneProjects/blob/master/T53/imgs/T39_search_book.png)

![](https://github.com/victoriadw/CapstoneProjects/blob/master/T53/imgs/T39_delete_book.png)


## Task 51 (Capstone VII)
This project is an analysis on the [USArrests dataset](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T51/Capstone_VII/UsArrests.csv), using Principal Components Analysis (PCA) and machine learning methods (hierarchical clustering, *k*-means clustering). 

### Installation instructions
Navigate to the master branch, open folder **T51/Capstone_VII** and download its contents. Using a suitable code editor that supports .ipynb files (e.g. VS Code), open up Capstone_VII.ipynb. Ensure that the downloaded files are in the working directory, and check that you have installed all of the necessary libraries imported in the first kernel. You should now be able to run the file and make any changes as necessary.

### Usage
You can view the complete analysis by simply opening [Capstone_VII.ipynb](https://github.com/victoriadw/CapstoneProjects/blob/80012f1d4a4b3f67623fd8e109e147c5be4192a4/T51/Capstone_VII/Capstone_VII.ipynb) on github. However, if you would like to make changes to the code, simply follow the installation instructions above and edit the code as you wish.

## Acknowledgements
This project was created by Victoria Daramy-Williams, using the resources provided by HyperionDev.
