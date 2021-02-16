# Working with Text Data

import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])

print(s)

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234', 'SteveSmith'])

print(s.str.lower())
print(s.str.len())
# diverse string operationen funktionieren so: split, strip, contains, replace


s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
# concatenate the elements in the serie
print(s.str.cat(sep='_'))

# get_dummies() unklar

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

# repeats each element two times
print(s.str.repeat(2))

# startswith, endtwith, find, findall, swapcase etc.
