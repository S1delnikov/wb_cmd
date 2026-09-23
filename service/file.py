
def check_file_type(outfile):
    if '.' not in outfile:
        print('Не указан формат файла! Доступные форматы: .txt, .xlsx')
        return False
    type_of_file = outfile.split('.')[-1]
    if type_of_file == 'txt' or type_of_file == 'xlsx':
        return type_of_file
    else:
        print(f'Вводимый формат файла ({type_of_file}) не поддерживается! Доступные форматы: .txt, .xlsx')
        return False