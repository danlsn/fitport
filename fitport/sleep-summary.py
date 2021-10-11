import os
import json
import pandas as pd


def main():
    # Directory where Fitbit Sleep json Files are
    directory = '../data/user-site-export/sleep/'

    # Empty list to hold json data
    json_data = list()

    # Iterate over each json file in directory
    for filename in os.listdir(directory):
        if filename.startswith("sleep-"):
            # Open and load json file and close when done
            with open(os.path.join(directory, filename)) as f:
                json_data.extend(json.load(f))

    df = pd.json_normalize(json_data)
    print(df)

    df.to_csv('../data/output/sleep.csv')
    return


if __name__ == '__main__':
    main()
