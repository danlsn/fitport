import json
import os
import pandas as pd


def main():
    # Directory where Fitbit Weight json Files are
    directory = '../data/user-site-export/weight/'

    # Empty Array of dataframes to hold json data
    dfs = []
    
    # Iterate over each json file in directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            # Open and load json file and close when done
            with open(os.path.join(directory, filename)) as f:
                data = pd.read_json(f)
                dfs.append(data)

    df = pd.concat(dfs, ignore_index=True)
    df['datetime'] = df['date'].astype(str) + ' ' + df['time']
    df['datetime'] = pd.to_datetime(df['datetime'])
    print(df[['datetime', 'weight', 'bmi', 'fat']])


if __name__ == '__main__':
    main()
