""" 
FileCloud class for managing files in cloud storage. 
This class inherits from the File class and provides methods for uploading, downloading, deleting, and reading files in cloud storage.
"""

from file import File

class FileCloud(File):
    def __init__(self, name, size, creation_date, owner, cloud_provider):
        super().__init__(name, size, creation_date, owner)
        self.cloud_provider = cloud_provider

    def upload(self):
        print(f"Uploading {self.name} to {self.cloud_provider} cloud storage.")

    def download(self):
        print(f"Downloading {self.name} from {self.cloud_provider} cloud storage.")

    def delete(self):
        print(f"Deleting {self.name} from {self.cloud_provider} cloud storage.")

    def read(self):
        print(f"Reading {self.name} from {self.cloud_provider} cloud storage.")
