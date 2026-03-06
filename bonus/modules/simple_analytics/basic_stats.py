"""
Module: basic_stats.py
Method: calculate_basic_stats, find_outliers
Description: This module provides functions to calculate basic statistics such as mean, median, and mode for a list of numbers.
"""

from typing import List, Union, Dict

def calculate_basic_stats(numbers: List[Union[int, float]]) -> Dict:
    """
    Calculates basic statistics (mean, median, mode) for a list of numbers.
    Args:        numbers (List[Union[int, float]]): A list of numbers to calculate statistics for.
    Returns:     Dict: A dictionary containing the calculated statistics.
    """
    mean = sum(numbers) / len(numbers) if numbers else 0
    count = len(numbers)
    min_value = min(numbers) if numbers else 0
    max_value = max(numbers) if numbers else 0
    sum_value = sum(numbers) if numbers else 0

    return {
        "mean": mean,
        "count": count,
        "min": min_value,
        "max": max_value,
        "sum": sum_value
    }

def find_outliers(numbers: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Identifies outliers in a list of numbers using the IQR method.
    Args:        numbers (List[Union[int, float]]): A list of numbers to check for outliers.
    Returns:     List[Union[int, float]]: A list of outliers found in the input list.
    """
    if not numbers:
        return []

    sorted_numbers = sorted(numbers)
    q1 = sorted_numbers[len(sorted_numbers) // 4]
    q3 = sorted_numbers[(len(sorted_numbers) * 3) // 4]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = [num for num in numbers if num < lower_bound or num > upper_bound]
    
    return outliers

if __name__ == "__main__":
    sample_numbers = [10, 12, 12, 150, 13, 12, 11, 10, 14, 13, 100]
    stats = calculate_basic_stats(sample_numbers)
    outliers = find_outliers(sample_numbers)

    print("Basic Statistics:", stats)
    print("Outliers:", outliers)