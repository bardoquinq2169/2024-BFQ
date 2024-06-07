# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # check user response, question
        # repeat if users don't enter yes/no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes/no")


def instructions():
    print('''


**** Instructions ****

To begin, decide how many questions you would like to receive. 
Press <enter> for infinite mode.

Choose difficulty level of your questions, 1 being the easiest level, 
2 being moderate and 3 being the hardest level.

The questions will differ from addition, subtraction,
multiplication, and division. 

Press <xxx> to end the game at anytime.
    ''')


# loop for testing purposes

# Main routine

print()
print("➕➖✖️➗ - Welcome to Queenie's Basic Facts quiz - ➕➖✖️➗")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# check is users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()


