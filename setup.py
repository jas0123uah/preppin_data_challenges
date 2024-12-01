import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--year", "-y", help="Year of the challenge to create directories and starter files for", type=int, required=True)
parser.add_argument("--maximum_challenge_number", "-n", help="The highest challenge number to create for the given year", type=int, required=True)
args = parser.parse_args()

def create_directories(year: int, max_challenge_number: int):
    """
    Create prepped_data directories for a given year and maximum challenge number.
    Each week (challenge number) will have a directory created under the prepped_data directory.
    If the directories already exist, this function will not raise an error.
    Parameters
    ----------
    year : int
        The year of the challenge data to be prepped.
    max_challenge_number : int
        The highest challenge number to create directories for.
    Returns
    -------
    None
    """
    # Get the absolute path to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for challenge_number in range(1, max_challenge_number + 1):
        prepped_data_path = f"{script_dir}/prepped_data/{year}/week_{challenge_number}"
        raw_data_path = f"{script_dir}/raw_data/{year}/week_{challenge_number}"
        workbook_path = f"{script_dir}/workbooks/{year}/week_{challenge_number}"
        solution_path = f"{script_dir}/solutions/{year}/week_{challenge_number}"
        os.makedirs(prepped_data_path, exist_ok=True)
        os.makedirs(raw_data_path, exist_ok=True)
        os.makedirs(workbook_path, exist_ok=True)
        os.makedirs(solution_path, exist_ok=True)

def create_starter_files(year: int, max_challenge_number: int):
    """
    Create starter files for a given year and maximum challenge number.
    Each week (challenge number) will have a starter file created under the prepped_data directory.
    If the starter files already exist, this function will not raise an error.
    Parameters
    ----------
    year : int
        The year of the challenge data to be prepped.
    max_challenge_number : int
        The highest challenge number to create starter files for.
    Returns
    -------
    None
    """
    # Get the absolute path to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    for challenge_number in range(1, max_challenge_number + 1):
        starter_file_path = f"{script_dir}/workbooks/{year}/week_{challenge_number}/week_{challenge_number}.ipynb"
        if not os.path.exists(starter_file_path):
            with open(starter_file_path, "w") as f:
                f.write("# Write your code here\n")
        else:
            print(f"Starter file for week {challenge_number} already exists")
if __name__ == "__main__":
    create_directories(args.year, args.maximum_challenge_number)
    create_starter_files(args.year, args.maximum_challenge_number)
