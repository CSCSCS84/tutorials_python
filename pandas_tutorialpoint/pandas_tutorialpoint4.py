import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10, 2), index=[1, 4, 6, 2, 3, 5, 9, 8, 0, 7], columns=['col2', 'col1'])

sorted_df = unsorted_df.sort_index(axis=1, ascending=False)
print(sorted_df)
# mehrer Spalten können ebenfalls als Argument übergeben werden
sorted_df = sorted_df.sort_values(by="col2")
print(sorted_df)

unsorted_df = pd.DataFrame({'col1': [2, 1, 1, 1], 'col2': [1, 3, 2, 4]})
sorted_df = unsorted_df.sort_values(by='col1', kind='mergesort')

print(sorted_df)
