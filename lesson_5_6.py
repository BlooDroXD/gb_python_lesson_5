# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import re

_file = open('subject.txt', 'r')
subj_dict = {}
for line in _file.readlines():
    nums = re.findall(r'\d+', line)
    nums = [int(i) for i in nums]
    subj_dict[f"{line.split(':')[0]}"] = sum(nums)

print(subj_dict)
_file.close()