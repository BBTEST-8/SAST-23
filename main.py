from datetime import datetime, timedelta

import os
import pandas as pd


def main():
    try:
        # Get actual datetime format and subtracts 2 years from it.
        two_years_ago_datetime = datetime.now() - timedelta(days=365 * 2)

        # Converts the datetime type to US date format string type.
        two_years_ago_date = two_years_ago_datetime.strftime('%Y-%m-%d')

        # Creating the base dataframe containing the entries related to the Test Cases, Test Case Executions, and its
        # Bugreports.
        dtypes = {'test_execution_key': 'str', 'test_case_key': 'str', 'bugreport_key': 'str',
                  'bugreport_resolution': 'str'}
        parse_dates = ['test_case_creation_date', 'test_execution_date']
        df = pd.read_csv('input/dataset.csv', dtype=dtypes, parse_dates=parse_dates)

        # Filtering the dataframe by the test cases created at least 2 years ago.
        df = df.loc[df['test_case_creation_date'] < two_years_ago_date]

        # Filtering the dataframe by the test cases executed in the last 2 years.
        df = df.loc[df['test_execution_date'] >= pd.Timestamp(two_years_ago_date)]

        # Filtering the dataset by the test cases that has been executed at least forty times
        df_grouped = df.drop_duplicates(subset=['test_execution_key']).groupby(by='test_case_key')

        tcs_40_execs = []
        for name, group in df_grouped:
            if len(list(group['test_execution_date'])) >= 40:
                tcs_40_execs.append(name)

        df = df[df['test_case_key'].isin(tcs_40_execs)]

        test_case_list = df.drop_duplicates(subset=['test_case_key'])['test_case_key'].to_list()

        # Save the result in the 'output/' folder as a text file with the name containing date and time of generation
        output_path = 'output/'
        os.makedirs(output_path, exist_ok=True)
        current_datetime = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(output_path, f'test_case_list_result_{current_datetime}.txt')

        with open(output_file, 'w') as f:
            for item in test_case_list:
                f.write("%s\n" % item)

        print(f'Test case list below saved to output/test_case_list_result_{current_datetime}.txt:\n{test_case_list}')
    except FileNotFoundError as e:
        print("Error: The input file 'dataset.csv' was not found.")
    except PermissionError as e:
        print("Error: Permission denied. You do not have the required permissions to access the file.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))


if __name__ == '__main__':
    main()
