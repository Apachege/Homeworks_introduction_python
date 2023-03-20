import view
import database

def main():
    while True:
        op = view.get_op()
        if op == 1:
            data_worker = view.get_data()
            database.add_data(data_worker)
        if op == 2:
            find_str = view.find_person()
            database.find_person(find_str)
            oper = view.get_oper()
            if oper == 1:
                num_str = view.get_num_str()
                data_worker = view.get_data()
                database.chan_person(data_worker, num_str)
            if oper == 2:
                num_str = view.get_num_str()
                database.del_person(num_str)
            if oper == 3:
                break
        if op == 3:
                database.all_lst()
        if op == 4:
            break