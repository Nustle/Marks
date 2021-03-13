from time import sleep
import helpers as h

print("Здравствуйте, это робот Адиль :)")
sleep(2)
print("Я предоставляю различные опции по обработке данных об учениках")
sleep(3)
print("Опция 1: вывод оценок определённого ученика")
print("Опция 2: вывод среднего бала определённого ученика")
print("Опция 3: вывод среднего бала по предметам")
print("Опция 4: вывод кол-ва выбранной вами оценки по предметам")
sleep(5)

while True:
    option = int(input("Какую опцию хотите выбрать: "))
    if (option >= 1 and option <= 4):
        break

if (option == 1 or option == 2):
    while True:
        idf = int(input("Введите id ученика: "))
        if h.isset(idf, h.get_id()):
            break

    print("Отлично, ученик {} найден!".format(idf))
    sleep(1)

    if option == 1:
        print("Оценка ученика {} по математике: {}".format(idf, h.get_marks(idf)[0]))
        print("Оценка ученика {} по физике: {}".format(idf, h.get_marks(idf)[1]))
        print("Оценка ученика {} по информатике: {}".format(idf, h.get_marks(idf)[2]))
    elif option == 2:
        print("Средний бал ученика {}: {}".format(idf, h.mean_pupil(idf)))

elif option == 4:
    while True:
        mark = int(input("Введите интересующую вас оценку: "))
        
        if h.isset(mark, h.all_marks()):
            break
    
    print("Оценка {} найдена!".format(mark))
    sleep(1)

    print("Кол-во {} по математике: {}".format(mark, h.count_marks(mark)[0]))
    print("Кол-во {} по физике: {}".format(mark, h.count_marks(mark)[1]))
    print("Кол-во {} по информатике: {}".format(mark, h.count_marks(mark)[2]))

else:
    print("Средний бал по математике: {}".format(h.mean_subjects()[0]))
    print("Средний бал по физике: {}".format(h.mean_subjects()[1]))
    print("Средний бал по информатике: {}".format(h.mean_subjects()[2]))
