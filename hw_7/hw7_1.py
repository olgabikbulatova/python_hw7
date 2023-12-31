# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#пара-ра-рам рам-пам-папам па-ра-па-да


def rythm(x):
    x = x.split()
    vowel = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е', 'a', 'e', 'i', 'o', 'u', 'y']
    lst = []
    for word in x:
        count = 0
        for letter in word:
            if letter in vowel:
                count += 1
        lst.append(count)
    if max(lst) == min(lst):
        return 'Парам пам-пам'
    else:
        return 'Пам парам'


a = 'пара-ра-рам рам-пам-папам па-ра-па-да'
print(rythm(a))