import pandas as pd
import numpy as np
import matplotlib.pyplot as p
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import chart_studio.plotly as py

import cufflinks as cf

print(__version__) # requires version >= 1.9.0

cf.go_offline()
df2 = pd.DataFrame({'Category':['A','B','C'],'Values':[32,43,50]})
df2.iplot(kind='bar',x='Category',y='Values')

p.show()