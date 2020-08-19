import random
class Hangman:

    def __init__(self):
        self.mistakes = int(input('Введите допустимое количество ошибок: '))
        with open('original.txt', 'rb') as f:
            k = f.read().decode('utf-8')
            self.word = random.choice(k.split('\n'))
        self.answer = []
        for i in range(len(self.word) - 1):
            i = '_'
            self.answer.append(i)

    def attempt(self):
        self.letter = input('Ваша буква: ')
        for k, v in game_dict.items():
            if v == self.letter:
                self.answer[k] = self.letter
        if not self.answer.count(self.letter):
            self.mistakes -= 1
        return f'Откройте букву {self.letter}!\n{self.answer}\n' \
               f'Осталось {self.mistakes} попыт(-ок/-ки)\n' \
                #f'(Подсказка: {self.word[0:-1:]})'

    def open_words(self):
        self.all_word = input('Итак! Ваше слово: ')
        if list(self.all_word) == list(self.word[0:-1:]):
            return True
        else:
            self.mistakes -= 1
            return False

    def current_inputs(self):
        return f'Перед Вами игровое табло: \n' \
               f'{self.answer}\n' \
               f'Осталось {self.mistakes} попыт(-ок/-ки)\n'

    def is_end(self):
        if self.answer == list(self.word[0:-1:]):
            print(f'Поздравляем! Вы разгадали слово: {self.word}')
            return False
        elif self.mistakes == 0:
            print('Вы проиграли!')
            return False
        else:
            return True

print('Добропожаловать в игру "Висилеца"!\n\n')
s = Hangman()
game_dict = dict.fromkeys(range(len(s.word)-1))
for key in game_dict.keys():
    game_dict[key] = s.word[0+key:(1+key):]
while s.is_end() != False:
    action = input('Выберите действие: \n'
                   '(1): Назовите букву\n'
                   '(2): Посмотреть табло\n'
                   '(3): Назвать слово целиком\n'
                   '(4): Выход')
    if action == '1':
        print(s.attempt())
    elif action == '2':
        print(s.current_inputs())
    elif action == '3':
        if s.open_words() == s.is_end():
            print(f'Поздравляем! Вы разгадали слово: {s.word}')
            break
        else:
            print('Вы ошиблись! Попробуйте еще раз')
            pass
    elif action == '4':
        print('До скорой встречи!')
        break
else:
    print(f'Игра окончена!\nСлово {s.word}')














