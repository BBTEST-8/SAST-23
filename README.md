# BBTEST-8: A Black-Box Test Suite Minimization History-Based Applied To An Industrial Case

## Description
This Python script processes a dataset containing information about Test Cases, Test Case Executions, and associated Bug Reports. It filters the data to extract specific entries that meet certain criteria and prints the Test Case Keys to be reduced from the test suite. 

This repository is a complementary page for the following publication:

> TBD


## Requirements
- Python 3.x
- pandas library

## How to Use
1. Ensure you have Python 3.x installed on your system.
2. Install the required pandas library by executing the following command:
pip install pandas
3. Place the dataset file named `dataset.csv` in the `input` directory. Make sure the dataset contains columns `test_execution_key`, `test_case_key`, `bugreport_key`, along with the `test_case_creation_date` and `test_execution_date` columns as US date format type.
4. Run the script `main.py`.
5. The script will display a list of Test Case Keys to be reduced from the test suite.

## Script Execution Flow
1. The script calculates the date two years ago from the current date and converts it to the US date format (`'%Y-%m-%d'`).
2. It reads the dataset `dataset.csv` and creates a pandas DataFrame, applying the data types specified for the columns `test_execution_key`, `test_case_key`, and `bugreport_key`, and parsing the columns `test_case_creation_date` and `test_execution_date` as dates.
3. The DataFrame is filtered to keep only the Test Cases created at least two years ago and executed within the last two years.
4. It then filters the dataset to keep only the Test Cases that have been executed at least forty times.
5. Finally, the script prints the list of Test Case Keys that meet these criteria.

## Note
- Ensure the `dataset.csv` file is properly formatted with the required columns and data before running the script.
- Please insert only `bugreport_key` that resulted in a bugfix or code change, because the script assumes all the `bugreport_key` present in this dataset resulted in a code change/bugfix.