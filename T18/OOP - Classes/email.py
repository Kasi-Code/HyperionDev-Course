### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:
    def __init__(self, email_address, subject_line, email_content):

    # Declare the class variable, with default value, for emails. 
        self.email_address = email_address
        self.subject_line = subject_line    
        self.email_content = email_content    

    # Initialise the instance variables for emails.
        self.has_been_read = False
    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        if not self.has_been_read:
            self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox():

    # Create 3 sample emails and add it to the Inbox list. 
    ophthalmologist_email = Email(
        "ophthalmologist@pymail.com", "Problem With The RE", 
        "Please have a look at the scans I have attached for you."
    )
    inbox.append(ophthalmologist_email)

    optometrist_email = Email(
        "optometrist@pymail.com", "AMD To Inject", 
        "PX 293344 would like to go ahead."
    )
    inbox.append(optometrist_email)

    nurse_email = Email(
        "nurse@pymail.com", "Visit PX 293344 Tomorrow", 
        "Please travel to see PX at 9:00 am."
    )
    inbox.append(nurse_email)

populate_inbox()

def list_emails():
    print("\nEmail Subject: -")

    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i,e in enumerate(inbox):
        if e.has_been_read:
            print(f"{i + 1}. seen:\t{e.subject_line}")
        else:
            print(f"{i + 1}. unread:\t{e.subject_line}")
      
list_emails()
print()

def read_email(index):

    # Create a function which displays a selected email. 
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    for i,e in enumerate(inbox):
        if i == index:
            print(
                f"""
--------------------------------------------
{e.subject_line}
To [{e.email_address}]

{e.email_content}
--------------------------------------------
    """
)
            e.mark_as_read()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.

# Fill in the logic for the various menu operations.
menu = True

while True:
    index = []
    for i, e in enumerate(inbox):
        index.append(i + 1)

    try:
        user_choice = int(input('''Would you like to:
        1. Read an email
        2. View unread emails
        3. Quit application

        Enter selection: '''))

        if user_choice == 1:
            # add logic here to read an email
            index = int(input(f"""
        Email: {', '.join(map(str, index))}

        Select one of the emails: """))
            if index < 0 or index > len(inbox):
                print("\nOops - incorrect input.\n")
            else:
                read_email(index - 1)
        elif user_choice == 2:
            # add logic here to view unread emails
            list_emails()
            print()

        elif user_choice == 3:
            # add logic here to quit application
            print("\nGoodbye!!\n")
            exit()
        else:
            print("\nOops - incorrect input.\n")
    except ValueError:
        print("\nPlease enter a valid integer.\n")
