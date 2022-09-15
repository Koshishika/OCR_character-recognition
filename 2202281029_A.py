import pandas as pd

df = pd.read_csv('2202281029_A.csv', encoding='shift_jis')
stat = df.describe()
print(df)
print(stat)

df.head()
df.shape

mi = df.min()
ma = df.max()
me = df.mean()
md = df.median()
su = df.sum()
st = df.std()
print(df)
print('最小値\r\n' + str(mi))
print('最大値\r\n' + str(ma))
print('平均値\r\n' + str(me))
print('中央値\r\n ' + str(md))
print('合計値\r\n ' + str(su))
print('標準偏差\r\n ' + str(st))
