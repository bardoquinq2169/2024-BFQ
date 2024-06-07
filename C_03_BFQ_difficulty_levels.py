import random


def basic_facts_quiz():
    question_number = 0

    difficulty_level = int_check("What level of difficulty would you like your questions?? (Choose from levels 1-5): ",
                                 low=1, high=5)

    # loops while question_num is lower than amount of questions - chosen at the start
    while question_number < number_questions:

        print()
        print(f"Question {question_number + 1}:")

        # Generates the numbers for the question and difficulty
        if difficulty_level == 1:
            num_1 = random.randint(1, 20)
            num_2 = random.randint(1, 20)
        elif difficulty_level == 2:
            num_1 = random.randint(1, 40)
            num_2 = random.randint(1, 40)
        elif difficulty_level == 3:
            num_1 = random.randint(1, 60)
            num_2 = random.randint(1, 60)
        elif difficulty_level == 4:
            num_1 = random.randint(1, 70)
            num_2 = random.randint(1, 70)
        else:
            num_1 = random.randint(1, 80)
            num_2 = random.randint(1, 80)
