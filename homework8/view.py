def get_op():
    op = int(input("1 - импорт\n2 - экспорт\n3 - показать всех\n4 - выход\n"))
    return op

def get_data():
    name = input("имя ")
    surname = input("фамилия ")
    telephone = input("телефон ")
    data_str = name + " " + surname + " " + telephone + "\n"
    return data_str

def find_person():
    data_str = input("введи параметр ")
    return data_str

def get_oper():
    opa = int(input("1 - изменение\n2 - удаление\n3 - выход\n"))
    return opa

def get_num_str():
    num_str = int(input("Введите номер строки "))
    return num_str