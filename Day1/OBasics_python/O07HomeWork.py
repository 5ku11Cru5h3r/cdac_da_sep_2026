'''
Develop a context manager
1. context manager work with "with" statements
'''
import sqlite3


class CA:
    def __init__(self, db):
        self.db = db
        self.connection = None
        # self.cursor = None
        # print("self", id(self))

    def fun(self):
        print("fun")

    def __enter__(self):
        print("Entered the function")
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        return self.cursor()
    def __exit__(self, exc_type, exc, tb):
        print("Exit")

# obj = CA()
# print(id(obj))


obj1 = CA()
with obj1:
    obj1.fun()
    # print(id(obj1))
