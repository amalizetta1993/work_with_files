
with open(r'test.txt', 'wt', encoding = 'utf-8') as file1:
    file1.write('''Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом.''')


with open(r'test.txt', 'rt', encoding = 'utf-8') as file1:
    for line in file1:
        print(line.strip())