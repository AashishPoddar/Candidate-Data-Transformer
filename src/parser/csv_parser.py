import pandas as pd


class CSVParser:
    """
    Reads recruiter CSV files and converts them
    into a list of Python dictionaries.
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def parse(self):
        """
        Read the CSV file and return all records.
        """

        try:
            dataframe = pd.read_csv(self.file_path)

            records = dataframe.to_dict(orient="records")

            return records

        except Exception as e:
            print(f"Error reading CSV: {e}")
            return []