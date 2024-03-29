# environment name : cdata
from AutoClean import AutoClean
import pandas as pd
import numpy as np
df = pd.read_csv('admission.csv')
# pipeline = AutoClean(df)
# cleaned_df = pipeline.output


# df.to_csv('filename.csv', index=False)

obj = AutoClean(df)

obj.__str__()