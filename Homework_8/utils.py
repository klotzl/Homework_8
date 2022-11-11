import json

from question8 import Question


def load_questions(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)

    questions = []
    for item in data:
        text = item['q']
        difficulty = item['d']
        right_answer = item['a']
        question = Question(text, difficulty, right_answer)
        questions.append(question)

    return questions


def build_statistics(questions):

    user_score = 0
    count = 0

    for question8 in questions:
        '''После того, как все вопросы заданы, выводится статистика на основе списка questions'''
        if question8.is_correct():
            user_score = user_score + question8.score
            count += 1

    return f'Вот и всё!\nОтвечено {count} вопроса из 5\nНабрано {user_score} баллов'
