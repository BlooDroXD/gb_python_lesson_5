# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

file = open('text_1.txt', 'r')
print(f'\nFile content:\n{file.read()}\n')
count_lines = 0
file.seek(0, 0)
words = 0
for line in file.readlines():
    count_lines += 1
    words += len(line.split(" "))
    line.replace('\n','')
    print(f'In {count_lines} line {len(line.split(" "))} words')
print(f'\nIn text :\n{"-" * 20}\n'
      f'{(str(count_lines)+ " lines").center(20) } \n{"-" * 20}\n'
      f'{(str(words) + " words").center(20)}')
file.close()


