import sklearn
import numpy as np
import pandas as pd
print("Sciki-learn Version: ", sklearn.__version__)
#numpy operations
array =np.array([1,2,3,4,5,6])
print("Numpy array: ", array)
print("Mean of array: ", np.mean(array))

#pandas operations
data= {"Name": ["Alice", "Bob", "Charlie"],"Age": [25,26,17]}
df= pd.DataFrame(data)
print("Pandas DataFrame:\n",df)
print("Average age: ", df['Age'].mean())