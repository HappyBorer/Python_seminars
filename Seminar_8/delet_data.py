def delet(data, path='data.txt'):
    choice = input('Delete data?(Y/N): ')
    if choice.upper() == 'Y':
        try:
            with open(path, 'r', encoding='utf-8') as file:
                string = file.read().split('\n')
            list = []
            for line in string:
                if data not in line:
                    list.append(line)
            if len(list) != len(string):
                with open(path, 'w', newline='', encoding='utf-8') as file:
                    for line in list:
                        file.write(line + '\n')
        except:
            print('File not found!')
    return data
