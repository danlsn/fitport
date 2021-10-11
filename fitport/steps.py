import os
import json
import pandas as pd


def main():
    # Directory where Fitbit steps json Files are
    directory = '../data/user-site-export/steps/'

    # Empty list to hold json data
    json_data = list()

    # Iterate over each json file in directory
    for filename in os.listdir(directory):
        if filename.startswith("steps-"):
            # Open and load json file and close when done
            with open(os.path.join(directory, filename)) as f:
                json_data.extend(json.load(f))

    df = pd.json_normalize(json_data)
    df['value'] = df['value'].astype(int)
    df = df[df['value'] > 0]
    print(df)
    print(df.info())
    df['dateTime'] = pd.to_datetime(df['dateTime'])
    df.to_csv('../data/output/steps.csv')

    df['dateTime'] = df['dateTime'].astype(str)

    df.to_json('../data/output/steps.json', orient='records')
    return


if __name__ == '__main__':
    main()
