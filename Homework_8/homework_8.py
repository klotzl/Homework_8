import random

from utils import load_questions, build_statistics

print("Игра начинается!\n")

if __name__ == '__main__':
    filename = 'questions.json'
    questions = load_questions(filename)
    '''Приложение в случайном порядке и по очереди задает все вопросы'''
    random.shuffle(questions)

    for question in questions:
        print(question.build_question())
        user_answer = input("Ваш ответ: ")
        '''После ответа пользователя...'''
        question.user_answer = user_answer
        print(question.build_feedback())

    print('')
    print(build_statistics(questions))
