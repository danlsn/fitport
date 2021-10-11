import os
import json
import pandas as pd
import datetime


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
                j_array = json.load(f)
                for j in j_array:
                    json_data.extend(j['levels']['data'])

    # Create DataFrame from all sleep state readings
    df = pd.DataFrame(json_data)
    df['start_time'] = pd.to_datetime(df['dateTime'])
    df['end_time'] = pd.to_datetime(df['dateTime']) + pd.to_timedelta(df['seconds'], unit='s')
    print(df.info())
    print(df.level.unique())
    
    df['type'] = df['level']
    df['type'] = df['type'].str.replace('(awake|wake)', 'awake', regex=True)
    df['type'] = df['type'].str.replace('(restless|asleep|light|deep|rem)', 'asleep', regex=True)
    print(df['type'])
    
    FIELDS = ['start_time', 'end_time', 'type']
    df_output = df[FIELDS]
    df_output['start_time'] = df_output['start_time'].astype(str)
    df_output['end_time'] = df_output['end_time'].astype(str)
    df_output.to_json('../data/output/sleep-state-readings-working.json', orient='records', date_format='iso')
    # df.to_csv('../data/output/sleep-state-readings.csv')
    
    return


if __name__ == '__main__':
    main()
