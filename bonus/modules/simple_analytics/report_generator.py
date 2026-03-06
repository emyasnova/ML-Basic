"""
Module: report_generator.py
Method: generate_report
Description: This module provides a function to generate a report based on the provided data.
"""

from types import List, Union

def generate_report(numbers: List[Union[int, float]], title: str) -> None:
    """
    Generates a report based on the provided data.
    Args:
        numbers (List[Union[int, float]]): A list of numbers to include in the report.
        title (str): The title of the report.
    Returns:
        None: This function prints the report to the console.
    """
    print(f"{title}\n{numbers}")
