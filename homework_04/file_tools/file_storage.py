""" 
FileStorage class for managing files in storage.
This class inherits from the File class and provides methods for uploading, downloading, deleting, and reading files in storage.
"""

from file import File

class FileStorage(File):
    def __init__(self, name, size, creation_date, owner, storage_location):
        super().__init__(name, size, creation_date, owner)
        self.storage_location = storage_location

    def upload(self):
        print(f"Uploading {self.name} to {self.storage_location} storage.")

    def download(self):
        print(f"Downloading {self.name} from {self.storage_location} storage.")

    def delete(self):
        print(f"Deleting {self.name} from {self.storage_location} storage.")

    def read(self):
        print(f"Reading {self.name} from {self.storage_location} storage.")
