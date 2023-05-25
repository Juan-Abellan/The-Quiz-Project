# TODO: IMPORTS
from data import question_data
from question_model import Question
from random import choice
from quiz_brain import QuizBrain

# TODO: INITIAL CONDITIONS
still_playing = True

# TODO: DEVELOPMENT

question_bank = [Question(text=question["text"], answer=question["answer"]) for question in question_data]
random_question = choice(question_bank)
quiz_brain = QuizBrain(question_list=question_bank)

while still_playing:
    if quiz_brain.still_has_questions(questions_bank_length=len(question_bank)):
        quiz_brain.next_question()
        print("\n")
    else:
        still_playing = False

print(f"You have finished the quiz!\nYour final score is: {quiz_brain.score} / {len(question_bank)}")

# print(f"""
# TESTING DATA AND QUESTION DATA
# {question_data = }
# {type(question_data) = }
# ---
# {question_data[0] = }
# {type(question_data[0])= }
# """)

# print(f"""
# TESTING QUESTION MODEL AND QUIZ BRAIN
# {question_bank = }
# {random_question = }
# {quiz_brain.next_question() = }
# {quiz_brain.still_has_questions(questions_bank_length=len(question_bank)) = }
# """)
#
