import os
import pandas as pd
import json


def main():
    # Directory where Fitbit Resting HR json Files are
    directory = '../data/user-site-export/resting_heart_rate/'

    # Empty list to hold json data
    json_data = list()

    # Iterate over each json file in directory
    for filename in os.listdir(directory):
        if filename.startswith("resting_heart_rate-"):
            # Open and load json file and close when done
            with open(os.path.join(directory, filename)) as f:
                json_data.extend(json.load(f))

    df = pd.json_normalize(json_data)
    df = df.loc[df['value.date'].notnull()]

    print(df.info())
    print(df)
    df.to_csv('../data/output/resting-heart-rate.csv')
    df['dateTime'] = pd.to_datetime(df['dateTime'])
    
    fields = ['dateTime', 'value.value']
    
    df = df[fields]
    df['dateTime'] = df['dateTime'].astype(str)
    df.to_json('../data/output/resting-heart-rate.json', orient='records')
    
    return


if __name__ == '__main__':
    main()
