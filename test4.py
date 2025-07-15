import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#create a DataFrame with random data
data= {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "Salary": [50000, 60000, 70000]}
df = pd.DataFrame(data)
#Save the DataFrame to a CSV file
df.to_csv("dataset.csv", index=False)
#Read the CSV file into a DataFrame
df_read = pd.read_csv("dataset.csv")
#Display the DataFrame
print(df_read)
