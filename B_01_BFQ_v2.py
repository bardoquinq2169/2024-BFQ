import random


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


# Instructions for the user if they want to know
def instructions():
    print('''


**** Instructions ****

To begin, decide how many questions you would like to receive. 
Press <enter> for infinite mode.

Choose difficulty level of your questions between levels 1 - 5, 1 being the easiest level, 
and 5 being the hardest level.

Choose what type of questions you would like.
Options are : Addition, Subtraction, Multiplication, Division and Mix

Press <xxx> to end the game at anytime.
    ''')


# checks for an integer
# lower limits and an optional exit code for infinite mode
def int_check(question, low=None, high=None, exit_code="xxx"):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"
    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    # if the number needs to be between low and high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()
        # check for infinite mode / exit code
        if response == exit_code:
            return response
        try:
            response = int(response)
            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)
            # check response is more than the low number
            elif high is not None and response > high:
                print(error)
            # if the response is valid, return it
            else:
                return response
        except ValueError:
            print(error)


def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a valid option from the following list: {valid_ans}'"
    while True:
        # Get user response and make sure it's lowercase
        user_response = input(question).lower()
        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item
        # print error if user does not enter something that is valid
        print(error)
        print()


# Main routine
mode = "regular"
end_game = "no"
feedback = ""

print()
print("➕➖✖️➗ - Welcome to Queenie's Basic Facts quiz - ➕➖✖️➗")
print()

# asking user if they want to read instructions
want_instructions = yes_no("Do you want to read the instructions? ")
# check is users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
number_questions = int_check("How many questions would you like? Push <enter> for infinite mode>: ",
                             low=1, exit_code="")
if number_questions == "":
    mode = "infinite"
    print("you chose infinite")
    number_questions = 5

question_number = 0
question_correct = 0
question_incorrect = 0
feedback = ""
quiz_history = []
history = []
bf_list = ["addition", "subtraction", "multiplication", "division", "mix"]

# ask user what type of operations they would like
# includes the option to have mixed operations
basic_facts_type = string_checker("What type of operation would you like? "
                                  "(addition, subtraction, multiplication, division, mix) ", bf_list)

# ask user what difficulty level they would like
difficulty_level = int_check("What level of difficulty would you like your questions?? (Choose from levels 1-5): ",
                             low=1, high=5)

# loops while question_num is lower than amount of questions - chosen at the start
# Quiz question loop starts here
while question_number < number_questions:
    # Question headings
    if mode == "infinite":
        question_heading = f"\n--- Question {question_number + 1} (Infinite Mode) ---"
    else:
        question_heading = f"\n💿💿💿 Question {question_number + 1} of {number_questions} 💿💿💿"
    print(question_heading)
    # Generates the numbers for the question and difficulty
    if difficulty_level == 1:
        num_1 = random.randint(1, 5)
        num_2 = random.randint(1, 5)
    elif difficulty_level == 2:
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 10)
    elif difficulty_level == 3:
        num_1 = random.randint(1, 15)
        num_2 = random.randint(1, 15)
    elif difficulty_level == 4:
        num_1 = random.randint(1, 20)
        num_2 = random.randint(1, 20)
    else:
        num_1 = random.randint(1, 25)
        num_2 = random.randint(1, 25)
    # generates a number to make sure the correct answer is an integer
    num_3 = num_1 * num_2
    num_4 = num_1 + num_2
    random_bf_list = ["addition questions", "subtraction questions", "multiplication questions", "division questions"]
    # generates the question type
    if basic_facts_type == "addition":
        question = "addition questions"
    elif basic_facts_type == "subtraction":
        question = "subtraction questions"
    elif basic_facts_type == "multiplication":
        question = "multiplication questions"
    elif basic_facts_type == "division":
        question = "division questions"
    else:
        question = random.choice(random_bf_list)

    user_chose = 0
    already_tried = []
    chances_allowed = 3
    user_choice = ""
    # generates the question format
    if question == "addition questions":
        answer = num_1 + num_2
        question_form = f"What is {num_1} + {num_2} ? "
    elif question == "subtraction questions":
        answer = num_1
        question_form = f"What is {num_4} - {num_2} ? "
    elif question == "multiplication questions":
        answer = num_1 * num_2
        question_form = f"What is {num_1} * {num_2} ? "
    elif question == "division questions":
        answer = num_1
        question_form = f"What is {num_3} / {num_2} ? "

    while user_choice != answer and user_chose < chances_allowed:
        user_choice = int_check(question_form)
        # check that they don't want to quit
        if user_choice == "xxx":
            # set end_game to use that outer loop can be broken
            end_game = "yes"
            break
        # add one to the number of guesses used
        user_chose += 1
        # checks if user has already tried their answer before
        if user_choice in already_tried:
            user_chose += -1
            print(f"You've already tried {user_choice}. You have used {user_chose} / {chances_allowed} chances")
            continue
        else:
            already_tried.append(user_choice)
        # allows user to try to answer the question again until they have run out of chances
        if user_choice != answer and user_chose < chances_allowed:
            print(f"Wrong answer!😔 Try again! You have used {user_chose} / {chances_allowed} chances")
        # feedback if user was unable to answer the question correctly
        elif user_choice != answer and user_chose == chances_allowed:
            feedback = "Sorry - you were unable to answer it correctly😔" \
                       f"The answer was {answer}"
            question_incorrect += 1
            history.append(feedback)
        # gives feedback if they answer correctly
        else:
            if user_choice == answer and user_chose == 1:
                feedback = "Amazing!! You got the answer in one go!"
                history.append(feedback)
            elif user_choice == answer and user_chose == chances_allowed:
                feedback = f"Phew! You got the answer in {user_chose} chances."
                history.append(feedback)
            elif user_choice == answer:
                feedback = f"Well done! You answered the question in {user_chose} chances."
                history.append(feedback)
    # print feedback to user
    print(feedback)

    if end_game == "yes":
        break

    # history and feedback
    history_item = f"Question {question_number + 1}: {feedback}"
    quiz_history.append(history_item)

    question_number += 1

    # if users are in infinite mode, increase number of questions!
    if mode == "infinite":
        number_questions += 1

# quiz history / statistics area
# calculate statistics
if question_number > 0:
    question_correct = question_number - question_incorrect
    percent_correct = question_correct / question_number * 100
    percent_incorrect = question_incorrect / question_number * 100

    print()
    print("📊📊📊 Quiz Statistics 📊📊📊")
    print(f"😊 Questions you got correct: {percent_correct:.2f} \t")
    print(f"😢 Questions you got incorrect: {percent_incorrect:.2f} \t")

    # ask user if they want to see their game history and output it if requested.
    see_history = yes_no("\nDo you want to see your quiz history? ")
    if see_history == "yes":
        for item in quiz_history:
            print(item)

    print()
    print("Thanks for using my quiz!")

else:
    print("Oops - You chickened out!")
