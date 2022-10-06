
def exp(request, path='data.txt'):
    with open(path, 'r', encoding='UTF8') as file:
        new_list = file.read()
    list = new_list.split('\n')
    new_list = [i.split(', ') for i in list if len(i) > 0]
    for person in new_list:
        for item in person:
            if item.startswith(request):
                print(' '.join(person))
    return request