"""
Module: data_loader.py
Method: load_from_text, load_from_csv
Description: This module provides functions to load data from various sources such as text files and CSV files.
"""

def load_from_text(file_path: str) -> list:
    """
    Loads data from a text file and returns it as a list of lines.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def load_from_csv(file_path: str) -> list:
    """
    Loads data from a CSV file and returns it as a list of rows.
    """
    import csv
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data
