class Question:
    '''класс Question для вопроса'''

    def __init__(self, text, difficulty, right_answer):
        '''текст вопроса, сложность вопроса, верный вариант ответа, задан ли вопрос(по умолчанию False), ответ пользователя(поумолчанию None), баллы за вопрос(вычисляется вмоментинициализации)'''
        self.text = text
        self.difficulty = difficulty
        self.right_answer = right_answer

        self.is_asked = False
        self.user_answer = None
        self.score = int(self.difficulty)

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов."""
        return self.score

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False."""
        return self.right_answer == self.user_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5"""
        return f'Вопрос: {self.text}\nСложность: {self.difficulty}/5'

    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов;
        Возвращает :
        Ответ неверный, верный ответ __"""
        if self.is_correct():
            '''...программа записывает полученные ответ в соответствующий экземпляр класса Question, а  еще комментирует этот ответ.'''
            return f'Ответ верный, получено {self.score} баллов\n'
        return f'Ответ неверный. Верный ответ – {self.right_answer}\n'


