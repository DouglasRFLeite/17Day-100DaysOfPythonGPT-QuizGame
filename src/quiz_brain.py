from question_model import Question

class QuizBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q{self.question_number}: {question.text} (True/False): ")
        return answer
    
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, answer) -> bool:
        question = self.question_list[self.question_number - 1] #last question
        if question.answer.lower() == answer.lower():
            self.score += 1
            print("You got it right!")
            return True

        print(f"That's wrong. The correct answer was: {question.answer}")
        return False
    
    def get_score(self) -> int:
        return f"{self.score}/{self.question_number}"

    def print_score(self) -> None:
        print(f"Your current score is: {self.get_score()}")

    def print_final_score(self) -> None:
        print(f"Your final score is: {self.get_score()}")