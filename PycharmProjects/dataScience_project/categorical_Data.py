import pandas as pd

crimes_df = pd.read_csv('crimes4.csv', header=0, index_col=None)
del crimes_df['Unnamed: 0']
crimesandschools_df = pd.read_csv('crimes_schools_old.csv', header=0, index_col=None)

new_df = pd.DataFrame.copy(crimes_df, deep=True)
print(1, len(new_df))
new_df = new_df.drop(['Descript', 'Location'], axis=1)
print(2, len(new_df))
bakalim = pd.DataFrame.copy(new_df, deep=True)
new_df = pd.concat([new_df, crimesandschools_df['Supervisor District'],
                    crimesandschools_df['General Type'],
                    crimesandschools_df['Distance'],
                    crimesandschools_df['School Type']], axis=1)
print(3, len(new_df))
new_df = pd.concat([new_df, crimesandschools_df['Sample num'],
                    crimesandschools_df['Descript']], axis=1)
print(4, len(new_df))
new_df.to_csv('categorical_data.csv')

print(5, len(new_df))
# new_df = new_df.sample(frac=1)
test_df = pd.DataFrame.copy(new_df.iloc[-5000:, :], deep=True)
new_df = new_df.iloc[:-5000, :]
print(len(test_df), len(new_df))
pd.DataFrame.to_csv(test_df, 'categorical_TESTING.csv')
pd.DataFrame.to_csv(new_df, 'categorical_TRAINING.csv')