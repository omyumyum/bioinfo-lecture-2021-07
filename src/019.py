import sys

try:
    with open('noname.txt', 'r') as handle:
        data = fr.readlines()
except FileNotFoundError as err:
    print('파일이 없음')
    sys.exit()

print(data)

