# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

eng_to_rus_dict = dict({'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'})
_file = open('text_2.txt', 'r')
_file_out = open('text_out.txt', 'w')
for line in _file.readlines():
    line = line.split(' ')
    print(line)
    if line[0] in eng_to_rus_dict:
        line[0] = eng_to_rus_dict.get(line[0])
        _file_out.writelines(' '.join(line))

_file_out.close()
_file.close()