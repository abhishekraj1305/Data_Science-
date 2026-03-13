import os

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(dir_path, 'input.txt')

contents = os.listdir(dir_path)
print(contents)