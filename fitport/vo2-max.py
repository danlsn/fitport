import os
import pandas as pd
import json


def main():
    # Directory where Fitbit Demographic VO2 Max json Files are
    directory = '../data/user-site-export/demographic_vo2_max/'

    # Empty list to hold json data
    json_data = list()

    # Iterate over each json file in directory
    for filename in os.listdir(directory):
        if filename.startswith("demographic_vo2_max-"):
            # Open and load json file and close when done
            with open(os.path.join(directory, filename)) as f:
                json_data.extend(json.load(f))

    df = pd.json_normalize(json_data)
    print(df.info())
    print(df)
    df.to_csv('../data/output/demographic-vo2-max.csv')
    df['dateTime'] = pd.to_datetime(df['dateTime'])

    fields = ['dateTime', 'value.filteredDemographicVO2Max']

    df = df[fields]
    df['dateTime'] = df['dateTime'].astype(str)
    df.to_json('../data/output/demographic-vo2-max.json', orient='records')

    return


if __name__ == '__main__':
    main()
