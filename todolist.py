# Initial user welcome (with *PIZZAZZ*)
print(''' __      __   _                    _         _____ ___    ___   ___  _ 
 \ \    / /__| |__ ___ _ __  ___  | |_ ___  |_   _/ _ \  |   \ / _ \| |
  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \   | || (_) | | |) | (_) |_|
   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/   |_| \___/  |___/ \___/(_)
                                                                       
                                                                       ''')

# Function to list user options
def show_user_options():
    print('''\nWhat would you like to do?
    1. Show List
    2. Add Task
    3. Add Subtask
    4. Edit Task
    5. Edit Subtask
    6. Delete Task
    7. Delete Subtask
    8. Clear List
    9. Exit\n''')

# Function to handle user's selected option. Keeps providing user options until provided an explicit exit request.
def user_option_handler(to_do_list):
    while True:
        show_user_options()
        user_option = input('Enter a number: ')

        if user_option == '1':
            show_list(to_do_list)
        elif user_option == '2':
            parent_task = input('Enter the task you want to add: ')
            add_task(to_do_list, parent_task)
        elif user_option == '3':
            parent_task = input('Enter the task to add a subtask to [CASE SENSITIVE]: ')
            if parent_task in to_do_list:
                subtask = input('Enter the subtask: ')
                add_subtask(to_do_list, parent_task, subtask)
            else:
                print(f"Task '{parent_task}' not found.")
        elif user_option == '4':
            parent_task = input('Enter the task you want to edit [CASE SENSITIVE]: ')
            edit_task(to_do_list, parent_task)
        elif user_option == '5':
            subtask = input('Enter the subtask you want to edit [CASE SENSITIVE]: ')
            parent_task = input('Enter the parent task: ')
            edit_subtask(to_do_list, parent_task, subtask)
        elif user_option == '6':
            parent_task = input('Enter the task you want to delete [CASE SENSITIVE]: ')
            delete_task(to_do_list, parent_task)
        elif user_option == '7':
            parent_task = input('Enter the parent task: ')
            subtask = input('Enter the subtask you want to delete [CASE SENSITIVE]: ')
            delete_subtask(to_do_list, parent_task, subtask)
        elif user_option == '8':
            clear_list(to_do_list)
        elif user_option == '9':
            if exit_application():
                break
        else:
            print('INVALID SELECTION. Please enter a valid option number.')

# Start of individual Operator Function Definitions
#Function to print existing list to the terminal. If empty, inform user, else print the existing list.
def show_list(to_do_list):
    if not to_do_list:
        print('Your to-do list is EMPTY')
    else: 
        print('Here is your current to-do list:')
        for task, subtasks in to_do_list.items():
            print(f"- {task}")
            for subtask in subtasks:
                print(f"  * {subtask}")

#Function to add parent task to list.
def add_task(to_do_list, parent_task):
    to_do_list[parent_task] = []
    print(f"Added task: {parent_task}")

#Function to add a subtask. Requires parent task to exist in order to add a subtask. 
def add_subtask(to_do_list, parent_task, subtask):
    to_do_list[parent_task].append(subtask)
    print(f"Added subtask: {subtask} under task: {parent_task}")

#Function to edit task. Task must exist to be edited. 
def edit_task(to_do_list, parent_task):
    if parent_task in to_do_list:
        new_task = input(f'Enter the new task name for "{parent_task}": ')
        to_do_list[new_task] = to_do_list.pop(parent_task)
        print(f"Task '{parent_task}' renamed to '{new_task}'")
    else:
        print(f"Task '{parent_task}' not found.")

#Function to edit a subtask. User identifies the parent task and then the subtask they wish to modify. Subtask must exist to be edited. 
def edit_subtask(to_do_list, parent_task, subtask):
    if parent_task in to_do_list and subtask in to_do_list[parent_task]:
        new_subtask = input(f'Enter the new subtask name for "{subtask}": ')
        index = to_do_list[parent_task].index(subtask)
        to_do_list[parent_task][index] = new_subtask
        print(f"Subtask '{subtask}' renamed to '{new_subtask}'")
    else:
        print(f"Subtask '{subtask}' not found under task '{parent_task}'.")

#Function to delete task. This operates under the assumption that no subtasks can exist with the absence of a parent task. Deletion of the parent results in the deletion of all subtasks.
def delete_task(to_do_list, parent_task):
    if parent_task in to_do_list:
        print('Deleting a Task results in the deletion of all associated subtasks.')
        user_acknowledgement = input('Continue? Y/N: ').upper()
        if user_acknowledgement == "N":
            return
        else: 
            del to_do_list[parent_task]
            print(f"Deleted task: {parent_task}")
    else:
        print(f"Task '{parent_task}' not found.")

#function to delete subtask
def delete_subtask(to_do_list, parent_task, subtask):
    if parent_task in to_do_list and subtask in to_do_list[parent_task]:
        to_do_list[parent_task].remove(subtask)
        print(f"Deleted subtask: {subtask} under task: {parent_task}")
    else:
        print(f"Subtask '{subtask}' not found under task '{parent_task}'.")

#Function to clear entire list
def clear_list(to_do_list):
    to_do_list.clear()
    print("Cleared all tasks from your list.")

#Function to exit the application
def exit_application():
    print('\nExiting Application. Your content will NOT be saved.\n')
    user_confirmation = input('Continue? Y/N: ').upper()
    if user_confirmation == 'Y':
        print('''
        ,___,
        (9v9)
        (_^((\ Goodbye
        
        ''')
        return True
    else:
        print("Returning to menu")
        return False

# Start application with empty to-do list
to_do_list = {}

# Start functoin that handles user feedback until application explicitly tells loop to break via exit function
user_option_handler(to_do_list)
