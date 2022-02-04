import os

FILES = ['1.txt', '2.txt', '3.txt']
FILE_TO_WRITE = 'result.txt'


def get_file_name(files):
    temp_list = []
    for i in files:
        temp_list.append(os.path.basename(i))
    return temp_list


def get_file_content(files):
    temp_list = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            temp_list.append(f.read())
    return temp_list


def inspect_len(files):
    temp_list = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            temp_list.append(len(f.readlines()))
    return temp_list


def sort_by_len(files):
    items = zip(inspect_len(files), get_file_name(files), get_file_content(files))
    now_sorted = (sorted(items))
    return now_sorted


def write_result(file):
    with open(FILE_TO_WRITE, 'w', encoding='utf-8') as f:
        item = sort_by_len(file)
        for i in item:
            f.write(f'Имя файла - {i[1]}\n')
            f.write(f'Количество строк в файле - {i[0]}\n')
            f.write(f'{i[2]}\n')
        return


write_result(FILES)
