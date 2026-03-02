"""
Keanrich 232301226 IBDA Project UAS
Pemrograman Berorientasi Object
"""
#  iterator design pattern
class ListIterator:
    def __init__(self,data : list):
        self.data = [i for i in data]
        self.index = 0

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration()
        
        word = self.data[self.index]
        self.index += 1
        return word


class ListIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return ListIterator(self.data)
    


