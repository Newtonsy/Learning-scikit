import pandas as pd
import numpy as np
import sklearn as sk
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
#create a DataFrame
data={"Feature1": [1.0, 2.0, None, 4.0], "Feature2": [5.0, None, 7.0, 8.0]}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

#handling missing values
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print("DataFrame after imputation:\n", df_imputed)