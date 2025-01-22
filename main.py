import os

path_to_project = r"E:\study\Python\homework_6\work_with_files"

#нормализованный абсолютный путь к файлу test_file_1.txt
path_to_project_1 = r"E:/study/Python/homework_6/work_with_files"
print(os.path.normpath(path_to_project))

#содержимое папки проекта
for path, dirnames, filenames in os.walk(path_to_project):
    print(f'path - {path}')
    print(f'dirnames - {dirnames}')
    print(f'filenames - {filenames}')
    
    
#нормализованный абсолютный путь к файлу test_file_3.txt

disk = 'E:\\'
dir1 = 'study'
dir2 = 'Python'
dir3 = 'homework_6'
dir4 = 'work_with_files'
dir5 = 'data_path_2'

print(os.path.join(disk, dir1, dir2, dir3, dir4, dir5))

#код для создания и для удаления папки внутри папки data_path_2
#создание папки
base_dir = '.'
test_dir = 'data_path_2'
new_dir = r'my_new_dir'
path_new_dir = os.path.join(base_dir, test_dir, new_dir)
try:
    os.mkdir(path_new_dir)
except FileExistsError:
    print('Такая папка уже есть')
#удаление папки
os.rmdir(path_new_dir)