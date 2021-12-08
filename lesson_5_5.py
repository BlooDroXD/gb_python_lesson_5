#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

my_f = open('test.txt', 'w')
string = []
for i in range(10):
    string.append(str(i))
my_f.writelines(' '.join(string))
my_f.close()

my_f = open('test.txt', 'r')
summ = 0
num = my_f.readline()
print(num)
num = num.split(' ')
for i in range(len(num)):
    summ += int(num[i])
print('Сумма = %i' % summ)
