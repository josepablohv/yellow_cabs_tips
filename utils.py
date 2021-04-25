import random
import pandas as pd

def read_csv_sample(filename: str, sample_proportion: float=0.1):
    """
    Returns a Pandas dataframe of a sample of a csv file.

    Parameters
    ----------
    filename : str
        absolute or relative path of the csv file to read
    
    sample_proportion : float, optional
        decimal proportion from 0 to 1 of the sample size (default 0.1)

    Returns
    ------
    pandas.Dataframe
        dataframe containing a random sample of filename
    """
    print(f"Filename: {filename}")
    n = sum(1 for line in open(filename)) - 1 #number of records in file (excludes header)
    s = int(sample_proportion * n) #desired sample size
    print(f"Total number of rows: {n}")
    print(f"Reading: {s}")
    skip = sorted(random.sample(range(1,n+1),n-s))
    return pd.read_csv(filename, skiprows=skip)
