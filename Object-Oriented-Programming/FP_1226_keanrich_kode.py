"""
Keanrich Cordana 232301226 IBDA project UAS
Pemrograman Berorientasi Object
"""
from abc import ABC, abstractmethod
from iterator_design import ListIterable
class people(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def get_biodata(self):
        pass

    def get_jkt48_data(self):
        pass

class member(people):
    def __init__ (self, name: str) -> None:
        self.__name = name
        self.biodata = {}
        self.jkt48_data = {}

    def get_name(self):
        return self.__name
        
class Biodata(member):
    def __init__(self, name, date:str,place: str, tall:int, hobby: str):
        super().__init__(name)
        self.biodata[name] = [date, place, tall, hobby]

    def get_biodata(self, nama) -> list:
        return self.biodata[nama]
    
    def set_biodata(self, name, new_biodata: list) :
        self.biodata[name] = new_biodata

    def read_data(self, target):
        print(f"name: {target}")
        print(f"birthday place and date: {self.biodata[target][1]}, {self.biodata[target][0]}")
        print(f"height: {self.biodata[target][2]}")
        print(f"hobby: {self.biodata[target][3]}")

    def delete_data(self, target):
        self.biodata[target] = []
    
class jkt48_data(member):
    def __init__(self, name, position: str, year:int, status: str, jiko: str, generation: int):
        super().__init__(name)
        self.jkt48_data[name] = [position, year, status, jiko, generation] 

    def get_jkt48_data(self, nama) -> list:
        return self.jkt48_data[nama]

    def set_jkt48_data(self, name, new_data):
        self.jkt48_data[name] = new_data

    def read_data(self, target):
        print(f"position: {self.jkt48_data[target][0]}")
        print(f"join in {self.jkt48_data[target][1]}")
        print(f"with status:{self.jkt48_data[target][2]}")
        print(f"jikoshoukai: {self.jkt48_data[target][3]}")
        print(f"generation: {self.jkt48_data[target][4]}")

    def delete_data(self, target):
        self.jkt48_data[target] = []

def read_file (file):
    try:
        f = open(file, "r")
        list_data = []
        for line in f:
            line = line.strip()
            line = line.split(",")
            list_data.append(line)
        f.close()
        return list_data
    except Exception as e:
        raise FileNotFoundError


def write_dict_to_txt(data_dict, file_path):
    try:
        with open(file_path, 'w') as file:

            for key, value in data_dict.items():
                file.write(f"{key},")

                for private_data in value[0].get_biodata(key):
                    file.write(f"{private_data},")

                for public_data in value[1].get_jkt48_data(key):
                    file.write(f"{public_data},")

                file.write("\n")
        print(f"Data berhasil ditulis ke {file_path}")
    except Exception as e:
        raise e

class strategy(ABC):
    @abstractmethod
    def execute(self, dict_o, file1):
        pass

class ConcreteStrategyCreate(strategy):
    def execute(self,dict_o, file1):
        while True:
            input_new_name = input("input new member name:")
            input_date_place_birthday = input("input new member dbp (place,xx-xx-xxxx):").split(",")
            input_height = input("input new member height:")
            input_hobby = input("input new member hobby:")
            private_d = Biodata(input_new_name, input_date_place_birthday[1], 
                                input_date_place_birthday[0], 
                                input_height, input_hobby)
            
            input_member_position = input("input new member position:")
            input_year_enterance = input("input new member enterance year:")
            input_status = input("input new member status:")
            input_jiko = input("input new member jikoshoukai:")
            input_generation = input("input new member generation:")
            jkt48_d = jkt48_data(input_new_name, input_member_position, input_year_enterance, 
                                input_status, input_jiko, input_generation)
            dict_o[input_new_name] = [private_d, jkt48_d]

            print("new member added")
            input_next = input("do you want to continue add? (y/n):")
            if input_next == "n":
                write_dict_to_txt(dict_o, file1)
                return

class ConcreteStrategyRead(strategy):
    def execute(self, dict_o, file1):
        while True:
            for index, name in enumerate(dict_o):
                print(f"{index + 1}. {name}")
                dict_data_member = dict_o[name][0].get_biodata(name)
                list_data = dict_data_member

                iterable = ListIterable(list_data)
                iterator = iter(iterable)
                while True:
                    try:
                        print(next(iterator))
                    except StopIteration:
                        break
                print()

            input_next = input("do you want to see detail of member (y/n):")
            if input_next == "y":
                input_name = input("which member do you want to see:")
                dict_o[input_name][0].read_data(input_name)
                dict_o[input_name][1].read_data(input_name)
                input_step = input("do you want to see another member?(y/n):")
                if input_step == "n":
                    return dict_o
            else:
                return dict_o

class ConcreteStrategyUpdate(strategy):
    def execute(self,dict_o, file1):
        while True:
            for index, name in enumerate(dict_o):
                print(f"{index + 1}. {name}")
                dict_data_member = dict_o[name][0].get_biodata(name)
                list_data = dict_data_member

                iterable = ListIterable(list_data)
                iterator = iter(iterable)
                while True:
                    try:
                        print(next(iterator))
                    except StopIteration:
                        break
                print()
            print("1. update personal data")
            print("2. update jkt48 data")
            print("3. exit")

            input_name = input("which MEMBER do you want to update?")
            input_next = input("What do you want to update?(1/2)")
            if input_next == "1":
                print("1. update dbp")
                print("2. update height")
                print("3. update hobby")
                input_option = input("which data do you want to update?(1-3)")
                list_old = dict_o[input_name][0].get_biodata(input_name)
                if input_option == "1":
                    new_dbp = input("insert new dbp (place,xx/xx/xxxx):").split(",")
                    list_old[0] = new_dbp[1]
                    list_old[1] = new_dbp[0]
                    dict_o[input_name][0].set_biodata(input_name, list_old)

                elif  input_option == "2":
                    new_height = input("insert new height:")
                    list_old[2] = new_height
                    dict_o[input_name][0].set_biodata(input_name, list_old)

                elif  input_option == "3":
                    new_hobby = input("insert new hobby:")
                    list_old[3] = new_hobby
                    dict_o[input_name][0].set_biodata(input_name, list_old)

            elif input_next == "2":
                print("1. update position")
                print("2. update year")
                print("3. update status")
                print("4. update jiko")
                print("5. update generation")
                input_option = input("which data do you want to update?(1-5)")
                list_old = dict_o[input_name][1].get_jkt48_data(input_name)
                if  input_option == "1":
                    new_position = input("insert new position:")
                    list_old[0] = new_position
                    dict_o[input_name][1].set_jkt48_data(input_name, list_old)
                
                elif input_option == "2":
                    new_year = input("insert new year enterance:")
                    list_old[1] = new_year
                    dict_o[input_name][1].set_jkt48_data(input_name, list_old)

                elif  input_option == "3":
                    new_status = input("insert new status:")
                    list_old[2] = new_status
                    dict_o[input_name][1].set_jkt48_data(input_name, list_old)

                elif  input_option == "4":
                    new_jiko = input("insert new jiko:")
                    list_old[3] = new_jiko
                    dict_o[input_name][1].set_jkt48_data(input_name, list_old)

                elif input_option == "5":
                    new_gen = input("insert new gen:")
                    list_old[4] = new_gen
                    dict_o[input_name][1].set_jkt48_data(input_name, list_old)

            else:
                write_dict_to_txt(dict_o, file1)
                return

            input_step = input("do you want to continue update? (y/n)")
            if input_step == "n":
                write_dict_to_txt(dict_o, file1)
                return


class ConcreteStrategyDelete(strategy):
    def execute(self,dict_o,file1):
        while True:
            input_name = input("insert name you want to delete:")
            dict_o[input_name][0].delete_data(input_name)
            dict_o[input_name][1].delete_data(input_name)
            del dict_o[input_name]

            input_next = input("do you want to contiue delete? (y/n)")
            if input_next == "n":
                write_dict_to_txt(dict_o, file1)
                return

class context:
    def __init__ (self, strategy: strategy):
        self.strategy = strategy

    def set_strategy (self, strategy: strategy):
        self.strategy = strategy

    def execute_strategy (self, dict_o, file):
        return self.strategy.execute(dict_o, file)
    

class Application:
    @abstractmethod
    def menu_program ():
        file = "data_member_jkt48.txt"
        list_data_per_member = read_file(file)
        dict_of_object = {}

        for data_member in list_data_per_member:
            private_data = Biodata(data_member[0], data_member[1], data_member[2], data_member[3], data_member[4])
            personal_jk48_data = jkt48_data(data_member[0], data_member[5], data_member[6], data_member[7], 
                                            data_member[8], data_member[9])
            dict_of_object[data_member[0]] = [private_data, personal_jk48_data]
        
        contex = context(None)
        while True:
            print("1. Create")
            print("2. Read")
            print("3. Update")
            print("4. Delete")
            print("5. Exit")
            input_option = input("what option do you want (1-5):")
            if input_option == "1":
                contex.set_strategy(ConcreteStrategyCreate())

            elif input_option == "2":
                contex.set_strategy(ConcreteStrategyRead())

            elif input_option == "3":
                contex.set_strategy(ConcreteStrategyUpdate())

            elif input_option == "4":
                contex.set_strategy(ConcreteStrategyDelete())

            elif input_option == "5":
                print("gudbay")
                return


            contex.execute_strategy(dict_of_object, file)
            
        
if __name__ == "__main__":
    Application.menu_program()