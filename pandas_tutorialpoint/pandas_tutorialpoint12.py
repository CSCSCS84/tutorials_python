import pandas as pd
import numpy as np

# sparse data functionality as been removed:

# SparseSeries, SparseDataFrame and the DataFrame.to_sparse method have been removed (GH28425).
# We recommend using a Series or DataFrame with sparse values instead. See Migrating for
# help with migrating existing code.

# now SparseDataFrame can be used:
dfsparse = pd.DataFrame({"A": pd.arrays.SparseArray([0, 1])})
print(dfsparse)
# später erledigen
