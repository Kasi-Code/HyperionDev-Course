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
        "ophthalmologist@pymail.com", "Problem With The RE.", 
        "Please have a look at the scans I have attached for you."
    )
    inbox.append(ophthalmologist_email)

    optometrist_email = Email(
        "optometrist@pymail.com", "AMD To Inject.", 
        "PX 293344 would like to go ahead."
    )
    inbox.append(optometrist_email)

    nurse_email = Email(
        "nurse@pymail.com", "Visit PX 293344 Tomorrow.", 
        "Please travel to see PX at 9:00am."
    )
    inbox.append(nurse_email)



def list_emails():

    populate_inbox()
    
    # Create a function which prints the email’s subject_line, along with a corresponding number.
    for i, e in enumerate(inbox):
        print(e.subject_line, e.email_content)

# def read_email(index):

#     # Create a function which displays a selected email. 
#     # Once displayed, call the class method to set its 'has_been_read' variable to True.

# # --- Email Program --- #

# # Call the function to populate the Inbox for further use in your program.

# # Fill in the logic for the various menu operations.
# menu = True

# while True:
#     user_choice = int(input('''\nWould you like to:
#     1. Read an email
#     2. View unread emails
#     3. Quit application

#     Enter selection: '''))
       
#     if user_choice == 1:
#         # add logic here to read an email
        
#     elif user_choice == 2:
#         # add logic here to view unread emails
            
#     elif user_choice == 3:
#         # add logic here to quit appplication

#     else:
#         print("Oops - incorrect input.")

