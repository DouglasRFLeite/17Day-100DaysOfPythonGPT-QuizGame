from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q["question"], q["correct_answer"]) for q in question_data]

brain = QuizBrain(question_bank)

while brain.still_has_questions():
    answer = brain.next_question()
    brain.check_answer(answer)
    brain.print_score()
    print()

print("You've completed the Quiz!")
brain.print_final_score() 