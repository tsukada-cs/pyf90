#%%
import os
import site
site.addsitedir(f"{os.environ['HOME']}/git")

import numpy as np

import pyfort
#%%
a = 10
b = pyfort.myext.sub1_1(a)
b
# %%
a = 10
b = pyfort.myext.sub2_1(a)
b
# %%
a = [10,20,30]
b = [1,2,3]
c = pyfort.myext.sub2_2(a, b)
print(c)
# %%
