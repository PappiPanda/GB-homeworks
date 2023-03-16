'''
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
'''



def count_words(string):
    return len(string.split())

def count_lines(file):
    file.seek(0, 0)
    return len(file.readlines())

with open('excercise_2.txt', 'r') as f:
    for i, line in enumerate(f.readlines(), 1):
        print(f'words in {i} line: {count_words(line)}')
    print(f'number of lines: {count_lines(f)}')