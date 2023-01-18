import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%d %b %Y"

class Task:
    def __init__(self, username = None, title = None, description = None, due_date = None, assigned_date = None, completed = None, task_num = None):
        '''
        Inputs:
        username: String
        title: String
        description: String
        due_date: DateTime
        assigned_date: DateTime
        completed: Boolean
        task_num: String
        '''
        self.username = username
        self.title = title
        self.description = description
        self.due_date = due_date
        self.assigned_date = assigned_date
        self.completed = completed
        self.task_num = task_num

    def from_string(self, task_str):
        '''
        Convert from string in tasks.txt to object
        '''
        tasks = task_str.split(";")
        username = tasks[0]
        title = tasks[1]
        description = tasks[2]
        due_date = datetime.strptime(tasks[3], DATETIME_STRING_FORMAT)
        assigned_date = datetime.strptime(tasks[4], DATETIME_STRING_FORMAT)
        completed = True if tasks[5] == "Yes" else False
        task_num = tasks[6]
        self.__init__(username, title, description, due_date, assigned_date, completed, task_num)

    def to_string(self):
        '''
        Convert to string for storage in tasks.txt
        '''
        str_attrs = [
            self.username,
            self.title,
            self.description,
            self.due_date.strftime(DATETIME_STRING_FORMAT),
            self.assigned_date.strftime(DATETIME_STRING_FORMAT),
            "Yes" if self.completed else "No",
            self.task_num
        ]
        return ";".join(str_attrs)

    def display(self):
        '''
        Display object in readable format
        '''
        disp_str = f"Task number:\t {self.task_num}\n"

        if self.completed == True:
            disp_str += f"Task completed?: Yes\n"
        else:
            disp_str += f"Task completed:\t No\n"

        disp_str += f"Task: \t\t {self.title}\n"
        disp_str += f"Assigned to: \t {self.username}\n"
        disp_str += f"Date Assigned: \t {self.assigned_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {self.due_date.strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n{self.description}\n"
        return disp_str


# Read and parse tasks.txt
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]

task_list = []
for t_str in task_data:
    curr_t = Task()
    curr_t.from_string(t_str)
    task_list.append(curr_t)

# Read and parse user.txt

# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

# Keep trying until a successful login
logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

def validate_string(input_str):
    '''
    Function for ensuring that string is safe to store
    '''
    if ";" in input_str:
        print("Your input cannot contain a ';' character")
        return False
    return True

def check_username_and_password(username, password):
    '''
    Ensures that usernames and passwords can't break the system
    '''
    # ';' character cannot be in the username or password
    if ";" in username or ";" in password:
        print("Username or password cannot contain ';'.")
        return False
    return True

def write_usernames_to_file(username_dict):
    '''
    Function to write username to file

    Input: dictionary of username-password key-value pairs
    '''
    with open("user.txt", "w") as out_file:
        user_data = []
        for k in username_dict:
            user_data.append(f"{k};{username_dict[k]}")
        out_file.write("\n".join(user_data))
        

#########################
# Main Program Functions 
######################### 

def reg_user():
    # Request input of a new username
    if curr_user != 'admin':
        print("Registering new users requires admin privileges")
        return
    new_username = input("New Username: ")

    # check if username already taken
    with open("user.txt") as user_file:
        user_data = user_file.read().split("\n")
        username_password = {}
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password

        while new_username in username_password:
            new_username = input("Username already taken. Please enter a new username: ")
        else:
            pass

    # Request input of a new password
    new_password = input("New Password: ")

    if not check_username_and_password(new_username, new_password):
        # Username or password is not safe for storage - continue
        pass

    # Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # If they are the same, add them to the user.txt file
        print("New user added")

        # Add to dictionary and write to file
        username_password[new_username] = new_password
        write_usernames_to_file(username_password)

    # Otherwise you present a relevant message.
    else:
        print("Passwords do not match")

def add_task():
    # Prompt a user for the following: 
    #     A username of the person whom the task is assigned to,
    #     A title of a task,
    #     A description of the task and 
    #     the due date of the task.

    # Ask for username
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
        return

    # Get title of task and ensure safe for storage
    while True:
        task_title = input("Title of Task: ")
        if validate_string(task_title):
            break

    # Get description of task and ensure safe for storage
    while True:
        task_description = input("Description of Task: ")
        if validate_string(task_description):
            break

    # Obtain and parse due date
    while True:
        try:
            task_due_date = input("Due date of task (DD MMM YYYY): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")

    # Obtain and parse current date
    curr_date = date.today()

    # add task number
    task_num = str(len(task_list) + 1)
        
    # Create a new Task object and append to list of tasks
    new_task = Task(task_username, task_title, task_description, due_date_time, curr_date, False, task_num)
    task_list.append(new_task)

    # Write to tasks.txt
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n".join([t.to_string() for t in task_list]))
    print("Task successfully added.")    

def view_all():
    # view tasks from all users
    print("-----------------------------------\n")
    if len(task_list) == 0:
        print("There are no tasks.")
        print("-----------------------------------\n")

    for t in task_list:
        print(t.display())
        print("-----------------------------------")

def view_mine():
    # view tasks for current user
    print("\n-----------------------------------")
    has_task = False    
    for t in task_list:
        if t.username == curr_user:
            has_task = True
            print(t.display())
            print("-----------------------------------")
    
    if not has_task:
        print("You have no tasks.")
        print("-----------------------------------")
        return

    # allow user to select task and change completedness status if required
    while True:
        select = input("Please select a task by entering its number, or enter -1 to return to the main menu: ")
        if select == "-1":
            return
        try:    
            if int(select) in range(1,len(task_list)):
                choose = input("Would you like to mark this task as complete? (Y/N): ").lower()
                if choose == "n":
                    print("Back to menu")
                elif choose == "y" and task_list[int(select)-1].completed == True:
                    print("This task has already been completed.")
                elif choose == "y" and task_list[int(select)-1].completed == False:
                    print(f"Task {select} has been marked as complete!")
                    task_list[int(select)-1].completed = True
                    with open("tasks.txt","w") as file:
                        file.write("\n".join([t.to_string() for t in task_list]))                          
                else:
                    print("Please enter Y or N.")         
        except:
            print("Invalid entry. Please enter a valid task number: ")

def gen_reports(): 
    # generate task and user reports when requested
    num_tasks = len(task_list)
    num_users = len(username_password.keys())
    comp_tasks = 0
    uncomp_tasks = 0
    overdue_tasks = 0
    for t in task_list:
        if t.completed == True:
            comp_tasks += 1
        else:
            uncomp_tasks += 1
            if datetime.date(t.due_date) < date.today():
                overdue_tasks += 1

    with open("task_overview.txt","w") as file1:
        # add lines to file
        file1.write("-----------------------------------\n\nTasks Overview\n\n")
        file1.write(f"Number of tasks generated and tracked: {num_tasks}\n")
        file1.write(f"Total number of completed tasks: {comp_tasks}\n")
        file1.write(f"Total number of uncompleted tasks: {uncomp_tasks}\n")
        file1.write(f"Total number of overdue tasks: {overdue_tasks}\n")
        file1.write(f"Percentage of tasks that are not complete: {int(uncomp_tasks/num_tasks * 100)}%\n")
        file1.write(f"Percentage of tasks that are overdue: {int(overdue_tasks/num_tasks * 100)}%\n")
        file1.write("\n-----------------------------------")

    with open("user_overview.txt","w") as file2:
        file2.write("Users Overview\n\n")
        file2.write(f"Total number of registered users: {num_users}\n")
        for user in username_password.keys():
            user_comp_tasks = 0
            user_uncomp_tasks = 0
            user_overdue_tasks = 0
            num_tasks_user = 0
            for t in task_list:
                if user == t.username:
                    num_tasks_user += 1
                    if t.completed == True:
                        user_comp_tasks += 1
                    else:
                        user_uncomp_tasks += 1
                        if datetime.date(t.due_date) < date.today():
                            user_overdue_tasks += 1
            # add lines to file
            file2.write(f"\n{user} tasks overview:\n")
            file2.write(f"Number of tasks assigned to {user}: {num_tasks_user}\n")
            file2.write(f"Percentage of total number of tasks assigned: {int(num_tasks_user/num_tasks * 100)}%\n")
            file2.write(f"Percentage of tasks assigned that have been completed: {int(user_comp_tasks/num_tasks_user * 100)}%\n")
            file2.write(f"Percentage of tasks assigned that have not been completed: {int(user_uncomp_tasks/num_tasks_user * 100)}%\n")
            file2.write(f"Percentage of tasks assigned that are overdue: {int(user_overdue_tasks/num_tasks_user * 100)}%\n")
        file2.write("\n-----------------------------------\n")

def display_stats():
    # always regenerate reports when user calls ds to update them 
    # (even if file already exists) in case user hasn't updated 
    # during the programme
    gen_reports()
    with open("task_overview.txt") as file1:
        print()
        print(file1.read())
    with open("user_overview.txt") as file2:
        print()
        print(file2.read())

#########################
# Main Loop
######################### 

while True:
    # Get input from user
    print()
    if curr_user == 'admin':
        menu = input('''Select one of the following options below:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    gr - generate reports
    ds - display statistics
    e - exit
    : ''').lower()
    else:
        menu = input('''Select one of the following options below:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''').lower()

    if menu == 'r': # Register new user (if admin)
        reg_user()
    elif menu == 'a': # Add a new task
        add_task()
    elif menu == 'va': # View all tasks
        view_all()
    elif menu == 'vm': # View my tasks
        view_mine()
    elif menu == 'ds' and curr_user == 'admin': # If admin, display statistics
        display_stats()
    elif menu == 'gr' and curr_user == 'admin': # If admin, generate reports
        gen_reports()
        print("\nReports generated!\n")
    elif menu == 'e': # Exit program
        print('Goodbye!')
        exit()
    else: # Default case
        print("There is no such option. Please try again.")