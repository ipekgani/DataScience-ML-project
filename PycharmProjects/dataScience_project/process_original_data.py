import pandas as pd

# crimes_df = pd.read_csv('_Change_Notice__Police_Department_Incidents.csv', header=0, index_col=None)
crimes_df = pd.read_csv('crimes.csv', header=0, index_col=0)
# crimes_df = crimes_df.drop(['Category', 'IncidntNum', 'Address', 'PdId', 'Location'], axis=1)
# for i in range(len(crimes_df)):
#     print(i)
#     crimes_df.loc[i, 'Time'] = crimes_df.loc[i, 'Time'][:2]
#     month = int(crimes_df.loc[i, 'Date'][:2])
#
#     if month in [12, 1, 2]:
#         crimes_df.loc[i, 'Date'] = 'Winter'
#     elif month in [3, 4, 5]:
#         crimes_df.loc[i, 'Date'] = 'Spring'
#     elif month in [6, 7, 8]:
#         crimes_df.loc[i, 'Date'] = 'Summer'
#     else:
#         crimes_df.loc[i, 'Date'] = 'Fall'

# days_df = pd.get_dummies(crimes_df['DayOfWeek'])
# seasons_df = pd.get_dummies(crimes_df['Date'])
# pd_df = pd.get_dummies(crimes_df['PdDistrict'])
# resol_df = pd.get_dummies(crimes_df['Resolution'])

# crimes_df = pd.concat([crimes_df, days_df, seasons_df, pd_df, resol_df], axis=1)

# crimes_df = crimes_df.drop(['DayOfWeek', 'Date', 'Location', 'PdDistrict', 'Resolution'], axis=1)

# print(crimes_df['Descript'].unique(), len(crimes_df['Descript'].unique()))

# MAPPING DESCRIPTIONS TO GENERALIZED INTEGER LABELS.
# for i in range(len(crimes_df)):
#     print(i)
#     if 'MARIJUANA' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 0
#     elif 'COCAINE' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 1
#     elif 'METH' in crimes_df.loc[i, 'Descript'] or 'AMPHETAMINE' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 2
#     elif 'OPIATES' in crimes_df.loc[i, 'Descript'] or 'OPIUM' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 3
#     elif 'HEROIN' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 4
#     elif 'FORGE' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 5
#     elif 'HALLUCINOGENIC' in crimes_df.loc[i, 'Descript']:
#         crimes_df.loc[i, 'Descript'] = 6
#     else:
#         crimes_df = crimes_df.drop(i, axis=0)

# pd.DataFrame.to_csv(crimes_df, 'crimes5.csv')

