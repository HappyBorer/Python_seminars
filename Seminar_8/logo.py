from datetime import datetime

def log(data, mode):
    with open('log.txt', 'a', encoding='utf-8', newline='') as file:
        if mode == 1:
            file.write(f'import - {data} : {datetime.now()}' + '\n')
        elif mode == 2:
            file.write(f'export - {data} : {datetime.now()}' + '\n')
        else:
            file.write(f'delete - {data} : {datetime.now()}' + '\n')
