import os
import pandas as pd

def main():
    # Directory where Fitbit Exercise json Files are
    directory = '../data/user-site-export/exercise/'

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

    # # Print Unique Activity Names
    # print(df.activityName.unique())

    # Use only the relevant columns
    fields = ['logId', 'activityName', 'startTime', 'duration', 'distance', 'distanceUnit']
    df = df[fields]

    print (df)
    
    # Output DataFrame to CSV
    df.to_csv('../data/output/workouts.csv')
    return


if __name__ == '__main__':
    main()
