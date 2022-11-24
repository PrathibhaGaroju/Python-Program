import pandas as pd
import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])


ser = pd.Series(data, index=[10, 11, 12, 13, 14])

print(ser);
