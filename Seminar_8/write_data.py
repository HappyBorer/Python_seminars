
def imp(data, path='data.txt'):
    with open(path, 'a', encoding='utf8', newline='') as file:
        file.write(data + '\n')
    print('The recording was successful!')
    return data