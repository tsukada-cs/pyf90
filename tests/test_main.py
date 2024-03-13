#%%
import pyf90
#%%
a = 10
b = pyf90.futils.sub1_1(a)
assert b == 11
# %%
a = 10
b = pyf90.futils.sub2_1(a)
assert b == 9
# %%
a = [10,20,30]
b = [1,2,3]
c = pyf90.futils.sub2_2(a, b)
print(c)
# %%
