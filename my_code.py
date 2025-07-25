import pandas as pd
import os

data = { #dictionary
    'Name': ["Alice", "Bob", "Charlie"],
    'Age' : [25,30,35],
    'City': ["New York", "Log Angeles", "Chicago"],
}

df = pd.DataFrame(data)

# # Adding new row to df for v2
# new_row_loc = {'Name': 'V2', 'Age': 20, 'City':'City1'}
#df.loc[len(df.inddex)] = new_row_loc

# new_row_loc2 = {'Name': 'V3', 'Age': 30, 'City':'City1'}
#df.loc[len(df.inddex)] = new_row_loc2

#ensure the "data" directory exists at a root level
data_dir = "data" #here we are creating a directory named data and are storing in a name data_dir
os.makedirs(data_dir,exist_ok=True)

#define the file path
file_path = os.path.join(data_dir,'sample_data.csv')

#save the dataframe to a csv file,including column names
df.to_csv(file_path, index=False)

print(f"csv file saved to {file_path}")