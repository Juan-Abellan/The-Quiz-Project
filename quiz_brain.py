class QuizBrain:
    """
    Contains the game´s flow.
    """

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        """
        Enunciates the question and returns the user´s answer.
        """
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True or False)?: ").lower()
        self.check_answer(user_answer=user_answer, solution=question.answer)

    def still_has_questions(self, questions_bank_length):
        """
        Evaluates if are still questions to be made.
        """
        return questions_bank_length >= self.question_number + 1

    def check_answer(self, user_answer, solution):
        if user_answer.lower() == solution.lower():
            self.score += 1
        else:
            print("That was wrong!")

        print(f"The correct answer is: {solution}")
        print(f"your current score is {self.score}/{self.question_number}")
