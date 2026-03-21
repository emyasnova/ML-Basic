"""
File class with methods to create, update, read and delete a file.
"""

import os

class File():
    def __init__(self, name, size, creation_date, owner):
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner
        self.create()

    def create(self):
        open(self.name, 'w').close()

    def update(self, name, size, creation_date, owner):
        os.rename(self.name, name)
        self.name = name
        self.size = size
        self.creation_date = creation_date
        self.owner = owner

    def read(self):
        with open(self.name, 'r') as file:
            return file.read()

    def delete(self):
        os.remove(self.name)
