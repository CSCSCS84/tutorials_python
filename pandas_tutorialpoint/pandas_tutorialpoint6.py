# Options and Custimization

import pandas as pd

print(pd.get_option("display.max_rows"))
pd.set_option("display.max_rows", 80)

print(pd.get_option("display.max_rows"))
pd.reset_option("display.max_rows")

# alle Optionen beschrieben
pd.describe_option()
print()
print()
pd.describe_option("display.max_rows")

# options are only changed in with block
with pd.option_context("display.max_rows", 10):
    print(pd.get_option("display.max_rows"))
    print(pd.get_option("display.max_rows"))
