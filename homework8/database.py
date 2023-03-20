def add_data(data_str):
    with open("homework8/file.txt", "a", encoding="UTF-8") as f:
        f.write(data_str)

def find_person(data_str):
    with open("homework8/file.txt", "r", encoding="UTF-8") as f:
        lst_str = f.readlines()
        count = 0
        for worker in lst_str:
            count += 1
            if data_str in worker:
                print(f"{count} {worker}")

def del_person(i):
    with open("homework8/file.txt", "r+", encoding="UTF-8") as f:
        lst_str = f.readlines()
        lst_str.pop(i-1)
        f.truncate(0)
        f.seek(0)
        f.writelines(lst_str)
        
def chan_person(data_str, i):
    with open("homework8/file.txt", "r+", encoding="UTF-8") as f:
        lst_str = f.readlines()
        lst_str[i-1] = data_str
        f.truncate(0)
        f.seek(0)
        f.writelines(lst_str)

def all_lst():
    with open("homework8/file.txt", "r", encoding="UTF-8") as f:
        lst_str = f.readlines()
        count = 0
        for worker in lst_str:
            count += 1
            print(f"{count} {worker}")