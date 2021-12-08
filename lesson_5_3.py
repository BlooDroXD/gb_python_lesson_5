# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
#
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

info_personal = open('personal.txt', 'r')
salary = 0
for line in info_personal.readlines():
    line.replace('\n', '')
    line = line.split(' ')
    salary += float(line[1])
    if float(line[1]) < 20000:
        print(f'{line[0]} имееет оклад менее 20000')
info_personal.seek(0, 0)
print('\nСредний оклад = %7.2f ' % float(salary / len(info_personal.readlines())))




info_personal.close()