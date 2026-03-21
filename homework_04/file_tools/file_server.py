""" 
FileServer class for managing files on a server.
This class inherits from the File class and provides methods for uploading, downloading, deleting, and reading files on a server.
"""

from file import File

class FileServer(File):
    def __init__(self, name, size, creation_date, owner, server_location):
        super().__init__(name, size, creation_date, owner)
        self.server_location = server_location

    def upload(self):
        print(f"Uploading {self.name} to {self.server_location} server.")

    def download(self):
        print(f"Downloading {self.name} from {self.server_location} server.")

    def delete(self):
        print(f"Deleting {self.name} from {self.server_location} server.")

    def read(self):
        print(f"Reading {self.name} from {self.server_location} server.")
