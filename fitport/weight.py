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
    df['datetime'] = pd.to_datetime(df['logId'], unit='ms')
    df['datetime'] = df['datetime'].astype(str)

    # Calculate Lean Body Mass Percentage and Calculated Column
    df['lean_pct'] = 100 - df.fat
    df['lean_weight'] = df.weight * (df.lean_pct/100)

    # Output DataFrame to CSV File
    df_output = df[['datetime', 'weight', 'bmi', 'fat', 'lean_weight']]
    output_file = '../data/output/weight.json'

    df_output.to_json(output_file, orient='records')


if __name__ == '__main__':
    main()
