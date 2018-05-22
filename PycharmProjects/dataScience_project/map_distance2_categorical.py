import pandas as pd
import stat
df = pd.read_csv('categorical_data/categorical_data.csv', header=0, index_col=0)
lenOG = len(df)
x = pd.DataFrame(columns=df.columns)
for i in range(len(df)):
    dist = df.loc[i, 'Distance']
    if dist >= 3611:
        x = x.append(df.iloc[i, :])
        df = df.drop(i, axis=0)
#
# print()
# print("max", max(df['Distance']))
# print("min", min(df['Distance']))
# print("std", df['Distance'].std())
# print("mean", df['Distance'].mean())
# sorted = df.sort_values('Distance', ascending=False)
#
# std = df['Distance'].std()
# mean = df['Distance'].mean()
#
# for i in range(lenOG):
#     if i not in df.index:
#         continue
#     dist = df.loc[i, 'Distance']
#     if dist > (mean + std):
#         df.loc[i, 'Distance'] = 'very far'
#     elif (dist <= (mean + std)) & (dist > mean):
#         df.loc[i, 'Distance'] = 'far'
#     elif (dist <= mean) & (dist > (mean-std)):
#         df.loc[i, 'Distance'] = 'close'
#     elif dist <= (mean-std):
#         df.loc[i, 'Distance'] = 'very close'
#
# print(df['Distance'].unique())
#
